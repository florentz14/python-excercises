-- =============================================================
--  stocks.db  |  Extended & Optimized Schema
--  SQLite 3.x  |  Stock portfolio / trade log
-- =============================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- -------------------------------------------------------------
-- 1. CATALOG: instruments
--    Replaces the bare TEXT symbol with instrument metadata.
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS instruments (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker      TEXT    NOT NULL UNIQUE,        -- e.g. 'AAPL', 'GOOG'
    name        TEXT    NOT NULL,               -- e.g. 'Apple Inc.'
    sector      TEXT,                           -- e.g. 'Technology'
    market_cap  TEXT,                           -- 'large', 'mid', 'small'
    currency    TEXT    NOT NULL DEFAULT 'USD'
                CHECK  (length(currency) = 3),  -- ISO 4217
    is_active   INTEGER NOT NULL DEFAULT 1      -- soft delete flag
                CHECK  (is_active IN (0, 1))
);

-- -------------------------------------------------------------
-- 2. CATALOG: transaction_types
--    Replaces the bare TEXT trans ('BUY'/'SELL') with a proper
--    catalog that can accommodate DIVIDEND, SPLIT, etc.
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS transaction_types (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    code        TEXT    NOT NULL UNIQUE,        -- e.g. 'BUY', 'SELL', 'DIV'
    label       TEXT    NOT NULL,               -- e.g. 'Purchase', 'Sale'
    affects_qty INTEGER NOT NULL DEFAULT 0      -- +1 increases position, -1 decreases, 0 neutral
                CHECK  (affects_qty IN (-1, 0, 1))
);

-- -------------------------------------------------------------
-- 3. CATALOG: brokers
--    Tracks which broker executed the trade (optional FK).
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS brokers (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT    NOT NULL UNIQUE,
    commission_rate REAL    NOT NULL DEFAULT 0.0
                    CHECK  (commission_rate >= 0)
);

-- -------------------------------------------------------------
-- 4. CATALOG: portfolios
--    Allows grouping trades into named portfolios.
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS portfolios (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,
    description TEXT
);

-- -------------------------------------------------------------
-- 5. MAIN TABLE: trades
--    One row per trade execution. Replaces original `stocks`.
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS trades (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,

    trade_date          TEXT    NOT NULL
                        CHECK  (trade_date GLOB '????-??-??'),

    instrument_id       INTEGER NOT NULL REFERENCES instruments(id)        ON UPDATE CASCADE ON DELETE RESTRICT,
    transaction_type_id INTEGER NOT NULL REFERENCES transaction_types(id)  ON UPDATE CASCADE ON DELETE RESTRICT,
    broker_id           INTEGER          REFERENCES brokers(id)            ON UPDATE CASCADE ON DELETE SET NULL,

    qty                 INTEGER NOT NULL CHECK (qty > 0),
    price               REAL    NOT NULL CHECK (price > 0),
    commission          REAL    NOT NULL DEFAULT 0.0 CHECK (commission >= 0),

    -- Stored generated column: total cost/proceeds including commission
    total_amount        REAL    GENERATED ALWAYS AS (
                            ROUND(qty * price + commission, 4)
                        ) STORED,

    notes               TEXT,
    created_at          TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- -------------------------------------------------------------
-- 6. JUNCTION TABLE: portfolio_trades  (M:N portfolios <-> trades)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS portfolio_trades (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    portfolio_id INTEGER NOT NULL REFERENCES portfolios(id) ON UPDATE CASCADE ON DELETE CASCADE,
    trade_id     INTEGER NOT NULL REFERENCES trades(id)     ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE (portfolio_id, trade_id)
);

-- -------------------------------------------------------------
-- 7. INDEXES
-- -------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_trades_date            ON trades(trade_date);
CREATE INDEX IF NOT EXISTS idx_trades_instrument      ON trades(instrument_id);
CREATE INDEX IF NOT EXISTS idx_trades_type            ON trades(transaction_type_id);
CREATE INDEX IF NOT EXISTS idx_trades_instrument_date ON trades(instrument_id, trade_date);
CREATE INDEX IF NOT EXISTS idx_pt_portfolio           ON portfolio_trades(portfolio_id);
CREATE INDEX IF NOT EXISTS idx_pt_trade               ON portfolio_trades(trade_id);

-- -------------------------------------------------------------
-- 8. VIEW: trade_log  (backwards-compatible with original schema)
-- -------------------------------------------------------------
CREATE VIEW IF NOT EXISTS trade_log AS
SELECT
    t.id,
    t.trade_date,
    tt.code             AS trans,
    tt.label            AS trans_label,
    i.ticker            AS symbol,
    i.name              AS company,
    i.sector,
    t.qty,
    t.price,
    t.commission,
    t.total_amount,
    b.name              AS broker,
    t.notes,
    t.created_at
FROM trades t
JOIN  instruments      i  ON i.id  = t.instrument_id
JOIN  transaction_types tt ON tt.id = t.transaction_type_id
LEFT JOIN brokers      b  ON b.id  = t.broker_id;

-- -------------------------------------------------------------
-- 9. VIEW: positions  (current open position per instrument)
--    affects_qty (+1 BUY / -1 SELL) drives net qty generically.
-- -------------------------------------------------------------
CREATE VIEW IF NOT EXISTS positions AS
SELECT
    i.id            AS instrument_id,
    i.ticker,
    i.name          AS company,
    i.sector,
    SUM(tt.affects_qty * t.qty)                                             AS net_qty,
    ROUND(
        SUM(CASE WHEN tt.affects_qty = 1 THEN t.total_amount ELSE 0 END) /
        NULLIF(SUM(CASE WHEN tt.affects_qty = 1 THEN t.qty ELSE 0 END), 0)
    , 4)                                                                    AS avg_cost_basis,
    SUM(CASE WHEN tt.affects_qty =  1 THEN t.total_amount ELSE 0 END)      AS total_invested,
    SUM(CASE WHEN tt.affects_qty = -1 THEN t.total_amount ELSE 0 END)      AS total_proceeds
FROM trades t
JOIN instruments       i  ON i.id  = t.instrument_id
JOIN transaction_types tt ON tt.id = t.transaction_type_id
GROUP BY i.id
HAVING net_qty > 0;

-- =============================================================
--  SEED DATA
-- =============================================================

INSERT OR IGNORE INTO instruments (ticker, name, sector) VALUES
('RHAT', 'Red Hat Inc.',    'Technology'),
('GOOG', 'Alphabet Inc.',   'Technology'),
('MSFT', 'Microsoft Corp.', 'Technology'),
('AAPL', 'Apple Inc.',      'Technology'),
('IBM',  'IBM Corp.',       'Technology');

INSERT OR IGNORE INTO transaction_types (code, label, affects_qty) VALUES
('BUY',   'Purchase',    1),
('SELL',  'Sale',       -1),
('DIV',   'Dividend',    0),
('SPLIT', 'Stock split', 1);

INSERT OR IGNORE INTO brokers (name, commission_rate) VALUES
('Default Broker', 0.0);

INSERT OR IGNORE INTO portfolios (name, description) VALUES
('Main', 'Default portfolio');

INSERT INTO trades (trade_date, instrument_id, transaction_type_id, broker_id, qty, price) VALUES
('2006-01-05', (SELECT id FROM instruments WHERE ticker='RHAT'), (SELECT id FROM transaction_types WHERE code='BUY'),  1, 100, 35.14),
('2006-01-10', (SELECT id FROM instruments WHERE ticker='GOOG'), (SELECT id FROM transaction_types WHERE code='BUY'),  1,  50, 432.50),
('2006-01-12', (SELECT id FROM instruments WHERE ticker='RHAT'), (SELECT id FROM transaction_types WHERE code='SELL'), 1,  30, 38.20),
('2006-01-18', (SELECT id FROM instruments WHERE ticker='MSFT'), (SELECT id FROM transaction_types WHERE code='BUY'),  1, 200, 26.75),
('2006-01-22', (SELECT id FROM instruments WHERE ticker='AAPL'), (SELECT id FROM transaction_types WHERE code='BUY'),  1,  75, 85.40),
('2006-01-25', (SELECT id FROM instruments WHERE ticker='GOOG'), (SELECT id FROM transaction_types WHERE code='SELL'), 1,  25, 445.00),
('2006-02-01', (SELECT id FROM instruments WHERE ticker='IBM'),  (SELECT id FROM transaction_types WHERE code='BUY'),  1,  40, 78.90),
('2006-02-08', (SELECT id FROM instruments WHERE ticker='MSFT'), (SELECT id FROM transaction_types WHERE code='SELL'), 1, 100, 27.10),
('2006-02-14', (SELECT id FROM instruments WHERE ticker='RHAT'), (SELECT id FROM transaction_types WHERE code='BUY'),  1,  60, 36.50);

INSERT OR IGNORE INTO portfolio_trades (portfolio_id, trade_id)
SELECT 1, id FROM trades;

-- =============================================================
--  SAMPLE QUERIES
-- =============================================================

-- Trade log (backwards-compatible with original `stocks` schema)
-- SELECT trade_date AS date, trans, symbol, qty, price, total_amount
-- FROM trade_log
-- ORDER BY trade_date;

-- Open positions with average cost basis
-- SELECT ticker, company, net_qty, avg_cost_basis, total_invested, total_proceeds
-- FROM positions
-- ORDER BY ticker;

-- Realized P&L (proceeds minus cost basis of sold shares)
-- SELECT
--     tl.symbol,
--     SUM(CASE WHEN tl.trans='SELL' THEN tl.total_amount ELSE 0 END)           AS proceeds,
--     SUM(CASE WHEN tl.trans='SELL' THEN tl.qty * p.avg_cost_basis ELSE 0 END) AS cost_of_sold,
--     ROUND(
--         SUM(CASE WHEN tl.trans='SELL' THEN tl.total_amount ELSE 0 END) -
--         SUM(CASE WHEN tl.trans='SELL' THEN tl.qty * p.avg_cost_basis ELSE 0 END)
--     , 2) AS realized_pnl
-- FROM trade_log tl
-- LEFT JOIN positions p ON p.ticker = tl.symbol
-- GROUP BY tl.symbol
-- HAVING proceeds > 0
-- ORDER BY realized_pnl DESC;

-- Monthly trading volume
-- SELECT
--     strftime('%Y-%m', trade_date) AS month,
--     COUNT(*)                      AS num_trades,
--     SUM(CASE WHEN trans='BUY'  THEN total_amount ELSE 0 END) AS total_bought,
--     SUM(CASE WHEN trans='SELL' THEN total_amount ELSE 0 END) AS total_sold
-- FROM trade_log
-- GROUP BY month
-- ORDER BY month;