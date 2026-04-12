-- Schema and seed for stocks example (used by 12_stocks.py)

CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    trans TEXT,
    symbol TEXT,
    qty INTEGER,
    price REAL
);

INSERT INTO stocks (date, trans, symbol, qty, price) VALUES
('2006-01-05', 'BUY', 'RHAT', 100, 35.14),
('2006-01-10', 'BUY', 'GOOG', 50, 432.50),
('2006-01-12', 'SELL', 'RHAT', 30, 38.20),
('2006-01-18', 'BUY', 'MSFT', 200, 26.75),
('2006-01-22', 'BUY', 'AAPL', 75, 85.40),
('2006-01-25', 'SELL', 'GOOG', 25, 445.00),
('2006-02-01', 'BUY', 'IBM', 40, 78.90),
('2006-02-08', 'SELL', 'MSFT', 100, 27.10),
('2006-02-14', 'BUY', 'RHAT', 60, 36.50);
