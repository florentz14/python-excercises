-- =============================================================================
-- FAMILY BUDGET & WEALTH MANAGEMENT - PostgreSQL Complete Script
-- Includes: Schema + Sample Data + Views + Functions + Triggers
-- =============================================================================

-- =============================================================================
-- PART 1: SCHEMA
-- =============================================================================

-- Drop existing tables (safe re-run)
DROP TABLE IF EXISTS
    debt_payments, debts, savings_contributions, savings_goals,
    investment_transactions, investments, investment_accounts,
    insurance_claims, insurance_asset_links, insurance_policies, insurance_companies,
    vehicle_expenses, vehicle_loan_payments, vehicle_loans, vehicles,
    mortgage_payments, mortgages, properties,
    other_assets, transfers, card_statements, cards,
    payment_methods, bank_accounts, banks,
    budget_alerts, budgets, expenses, expense_subcategories, expense_categories,
    incomes, income_categories, recurring_items,
    members, households,
    audit_logs, sessions, user_permission, user_role,
    role_permission, permissions, roles, users
CASCADE;

-- ---------------------------------------------------------------------------
-- SECURITY
-- ---------------------------------------------------------------------------
CREATE TABLE users (
    user_id       SERIAL PRIMARY KEY,
    full_name     VARCHAR(120)  NOT NULL,
    email         VARCHAR(180)  NOT NULL UNIQUE,
    password_hash VARCHAR(255)  NOT NULL,
    phone         VARCHAR(30),
    avatar_url    VARCHAR(500),
    status        VARCHAR(20)   NOT NULL DEFAULT 'active'
                      CHECK (status IN ('active','inactive','suspended')),
    last_login    TIMESTAMP,
    created_at    TIMESTAMP     NOT NULL DEFAULT NOW()
);

CREATE TABLE roles (
    role_id        SERIAL PRIMARY KEY,
    name           VARCHAR(60)  NOT NULL UNIQUE,
    description    VARCHAR(255),
    is_system_role BOOLEAN      NOT NULL DEFAULT FALSE,
    created_at     TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE permissions (
    permission_id SERIAL PRIMARY KEY,
    code          VARCHAR(100)  NOT NULL UNIQUE,
    name          VARCHAR(120)  NOT NULL,
    description   VARCHAR(255),
    module        VARCHAR(60),
    created_at    TIMESTAMP     NOT NULL DEFAULT NOW()
);

CREATE TABLE role_permission (
    role_permission_id SERIAL PRIMARY KEY,
    role_id            INT NOT NULL REFERENCES roles(role_id) ON DELETE CASCADE,
    permission_id      INT NOT NULL REFERENCES permissions(permission_id) ON DELETE CASCADE,
    granted_at         TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (role_id, permission_id)
);

CREATE TABLE user_role (
    user_role_id SERIAL PRIMARY KEY,
    user_id      INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    role_id      INT NOT NULL REFERENCES roles(role_id) ON DELETE CASCADE,
    assigned_by  INT REFERENCES users(user_id),
    assigned_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    expires_at   TIMESTAMP,
    UNIQUE (user_id, role_id)
);

CREATE TABLE user_permission (
    user_permission_id SERIAL PRIMARY KEY,
    user_id            INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    permission_id      INT NOT NULL REFERENCES permissions(permission_id) ON DELETE CASCADE,
    granted            BOOLEAN  NOT NULL DEFAULT TRUE,
    granted_by         INT REFERENCES users(user_id),
    granted_at         TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (user_id, permission_id)
);

CREATE TABLE sessions (
    session_id  SERIAL PRIMARY KEY,
    user_id     INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    token_hash  VARCHAR(255) NOT NULL UNIQUE,
    device_info VARCHAR(255),
    ip_address  VARCHAR(45),
    created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    expires_at  TIMESTAMP NOT NULL,
    revoked_at  TIMESTAMP
);

CREATE TABLE audit_logs (
    log_id      SERIAL PRIMARY KEY,
    user_id     INT REFERENCES users(user_id) ON DELETE SET NULL,
    action      VARCHAR(60)  NOT NULL,
    module      VARCHAR(60)  NOT NULL,
    entity_name VARCHAR(100) NOT NULL,
    entity_id   INT,
    old_value   JSONB,
    new_value   JSONB,
    ip_address  VARCHAR(45),
    device      VARCHAR(255),
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------------------
-- HOUSEHOLD & MEMBERS
-- ---------------------------------------------------------------------------
CREATE TABLE households (
    household_id      SERIAL PRIMARY KEY,
    name              VARCHAR(120) NOT NULL,
    currency          CHAR(3)      NOT NULL DEFAULT 'USD',
    country           VARCHAR(80),
    timezone          VARCHAR(60)  NOT NULL DEFAULT 'UTC',
    subscription_plan VARCHAR(30)  NOT NULL DEFAULT 'free'
                          CHECK (subscription_plan IN ('free','basic','premium')),
    active            BOOLEAN      NOT NULL DEFAULT TRUE,
    created_at        TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE members (
    member_id    SERIAL PRIMARY KEY,
    household_id INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    user_id      INT  REFERENCES users(user_id) ON DELETE SET NULL,
    nickname     VARCHAR(80)  NOT NULL,
    relationship VARCHAR(30)  NOT NULL DEFAULT 'member'
                     CHECK (relationship IN ('head','spouse','child','parent','other')),
    date_of_birth DATE,
    active        BOOLEAN   NOT NULL DEFAULT TRUE,
    joined_at     TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------------------
-- BANKS & ACCOUNTS
-- ---------------------------------------------------------------------------
CREATE TABLE banks (
    bank_id    SERIAL PRIMARY KEY,
    name       VARCHAR(120) NOT NULL,
    country    VARCHAR(80),
    swift_code VARCHAR(20),
    logo_url   VARCHAR(500),
    active     BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE bank_accounts (
    account_id            SERIAL PRIMARY KEY,
    household_id          INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id             INT  REFERENCES members(member_id) ON DELETE SET NULL,
    bank_id               INT  REFERENCES banks(bank_id) ON DELETE SET NULL,
    account_name          VARCHAR(120) NOT NULL,
    account_number_masked VARCHAR(30),
    account_type          VARCHAR(30)  NOT NULL
                              CHECK (account_type IN ('checking','savings','investment','pension')),
    currency              CHAR(3)       NOT NULL DEFAULT 'USD',
    opening_balance       NUMERIC(15,2) NOT NULL DEFAULT 0,
    current_balance       NUMERIC(15,2) NOT NULL DEFAULT 0,
    opening_date          DATE,
    interest_rate         NUMERIC(6,4),
    active                BOOLEAN      NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- CARDS
-- ---------------------------------------------------------------------------
CREATE TABLE cards (
    card_id            SERIAL PRIMARY KEY,
    household_id       INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id          INT  REFERENCES members(member_id) ON DELETE SET NULL,
    bank_account_id    INT  REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    bank_id            INT  REFERENCES banks(bank_id) ON DELETE SET NULL,
    card_name          VARCHAR(120) NOT NULL,
    card_type          VARCHAR(20)  NOT NULL CHECK (card_type IN ('credit','debit','prepaid')),
    last_four_digits   CHAR(4),
    brand              VARCHAR(30),
    credit_limit       NUMERIC(15,2),
    current_balance    NUMERIC(15,2) NOT NULL DEFAULT 0,
    available_credit   NUMERIC(15,2),
    billing_cycle_day  SMALLINT,
    payment_due_day    SMALLINT,
    expiration_month   SMALLINT,
    expiration_year    SMALLINT,
    is_primary         BOOLEAN NOT NULL DEFAULT FALSE,
    active             BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE card_statements (
    statement_id   SERIAL PRIMARY KEY,
    card_id        INT  NOT NULL REFERENCES cards(card_id) ON DELETE CASCADE,
    period_start   DATE NOT NULL,
    period_end     DATE NOT NULL,
    total_charges  NUMERIC(15,2) NOT NULL DEFAULT 0,
    minimum_payment NUMERIC(15,2),
    total_due      NUMERIC(15,2),
    due_date       DATE,
    paid_amount    NUMERIC(15,2) NOT NULL DEFAULT 0,
    paid_at        TIMESTAMP,
    status         VARCHAR(20) NOT NULL DEFAULT 'open'
                       CHECK (status IN ('open','paid','partial','overdue'))
);

-- ---------------------------------------------------------------------------
-- PAYMENT METHODS
-- ---------------------------------------------------------------------------
CREATE TABLE payment_methods (
    method_id    SERIAL PRIMARY KEY,
    household_id INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    name         VARCHAR(80)  NOT NULL,
    type         VARCHAR(30)  NOT NULL
                     CHECK (type IN ('cash','debit_card','credit_card','transfer','digital_wallet')),
    bank_account_id INT REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    card_id         INT REFERENCES cards(card_id) ON DELETE SET NULL,
    active          BOOLEAN NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- INCOME
-- ---------------------------------------------------------------------------
CREATE TABLE income_categories (
    category_id  SERIAL PRIMARY KEY,
    household_id INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    name         VARCHAR(80) NOT NULL,
    icon         VARCHAR(60),
    color        CHAR(7),
    active       BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE incomes (
    income_id          SERIAL PRIMARY KEY,
    member_id          INT  NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    category_id        INT  REFERENCES income_categories(category_id) ON DELETE SET NULL,
    bank_account_id    INT  REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    amount             NUMERIC(15,2) NOT NULL,
    date               DATE          NOT NULL,
    description        VARCHAR(255),
    frequency          VARCHAR(20)   NOT NULL DEFAULT 'once'
                           CHECK (frequency IN ('once','daily','weekly','biweekly','monthly','annual')),
    is_taxable         BOOLEAN NOT NULL DEFAULT FALSE,
    tax_amount         NUMERIC(15,2),
    net_amount         NUMERIC(15,2),
    recurring_end_date DATE,
    active             BOOLEAN   NOT NULL DEFAULT TRUE,
    created_at         TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------------------
-- EXPENSES
-- ---------------------------------------------------------------------------
CREATE TABLE expense_categories (
    category_id  SERIAL PRIMARY KEY,
    household_id INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    name         VARCHAR(80) NOT NULL,
    icon         VARCHAR(60),
    color        CHAR(7),
    is_fixed     BOOLEAN NOT NULL DEFAULT FALSE,
    active       BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE expense_subcategories (
    subcategory_id SERIAL PRIMARY KEY,
    category_id    INT  NOT NULL REFERENCES expense_categories(category_id) ON DELETE CASCADE,
    name           VARCHAR(80) NOT NULL,
    active         BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE expenses (
    expense_id        SERIAL PRIMARY KEY,
    household_id      INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id         INT  REFERENCES members(member_id) ON DELETE SET NULL,
    category_id       INT  REFERENCES expense_categories(category_id) ON DELETE SET NULL,
    subcategory_id    INT  REFERENCES expense_subcategories(subcategory_id) ON DELETE SET NULL,
    payment_method_id INT  REFERENCES payment_methods(method_id) ON DELETE SET NULL,
    amount            NUMERIC(15,2) NOT NULL,
    date              DATE          NOT NULL,
    description       VARCHAR(255),
    is_fixed          BOOLEAN NOT NULL DEFAULT FALSE,
    is_recurring      BOOLEAN NOT NULL DEFAULT FALSE,
    receipt_url       VARCHAR(500),
    installment_count  SMALLINT,
    installment_number SMALLINT,
    notes             TEXT,
    created_at        TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------------------
-- BUDGET
-- ---------------------------------------------------------------------------
CREATE TABLE budgets (
    budget_id    SERIAL PRIMARY KEY,
    household_id INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    category_id  INT  REFERENCES expense_categories(category_id) ON DELETE SET NULL,
    amount_limit NUMERIC(15,2) NOT NULL,
    month        SMALLINT      NOT NULL CHECK (month BETWEEN 1 AND 12),
    year         SMALLINT      NOT NULL,
    rollover_unused BOOLEAN    NOT NULL DEFAULT FALSE,
    notes        TEXT,
    created_at   TIMESTAMP     NOT NULL DEFAULT NOW(),
    UNIQUE (household_id, category_id, month, year)
);

CREATE TABLE budget_alerts (
    alert_id          SERIAL PRIMARY KEY,
    budget_id         INT  NOT NULL REFERENCES budgets(budget_id) ON DELETE CASCADE,
    threshold_percent SMALLINT NOT NULL CHECK (threshold_percent BETWEEN 1 AND 100),
    notified_at       TIMESTAMP,
    channel           VARCHAR(20) DEFAULT 'push'
                          CHECK (channel IN ('email','push','sms'))
);

-- ---------------------------------------------------------------------------
-- TRANSFERS
-- ---------------------------------------------------------------------------
CREATE TABLE transfers (
    transfer_id     SERIAL PRIMARY KEY,
    household_id    INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    from_account_id INT  REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    to_account_id   INT  REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    from_card_id    INT  REFERENCES cards(card_id) ON DELETE SET NULL,
    to_card_id      INT  REFERENCES cards(card_id) ON DELETE SET NULL,
    amount          NUMERIC(15,2) NOT NULL,
    fee             NUMERIC(15,2) NOT NULL DEFAULT 0,
    exchange_rate   NUMERIC(12,6) NOT NULL DEFAULT 1,
    date            DATE          NOT NULL,
    description     VARCHAR(255),
    status          VARCHAR(20)   NOT NULL DEFAULT 'completed'
                        CHECK (status IN ('pending','completed','failed','cancelled'))
);

-- ---------------------------------------------------------------------------
-- ASSETS — REAL ESTATE
-- ---------------------------------------------------------------------------
CREATE TABLE mortgages (
    mortgage_id         SERIAL PRIMARY KEY,
    bank_id             INT REFERENCES banks(bank_id) ON DELETE SET NULL,
    bank_account_id     INT REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    original_amount     NUMERIC(15,2) NOT NULL,
    outstanding_balance NUMERIC(15,2) NOT NULL,
    interest_rate       NUMERIC(6,4)  NOT NULL,
    rate_type           VARCHAR(20)   NOT NULL DEFAULT 'fixed'
                            CHECK (rate_type IN ('fixed','variable')),
    monthly_payment     NUMERIC(15,2) NOT NULL,
    start_date          DATE NOT NULL,
    end_date            DATE NOT NULL,
    payment_day         SMALLINT,
    status              VARCHAR(20) NOT NULL DEFAULT 'active'
                            CHECK (status IN ('active','paid','defaulted'))
);

CREATE TABLE properties (
    property_id             SERIAL PRIMARY KEY,
    household_id            INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    name                    VARCHAR(120) NOT NULL,
    property_type           VARCHAR(30)  NOT NULL
                                CHECK (property_type IN ('house','apartment','land','commercial','vacation')),
    address                 VARCHAR(255),
    city                    VARCHAR(80),
    state                   VARCHAR(80),
    country                 VARCHAR(80),
    zip_code                VARCHAR(20),
    purchase_date           DATE,
    purchase_price          NUMERIC(15,2),
    current_value           NUMERIC(15,2),
    market_value_updated_at DATE,
    is_primary_residence    BOOLEAN NOT NULL DEFAULT FALSE,
    is_rented               BOOLEAN NOT NULL DEFAULT FALSE,
    rental_income           NUMERIC(15,2),
    mortgage_id             INT REFERENCES mortgages(mortgage_id) ON DELETE SET NULL,
    active                  BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE mortgage_payments (
    payment_id        SERIAL PRIMARY KEY,
    mortgage_id       INT  NOT NULL REFERENCES mortgages(mortgage_id) ON DELETE CASCADE,
    payment_date      DATE          NOT NULL,
    amount_paid       NUMERIC(15,2) NOT NULL,
    principal_paid    NUMERIC(15,2) NOT NULL,
    interest_paid     NUMERIC(15,2) NOT NULL,
    remaining_balance NUMERIC(15,2) NOT NULL
);

-- ---------------------------------------------------------------------------
-- ASSETS — VEHICLES
-- ---------------------------------------------------------------------------
CREATE TABLE vehicle_loans (
    loan_id             SERIAL PRIMARY KEY,
    bank_id             INT REFERENCES banks(bank_id) ON DELETE SET NULL,
    original_amount     NUMERIC(15,2) NOT NULL,
    outstanding_balance NUMERIC(15,2) NOT NULL,
    interest_rate       NUMERIC(6,4)  NOT NULL,
    monthly_payment     NUMERIC(15,2) NOT NULL,
    start_date          DATE NOT NULL,
    end_date            DATE NOT NULL,
    status              VARCHAR(20) NOT NULL DEFAULT 'active'
                            CHECK (status IN ('active','paid','defaulted'))
);

CREATE TABLE vehicles (
    vehicle_id     SERIAL PRIMARY KEY,
    household_id   INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id      INT  REFERENCES members(member_id) ON DELETE SET NULL,
    make           VARCHAR(60)  NOT NULL,
    model          VARCHAR(60)  NOT NULL,
    year           SMALLINT     NOT NULL,
    color          VARCHAR(30),
    vin            VARCHAR(40),
    license_plate  VARCHAR(20),
    vehicle_type   VARCHAR(30)  NOT NULL DEFAULT 'car'
                       CHECK (vehicle_type IN ('car','motorcycle','truck','boat','rv')),
    purchase_date  DATE,
    purchase_price NUMERIC(15,2),
    current_value  NUMERIC(15,2),
    mileage        INT,
    fuel_type      VARCHAR(20),
    is_financed    BOOLEAN NOT NULL DEFAULT FALSE,
    loan_id        INT REFERENCES vehicle_loans(loan_id) ON DELETE SET NULL,
    active         BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE vehicle_loan_payments (
    payment_id        SERIAL PRIMARY KEY,
    loan_id           INT  NOT NULL REFERENCES vehicle_loans(loan_id) ON DELETE CASCADE,
    payment_date      DATE          NOT NULL,
    amount_paid       NUMERIC(15,2) NOT NULL,
    principal_paid    NUMERIC(15,2) NOT NULL,
    interest_paid     NUMERIC(15,2) NOT NULL,
    remaining_balance NUMERIC(15,2) NOT NULL
);

CREATE TABLE vehicle_expenses (
    expense_id         SERIAL PRIMARY KEY,
    vehicle_id         INT  NOT NULL REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    expense_type       VARCHAR(30) NOT NULL
                           CHECK (expense_type IN ('fuel','maintenance','repair','tax','parking','toll','other')),
    amount             NUMERIC(15,2) NOT NULL,
    date               DATE          NOT NULL,
    mileage_at_service INT,
    description        VARCHAR(255),
    provider           VARCHAR(120)
);

-- ---------------------------------------------------------------------------
-- ASSETS — OTHER
-- ---------------------------------------------------------------------------
CREATE TABLE other_assets (
    asset_id       SERIAL PRIMARY KEY,
    household_id   INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id      INT  REFERENCES members(member_id) ON DELETE SET NULL,
    name           VARCHAR(120) NOT NULL,
    asset_type     VARCHAR(30)  NOT NULL
                       CHECK (asset_type IN ('jewelry','art','electronics','furniture','collectible','other')),
    purchase_date  DATE,
    purchase_price NUMERIC(15,2),
    current_value  NUMERIC(15,2),
    description    TEXT,
    serial_number  VARCHAR(80),
    location       VARCHAR(120),
    active         BOOLEAN NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- INVESTMENTS
-- ---------------------------------------------------------------------------
CREATE TABLE investment_accounts (
    account_id            SERIAL PRIMARY KEY,
    household_id          INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id             INT  REFERENCES members(member_id) ON DELETE SET NULL,
    broker_name           VARCHAR(120) NOT NULL,
    account_name          VARCHAR(120) NOT NULL,
    account_number_masked VARCHAR(30),
    account_type          VARCHAR(30)  NOT NULL
                              CHECK (account_type IN ('brokerage','retirement','401k','ira','roth','pension')),
    currency              CHAR(3)       NOT NULL DEFAULT 'USD',
    opening_balance       NUMERIC(15,2) NOT NULL DEFAULT 0,
    current_value         NUMERIC(15,2) NOT NULL DEFAULT 0,
    opening_date          DATE,
    active                BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE investments (
    investment_id        SERIAL PRIMARY KEY,
    account_id           INT  NOT NULL REFERENCES investment_accounts(account_id) ON DELETE CASCADE,
    asset_type           VARCHAR(30)  NOT NULL
                             CHECK (asset_type IN ('stock','bond','etf','mutual_fund','crypto','real_estate_fund','commodity')),
    ticker_symbol        VARCHAR(20),
    asset_name           VARCHAR(120) NOT NULL,
    quantity             NUMERIC(18,8) NOT NULL DEFAULT 0,
    avg_buy_price        NUMERIC(15,4),
    current_price        NUMERIC(15,4),
    current_value        NUMERIC(15,2),
    unrealized_gain_loss NUMERIC(15,2),
    purchase_date        DATE,
    last_updated         TIMESTAMP
);

CREATE TABLE investment_transactions (
    txn_id         SERIAL PRIMARY KEY,
    investment_id  INT  NOT NULL REFERENCES investments(investment_id) ON DELETE CASCADE,
    txn_type       VARCHAR(20) NOT NULL
                       CHECK (txn_type IN ('buy','sell','dividend','split','fee')),
    quantity       NUMERIC(18,8),
    price_per_unit NUMERIC(15,4),
    total_amount   NUMERIC(15,2) NOT NULL,
    fee            NUMERIC(15,2) NOT NULL DEFAULT 0,
    date           DATE          NOT NULL,
    notes          TEXT
);

-- ---------------------------------------------------------------------------
-- INSURANCE
-- ---------------------------------------------------------------------------
CREATE TABLE insurance_companies (
    company_id SERIAL PRIMARY KEY,
    name       VARCHAR(120) NOT NULL,
    country    VARCHAR(80),
    phone      VARCHAR(30),
    website    VARCHAR(255),
    active     BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE insurance_policies (
    policy_id         SERIAL PRIMARY KEY,
    household_id      INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id         INT  REFERENCES members(member_id) ON DELETE SET NULL,
    company_id        INT  REFERENCES insurance_companies(company_id) ON DELETE SET NULL,
    policy_number     VARCHAR(80),
    policy_type       VARCHAR(30) NOT NULL
                          CHECK (policy_type IN ('life','health','auto','home','disability','travel','pet','other')),
    coverage_amount   NUMERIC(15,2),
    deductible        NUMERIC(15,2),
    premium_amount    NUMERIC(15,2) NOT NULL,
    premium_frequency VARCHAR(20)   NOT NULL DEFAULT 'monthly'
                          CHECK (premium_frequency IN ('monthly','quarterly','annual')),
    start_date        DATE NOT NULL,
    end_date          DATE,
    renewal_date      DATE,
    beneficiary       VARCHAR(120),
    agent_name        VARCHAR(120),
    agent_phone       VARCHAR(30),
    status            VARCHAR(20) NOT NULL DEFAULT 'active'
                          CHECK (status IN ('active','expired','cancelled')),
    notes             TEXT
);

CREATE TABLE insurance_asset_links (
    link_id    SERIAL PRIMARY KEY,
    policy_id  INT  NOT NULL REFERENCES insurance_policies(policy_id) ON DELETE CASCADE,
    asset_type VARCHAR(20) NOT NULL CHECK (asset_type IN ('property','vehicle','other_asset')),
    asset_id   INT  NOT NULL
);

CREATE TABLE insurance_claims (
    claim_id        SERIAL PRIMARY KEY,
    policy_id       INT  NOT NULL REFERENCES insurance_policies(policy_id) ON DELETE CASCADE,
    claim_number    VARCHAR(80),
    claim_date      DATE NOT NULL,
    incident_date   DATE,
    description     TEXT,
    claimed_amount  NUMERIC(15,2),
    approved_amount NUMERIC(15,2),
    status          VARCHAR(20) NOT NULL DEFAULT 'submitted'
                        CHECK (status IN ('submitted','under_review','approved','rejected','paid')),
    resolution_date DATE,
    notes           TEXT
);

-- ---------------------------------------------------------------------------
-- SAVINGS GOALS
-- ---------------------------------------------------------------------------
CREATE TABLE savings_goals (
    goal_id         SERIAL PRIMARY KEY,
    household_id    INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    name            VARCHAR(120) NOT NULL,
    description     TEXT,
    target_amount   NUMERIC(15,2) NOT NULL,
    current_amount  NUMERIC(15,2) NOT NULL DEFAULT 0,
    bank_account_id INT  REFERENCES bank_accounts(account_id) ON DELETE SET NULL,
    deadline        DATE,
    priority        VARCHAR(10) NOT NULL DEFAULT 'medium'
                        CHECK (priority IN ('high','medium','low')),
    status          VARCHAR(20) NOT NULL DEFAULT 'active'
                        CHECK (status IN ('active','completed','cancelled')),
    icon            VARCHAR(60),
    color           CHAR(7),
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE savings_contributions (
    contribution_id SERIAL PRIMARY KEY,
    goal_id         INT  NOT NULL REFERENCES savings_goals(goal_id) ON DELETE CASCADE,
    member_id       INT  REFERENCES members(member_id) ON DELETE SET NULL,
    amount          NUMERIC(15,2) NOT NULL,
    date            DATE          NOT NULL,
    notes           TEXT
);

-- ---------------------------------------------------------------------------
-- RECURRING ITEMS
-- ---------------------------------------------------------------------------
CREATE TABLE recurring_items (
    item_id           SERIAL PRIMARY KEY,
    household_id      INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    item_type         VARCHAR(20) NOT NULL CHECK (item_type IN ('expense','income','transfer')),
    name              VARCHAR(120) NOT NULL,
    amount            NUMERIC(15,2) NOT NULL,
    category_id       INT,
    payment_method_id INT  REFERENCES payment_methods(method_id) ON DELETE SET NULL,
    frequency         VARCHAR(20)  NOT NULL
                          CHECK (frequency IN ('daily','weekly','biweekly','monthly','annual')),
    start_date        DATE NOT NULL,
    end_date          DATE,
    next_due_date     DATE,
    last_generated    DATE,
    active            BOOLEAN NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- DEBTS
-- ---------------------------------------------------------------------------
CREATE TABLE debts (
    debt_id             SERIAL PRIMARY KEY,
    household_id        INT  NOT NULL REFERENCES households(household_id) ON DELETE CASCADE,
    member_id           INT  REFERENCES members(member_id) ON DELETE SET NULL,
    creditor_name       VARCHAR(120) NOT NULL,
    debt_type           VARCHAR(30)  NOT NULL
                            CHECK (debt_type IN ('personal_loan','student_loan','credit_card','medical','other')),
    original_amount     NUMERIC(15,2) NOT NULL,
    outstanding_balance NUMERIC(15,2) NOT NULL,
    interest_rate       NUMERIC(6,4),
    monthly_payment     NUMERIC(15,2),
    start_date          DATE,
    due_date            DATE,
    status              VARCHAR(20) NOT NULL DEFAULT 'active'
                            CHECK (status IN ('active','paid','defaulted')),
    notes               TEXT
);

CREATE TABLE debt_payments (
    payment_id        SERIAL PRIMARY KEY,
    debt_id           INT  NOT NULL REFERENCES debts(debt_id) ON DELETE CASCADE,
    amount_paid       NUMERIC(15,2) NOT NULL,
    principal_paid    NUMERIC(15,2),
    interest_paid     NUMERIC(15,2),
    payment_date      DATE          NOT NULL,
    remaining_balance NUMERIC(15,2) NOT NULL
);

-- ---------------------------------------------------------------------------
-- INDEXES
-- ---------------------------------------------------------------------------
CREATE INDEX idx_user_role_user       ON user_role(user_id);
CREATE INDEX idx_user_role_role       ON user_role(role_id);
CREATE INDEX idx_role_permission_role ON role_permission(role_id);
CREATE INDEX idx_audit_logs_user      ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_date      ON audit_logs(created_at);
CREATE INDEX idx_sessions_user        ON sessions(user_id);
CREATE INDEX idx_expenses_household   ON expenses(household_id);
CREATE INDEX idx_expenses_date        ON expenses(date);
CREATE INDEX idx_expenses_category    ON expenses(category_id);
CREATE INDEX idx_incomes_member       ON incomes(member_id);
CREATE INDEX idx_incomes_date         ON incomes(date);
CREATE INDEX idx_budgets_household    ON budgets(household_id, year, month);
CREATE INDEX idx_properties_household ON properties(household_id);
CREATE INDEX idx_vehicles_household   ON vehicles(household_id);
CREATE INDEX idx_investments_account  ON investments(account_id);
CREATE INDEX idx_policies_household   ON insurance_policies(household_id);
CREATE INDEX idx_debts_household      ON debts(household_id);


-- =============================================================================
-- PART 2: SAMPLE DATA
-- =============================================================================

-- Users
INSERT INTO users (full_name, email, password_hash, phone, status) VALUES
('Carlos Mendoza',   'carlos@family.com',  'hashed_pw_1', '+1-555-0101', 'active'),
('Maria Mendoza',    'maria@family.com',   'hashed_pw_2', '+1-555-0102', 'active'),
('Luis Mendoza',     'luis@family.com',    'hashed_pw_3', '+1-555-0103', 'active'),
('Sofia Mendoza',    'sofia@family.com',   'hashed_pw_4', '+1-555-0104', 'active');

-- Roles
INSERT INTO roles (name, description, is_system_role) VALUES
('admin',      'Full access to all modules',          TRUE),
('owner',      'Household owner, manage members',     TRUE),
('member',     'Can view and add own expenses',        TRUE),
('viewer',     'Read-only access',                    TRUE),
('accountant', 'Can manage budgets and reports',      FALSE);

-- Permissions
INSERT INTO permissions (code, name, module) VALUES
-- Security
('user:read',                  'View Users',                         'security'),
('user:manage',                'Manage Users',                       'security'),
('role:read',                  'View Roles',                         'security'),
('role:manage',                'Manage Roles',                       'security'),
('permission:read',            'View Permissions',                   'security'),
('permission:manage',          'Manage Permissions',                 'security'),
('session:read',               'View Sessions',                      'security'),
('session:manage',             'Manage Sessions',                    'security'),
('audit:read',                 'View Audit Logs',                    'security'),
-- Household
('household:read',             'View Households',                    'household'),
('household:write',            'Manage Households',                  'household'),
('member:read',                'View Members',                       'household'),
('member:write',               'Manage Members',                     'household'),
-- Banking and payments
('bank:read',                  'View Banks',                         'banking'),
('bank:write',                 'Manage Banks',                       'banking'),
('account:read',               'View Bank Accounts',                 'banking'),
('account:write',              'Manage Bank Accounts',               'banking'),
('card:read',                  'View Cards',                         'banking'),
('card:write',                 'Manage Cards',                       'banking'),
('statement:read',             'View Card Statements',               'banking'),
('statement:write',            'Manage Card Statements',             'banking'),
('payment_method:read',        'View Payment Methods',               'banking'),
('payment_method:write',       'Manage Payment Methods',             'banking'),
('transfer:read',              'View Transfers',                     'banking'),
('transfer:write',             'Manage Transfers',                   'banking'),
-- Income and expenses
('income_category:read',       'View Income Categories',             'income'),
('income_category:write',      'Manage Income Categories',           'income'),
('income:read',                'View Income',                        'income'),
('income:write',               'Add/Update Income',                  'income'),
('expense_category:read',      'View Expense Categories',            'expense'),
('expense_category:write',     'Manage Expense Categories',          'expense'),
('expense_subcategory:read',   'View Expense Subcategories',         'expense'),
('expense_subcategory:write',  'Manage Expense Subcategories',       'expense'),
('expense:read',               'View Expenses',                      'expense'),
('expense:write',              'Add/Update Expenses',                'expense'),
('expense:delete',             'Delete Expenses',                    'expense'),
('recurring:read',             'View Recurring Items',               'expense'),
('recurring:write',            'Manage Recurring Items',             'expense'),
('budget:read',                'View Budgets',                       'budget'),
('budget:write',               'Edit Budgets',                       'budget'),
('budget_alert:read',          'View Budget Alerts',                 'budget'),
('budget_alert:write',         'Manage Budget Alerts',               'budget'),
-- Assets and liabilities
('asset:read',                 'View Other Assets',                  'asset'),
('asset:write',                'Manage Other Assets',                'asset'),
('property:read',              'View Properties',                    'asset'),
('property:write',             'Manage Properties',                  'asset'),
('mortgage:read',              'View Mortgages',                     'asset'),
('mortgage:write',             'Manage Mortgages',                   'asset'),
('vehicle:read',               'View Vehicles',                      'asset'),
('vehicle:write',              'Manage Vehicles',                    'asset'),
('vehicle_loan:read',          'View Vehicle Loans',                 'asset'),
('vehicle_loan:write',         'Manage Vehicle Loans',               'asset'),
('insurance_company:read',     'View Insurance Companies',           'asset'),
('insurance_company:write',    'Manage Insurance Companies',         'asset'),
('insurance_policy:read',      'View Insurance Policies',            'asset'),
('insurance_policy:write',     'Manage Insurance Policies',          'asset'),
('insurance_claim:read',       'View Insurance Claims',              'asset'),
('insurance_claim:write',      'Manage Insurance Claims',            'asset'),
('investment_account:read',    'View Investment Accounts',           'investment'),
('investment_account:write',   'Manage Investment Accounts',         'investment'),
('investment:read',            'View Investments',                   'investment'),
('investment:write',           'Manage Investments',                 'investment'),
('savings_goal:read',          'View Savings Goals',                 'savings'),
('savings_goal:write',         'Manage Savings Goals',               'savings'),
('debt:read',                  'View Debts',                         'debt'),
('debt:write',                 'Manage Debts',                       'debt'),
-- Reporting
('report:read',                'View Reports',                       'report');

-- Role permissions (admin gets all)
INSERT INTO role_permission (role_id, permission_id)
SELECT 1, permission_id FROM permissions;

-- Owner gets most permissions
INSERT INTO role_permission (role_id, permission_id)
SELECT 2, permission_id
FROM permissions
WHERE code NOT IN ('user:manage','role:manage','permission:manage','session:manage');

-- Member gets basic permissions
INSERT INTO role_permission (role_id, permission_id)
SELECT 3, permission_id FROM permissions
WHERE code IN ('budget:read','expense:read','expense:write','income:read','report:read');

-- Viewer: read-only
INSERT INTO role_permission (role_id, permission_id)
SELECT 4, permission_id FROM permissions WHERE code LIKE '%:read';

-- Accountant: finance and reporting modules
INSERT INTO role_permission (role_id, permission_id)
SELECT 5, permission_id
FROM permissions
WHERE module IN ('income','expense','budget','banking','investment','asset','savings','debt','report')
  AND code NOT LIKE '%:delete';

-- User roles
INSERT INTO user_role (user_id, role_id, assigned_by) VALUES
(1, 1, 1), -- Carlos = admin
(1, 2, 1), -- Carlos = owner
(2, 3, 1), -- Maria  = member
(3, 3, 1), -- Luis   = member
(4, 4, 1); -- Sofia  = viewer

-- Household
INSERT INTO households (name, currency, country, timezone, subscription_plan) VALUES
('Mendoza Family', 'USD', 'United States', 'America/New_York', 'premium');

-- Members
INSERT INTO members (household_id, user_id, nickname, relationship, date_of_birth) VALUES
(1, 1, 'Carlos',  'head',   '1980-03-15'),
(1, 2, 'Maria',   'spouse', '1983-07-22'),
(1, 3, 'Luis',    'child',  '2008-11-05'),
(1, 4, 'Sofia',   'child',  '2012-04-18');

-- Banks
INSERT INTO banks (name, country, swift_code) VALUES
('Chase Bank',        'United States', 'CHASUS33'),
('Bank of America',   'United States', 'BOFAUS3N'),
('Wells Fargo',       'United States', 'WFBIUS6S'),
('Fidelity',          'United States', 'FIDMUS33'),
('Charles Schwab',    'United States', 'SCHBUS44');

-- Bank Accounts
INSERT INTO bank_accounts (household_id, member_id, bank_id, account_name, account_type, currency, opening_balance, current_balance, opening_date) VALUES
(1, 1, 1, 'Chase Checking',       'checking', 'USD', 5000.00,  8750.50,  '2018-01-15'),
(1, 1, 2, 'BofA Savings',         'savings',  'USD', 10000.00, 24300.00, '2018-01-15'),
(1, 2, 1, 'Chase Joint Checking', 'checking', 'USD', 3000.00,  4120.75,  '2019-06-01'),
(1, 1, 3, 'Wells Fargo Savings',  'savings',  'USD', 0.00,     15000.00, '2020-03-10'),
(1, 1, 4, 'Fidelity 401k',        'pension',  'USD', 0.00,     185000.00,'2010-08-01');

-- Cards
INSERT INTO cards (household_id, member_id, bank_id, card_name, card_type, last_four_digits, brand, credit_limit, current_balance, available_credit, billing_cycle_day, payment_due_day, expiration_month, expiration_year, is_primary) VALUES
(1, 1, 1, 'Chase Sapphire',    'credit', '4521', 'Visa',       15000.00, 2340.50, 12659.50, 1,  25, 9, 2027, TRUE),
(1, 2, 2, 'BofA Cash Rewards', 'credit', '7832', 'Mastercard',  8000.00, 1205.00,  6795.00, 5,  28, 11,2026, FALSE),
(1, 1, 1, 'Chase Debit',       'debit',  '1198', 'Visa',            NULL,    0.00,      NULL, NULL,NULL,  6, 2028, FALSE),
(1, 2, 2, 'BofA Debit',        'debit',  '3341', 'Mastercard',      NULL,    0.00,      NULL, NULL,NULL,  3, 2027, FALSE);

-- Card statements
INSERT INTO card_statements (card_id, period_start, period_end, total_charges, minimum_payment, total_due, due_date, paid_amount, status) VALUES
(1, '2026-01-01', '2026-01-31', 1850.00, 35.00, 1850.00, '2026-02-25', 1850.00, 'paid'),
(1, '2026-02-01', '2026-02-28', 2340.50, 47.00, 2340.50, '2026-03-25', 0.00,    'open'),
(2, '2026-01-05', '2026-02-04', 1205.00, 25.00, 1205.00, '2026-02-28', 500.00,  'partial');

-- Payment methods
INSERT INTO payment_methods (household_id, name, type, bank_account_id, card_id) VALUES
(1, 'Chase Checking',       'transfer',    1, NULL),
(1, 'BofA Savings',         'transfer',    2, NULL),
(1, 'Chase Sapphire Card',  'credit_card', NULL, 1),
(1, 'BofA Cash Rewards',    'credit_card', NULL, 2),
(1, 'Chase Debit Card',     'debit_card',  NULL, 3),
(1, 'Cash',                 'cash',        NULL, NULL);

-- Income categories
INSERT INTO income_categories (household_id, name, icon, color) VALUES
(1, 'Salary',      '💼', '#4CAF50'),
(1, 'Freelance',   '💻', '#2196F3'),
(1, 'Rental',      '🏠', '#FF9800'),
(1, 'Dividends',   '📈', '#9C27B0'),
(1, 'Bonus',       '🎯', '#F44336');

-- Incomes
INSERT INTO incomes (member_id, category_id, bank_account_id, amount, date, description, frequency, is_taxable, net_amount) VALUES
(1, 1, 1, 8500.00, '2026-03-01', 'Monthly salary - Software Engineer', 'monthly', TRUE, 6200.00),
(1, 1, 1, 8500.00, '2026-02-01', 'Monthly salary - Software Engineer', 'monthly', TRUE, 6200.00),
(1, 1, 1, 8500.00, '2026-01-01', 'Monthly salary - Software Engineer', 'monthly', TRUE, 6200.00),
(2, 1, 3, 5200.00, '2026-03-01', 'Monthly salary - Teacher',           'monthly', TRUE, 4100.00),
(2, 1, 3, 5200.00, '2026-02-01', 'Monthly salary - Teacher',           'monthly', TRUE, 4100.00),
(1, 3, 2, 1500.00, '2026-02-15', 'Rental income - apartment',          'monthly', TRUE, 1350.00),
(1, 3, 2, 1500.00, '2026-03-15', 'Rental income - apartment',          'monthly', TRUE, 1350.00),
(1, 5, 1, 3000.00, '2026-01-15', 'Year-end bonus',                     'once',    TRUE, 2400.00),
(1, 2, 1,  850.00, '2026-03-10', 'Freelance project - web dev',        'once',    TRUE,  720.00),
(1, 4, 2,  420.00, '2026-03-05', 'Stock dividends Q1',                 'once',    TRUE,  357.00);

-- Expense categories
INSERT INTO expense_categories (household_id, name, icon, color, is_fixed) VALUES
(1, 'Housing',       '🏠', '#795548', TRUE),
(1, 'Food',          '🛒', '#4CAF50', FALSE),
(1, 'Transport',     '🚗', '#2196F3', FALSE),
(1, 'Health',        '⚕️', '#F44336', FALSE),
(1, 'Education',     '📚', '#9C27B0', FALSE),
(1, 'Entertainment', '🎬', '#FF9800', FALSE),
(1, 'Utilities',     '💡', '#607D8B', TRUE),
(1, 'Insurance',     '🛡️', '#009688', TRUE),
(1, 'Clothing',      '👗', '#E91E63', FALSE),
(1, 'Savings',       '💰', '#FFC107', FALSE),
(1, 'Personal Care', '🧴', '#FF7043', FALSE),
(1, 'Kids',          '🧸', '#3F51B5', FALSE),
(1, 'Pets',          '🐾', '#8D6E63', FALSE),
(1, 'Debt Payment',  '💳', '#455A64', TRUE),
(1, 'Travel',        '✈️', '#00ACC1', FALSE),
(1, 'Gifts',         '🎁', '#EC407A', FALSE);

-- Expense subcategories
INSERT INTO expense_subcategories (category_id, name) VALUES
(2, 'Supermarket'),
(2, 'Restaurant'),
(2, 'Delivery'),
(3, 'Gas'),
(3, 'Uber/Lyft'),
(3, 'Parking'),
(4, 'Doctor'),
(4, 'Pharmacy'),
(4, 'Gym'),
(6, 'Streaming'),
(6, 'Movies'),
(6, 'Travel'),
(1, 'Rent'),
(1, 'Mortgage'),
(1, 'Maintenance'),
(7, 'Electricity'),
(7, 'Water'),
(7, 'Internet'),
(8, 'Health Insurance'),
(8, 'Car Insurance'),
(8, 'Home Insurance'),
(9, 'Shoes'),
(9, 'Accessories'),
(10, 'Emergency Fund'),
(10, 'Retirement'),
(11, 'Haircut'),
(11, 'Skincare'),
(11, 'Toiletries'),
(12, 'School Supplies'),
(12, 'Daycare'),
(12, 'Extracurricular'),
(13, 'Pet Food'),
(13, 'Vet'),
(13, 'Pet Grooming'),
(14, 'Credit Card'),
(14, 'Student Loan'),
(14, 'Car Loan'),
(15, 'Flights'),
(15, 'Hotels'),
(15, 'Local Transport'),
(16, 'Birthday'),
(16, 'Holiday Gifts'),
(16, 'Donations');

-- Expenses (3 months of data)
INSERT INTO expenses (household_id, member_id, category_id, subcategory_id, payment_method_id, amount, date, description, is_fixed) VALUES
-- January
(1, 1, 1, NULL, 1, 2200.00, '2026-01-01', 'Mortgage payment',       TRUE),
(1, 1, 7, NULL, 1,  185.00, '2026-01-05', 'Electric & Gas bill',    TRUE),
(1, 1, 7, NULL, 1,   89.00, '2026-01-05', 'Internet service',       TRUE),
(1, 2, 2,    1, 5,  520.00, '2026-01-07', 'Costco groceries',       FALSE),
(1, 1, 3,    4, 5,  180.00, '2026-01-10', 'Gas for cars',           FALSE),
(1, 2, 4,    7, 3,  350.00, '2026-01-12', 'Doctor visit + labs',    FALSE),
(1, 2, 2,    2, 3,   95.00, '2026-01-14', 'Dinner anniversary',     FALSE),
(1, 1, 6,   10, 3,   45.00, '2026-01-15', 'Netflix/Spotify/Disney', TRUE),
(1, 3, 5, NULL, 6,  120.00, '2026-01-15', 'School supplies',        FALSE),
(1, 1, 8, NULL, 1,  320.00, '2026-01-20', 'Car insurance',          TRUE),
(1, 2, 2,    3, 3,   68.00, '2026-01-22', 'Uber Eats',              FALSE),
(1, 1, 3,    5, 6,   35.00, '2026-01-25', 'Uber to airport',        FALSE),
(1, 2, 9, NULL, 3,  210.00, '2026-01-28', 'Winter clothing kids',   FALSE),
(1, 2, 11,  26, 3,   35.00, '2026-01-18', 'Haircut and grooming',   FALSE),
(1, 3, 12,  29, 6,   95.00, '2026-01-19', 'School notebooks and art supplies', FALSE),
(1, 1, 13,  32, 3,   65.00, '2026-01-21', 'Dog food monthly pack',  FALSE),
(1, 1, 14,  35, 1,  450.00, '2026-01-26', 'Credit card statement payment', TRUE),
(1, 1, 15,  38, 1,  320.00, '2026-01-27', 'Domestic flight tickets', FALSE),
(1, 2, 16,  41, 3,   80.00, '2026-01-30', 'Birthday gift for niece', FALSE),
-- February
(1, 1, 1, NULL, 1, 2200.00, '2026-02-01', 'Mortgage payment',       TRUE),
(1, 1, 7, NULL, 1,  195.00, '2026-02-05', 'Electric & Gas bill',    TRUE),
(1, 1, 7, NULL, 1,   89.00, '2026-02-05', 'Internet service',       TRUE),
(1, 2, 2,    1, 5,  490.00, '2026-02-08', 'Walmart groceries',      FALSE),
(1, 1, 3,    4, 5,  165.00, '2026-02-10', 'Gas for cars',           FALSE),
(1, 4, 4,    9, 4,   80.00, '2026-02-12', 'Gym monthly fee',        TRUE),
(1, 2, 2,    2, 3,  145.00, '2026-02-14', 'Valentine''s dinner',    FALSE),
(1, 1, 6,   10, 3,   45.00, '2026-02-15', 'Netflix/Spotify/Disney', TRUE),
(1, 1, 8, NULL, 1,  320.00, '2026-02-20', 'Car insurance',          TRUE),
(1, 2, 4,    8, 3,   55.00, '2026-02-22', 'Pharmacy',               FALSE),
(1, 3, 5, NULL, 6,   85.00, '2026-02-25', 'School trip payment',    FALSE),
(1, 1, 6,   11, 3,   48.00, '2026-02-28', 'Cinema family',          FALSE),
(1, 2, 11,  27, 3,   42.00, '2026-02-09', 'Skincare products',      FALSE),
(1, 4, 12,  31, 4,   75.00, '2026-02-16', 'After-school robotics club', FALSE),
(1, 2, 13,  33, 3,  120.00, '2026-02-18', 'Annual vet checkup',     FALSE),
(1, 1, 14,  37, 1,  280.00, '2026-02-24', 'Car loan installment',   TRUE),
(1, 1, 15,  39, 1,  540.00, '2026-02-26', 'Hotel reservation for trip', FALSE),
(1, 1, 16,  43, 2,  100.00, '2026-02-27', 'Donation to local shelter', FALSE),
-- March
(1, 1, 1, NULL, 1, 2200.00, '2026-03-01', 'Mortgage payment',       TRUE),
(1, 1, 7, NULL, 1,  175.00, '2026-03-05', 'Electric & Gas bill',    TRUE),
(1, 1, 7, NULL, 1,   89.00, '2026-03-05', 'Internet service',       TRUE),
(1, 2, 2,    1, 5,  510.00, '2026-03-07', 'Costco groceries',       FALSE),
(1, 1, 3,    4, 5,  170.00, '2026-03-09', 'Gas for cars',           FALSE),
(1, 4, 4,    9, 4,   80.00, '2026-03-12', 'Gym monthly fee',        TRUE),
(1, 1, 6,   10, 3,   45.00, '2026-03-15', 'Netflix/Spotify/Disney', TRUE),
(1, 1, 8, NULL, 1,  320.00, '2026-03-20', 'Car insurance',          TRUE),
(1, 2, 2,    3, 3,   72.00, '2026-03-21', 'DoorDash delivery',      FALSE),
(1, 1, 3,    6, 6,   25.00, '2026-03-22', 'Parking downtown',       FALSE),
(1, 3, 5, NULL, 6,  200.00, '2026-03-25', 'Sports club enrollment', FALSE),
(1, 2, 9, NULL, 3,  155.00, '2026-03-28', 'Spring clothing',        FALSE),
(1, 1, 11,  28, 3,   18.00, '2026-03-08', 'Toiletries refill',      FALSE),
(1, 3, 12,  30, 6,  260.00, '2026-03-11', 'Daycare monthly fee',    TRUE),
(1, 2, 13,  34, 3,   45.00, '2026-03-14', 'Pet grooming service',   FALSE),
(1, 1, 14,  36, 1,  310.00, '2026-03-18', 'Student loan payment',   TRUE),
(1, 1, 15,  40, 6,   70.00, '2026-03-23', 'Taxi and metro during trip', FALSE),
(1, 2, 16,  42, 3,  130.00, '2026-03-29', 'Holiday gifts for family', FALSE);

-- Budgets (March 2026)
INSERT INTO budgets (household_id, category_id, amount_limit, month, year, notes) VALUES
(1, 1, 2300.00, 3, 2026, 'Includes mortgage + HOA'),
(1, 2,  600.00, 3, 2026, 'Groceries + eating out'),
(1, 3,  300.00, 3, 2026, 'Gas, uber, parking'),
(1, 4,  200.00, 3, 2026, 'Medical + gym'),
(1, 5,  250.00, 3, 2026, 'School + activities'),
(1, 6,  150.00, 3, 2026, 'Fun money'),
(1, 7,  300.00, 3, 2026, 'Utilities cap'),
(1, 8,  350.00, 3, 2026, 'All insurance premiums'),
(1, 9,  200.00, 3, 2026, 'Clothing budget'),
(1, 10, 500.00, 3, 2026, 'Monthly savings transfer');

-- Budget alerts
INSERT INTO budget_alerts (budget_id, threshold_percent, channel) VALUES
(1, 80, 'push'), (1, 100, 'email'),
(2, 80, 'push'), (2, 100, 'email'),
(3, 80, 'push'), (3, 100, 'email'),
(6, 50, 'push'), (6, 100, 'email');

-- Mortgages
INSERT INTO mortgages (bank_id, bank_account_id, original_amount, outstanding_balance, interest_rate, rate_type, monthly_payment, start_date, end_date, payment_day) VALUES
(1, 1, 380000.00, 312450.00, 3.75, 'fixed', 2200.00, '2018-03-01', '2048-03-01', 1);

-- Properties
INSERT INTO properties (household_id, name, property_type, address, city, state, country, zip_code, purchase_date, purchase_price, current_value, market_value_updated_at, is_primary_residence, is_rented, mortgage_id) VALUES
(1, 'Primary Home',       'house',     '123 Maple Street',  'Springfield', 'IL', 'USA', '62701', '2018-03-15', 385000.00, 465000.00, '2026-01-01', TRUE,  FALSE, 1),
(1, 'Rental Apartment',   'apartment', '456 Oak Avenue #2B','Chicago',     'IL', 'USA', '60601', '2021-07-01', 195000.00, 228000.00, '2026-01-01', FALSE, TRUE,  NULL);

-- Mortgage payments (last 3 months)
INSERT INTO mortgage_payments (mortgage_id, payment_date, amount_paid, principal_paid, interest_paid, remaining_balance) VALUES
(1, '2026-01-01', 2200.00, 1222.00, 978.00, 314650.00),
(1, '2026-02-01', 2200.00, 1226.00, 974.00, 313424.00),
(1, '2026-03-01', 2200.00, 1230.00, 970.00, 312194.00);

-- Vehicle loans
INSERT INTO vehicle_loans (bank_id, original_amount, outstanding_balance, interest_rate, monthly_payment, start_date, end_date) VALUES
(2, 35000.00, 18450.00, 4.90, 620.00, '2022-06-01', '2027-06-01');

-- Vehicles
INSERT INTO vehicles (household_id, member_id, make, model, year, color, license_plate, vehicle_type, purchase_date, purchase_price, current_value, mileage, fuel_type, is_financed, loan_id) VALUES
(1, 1, 'Toyota',  'Camry',   2022, 'Silver', 'ABC-1234', 'car', '2022-06-15', 35000.00, 26500.00, 42000, 'Gasoline', TRUE,  1),
(1, 2, 'Honda',   'CRV',     2019, 'White',  'XYZ-5678', 'car', '2019-09-20', 28000.00, 19800.00, 68000, 'Gasoline', FALSE, NULL);

-- Vehicle expenses (last 2 months)
INSERT INTO vehicle_expenses (vehicle_id, expense_type, amount, date, mileage_at_service, description) VALUES
(1, 'fuel',        55.00, '2026-03-09', 42100, 'Shell gas station'),
(1, 'fuel',        52.00, '2026-02-10', 41800, 'Shell gas station'),
(2, 'fuel',        48.00, '2026-03-08', 68200, 'BP gas station'),
(2, 'maintenance', 95.00, '2026-02-20', 67800, 'Oil change + tire rotation'),
(1, 'maintenance',180.00, '2026-01-15', 41200, 'Brake pad replacement'),
(2, 'fuel',        46.00, '2026-01-10', 67200, 'Chevron gas station');

-- Other assets
INSERT INTO other_assets (household_id, member_id, name, asset_type, purchase_date, purchase_price, current_value, description, serial_number) VALUES
(1, 1, 'MacBook Pro 16"',      'electronics',  '2024-01-10', 3499.00, 2800.00, 'M3 Max chip',       'SN-MBP-2024-001'),
(1, 2, 'Diamond Ring',         'jewelry',      '2005-06-15', 4500.00, 7200.00, 'Wedding ring 1.2ct',''),
(1, 1, 'Art Collection #1',    'art',          '2022-11-20', 2200.00, 3100.00, 'Local artist piece',''),
(1, 1, 'Sony TV 75"',          'electronics',  '2023-11-25', 1800.00, 1200.00, 'OLED 4K',           'SN-SONY-2023-TV');

-- Investment accounts
INSERT INTO investment_accounts (household_id, member_id, broker_name, account_name, account_type, currency, opening_balance, current_value, opening_date) VALUES
(1, 1, 'Fidelity',       'Carlos 401k',          '401k',      'USD', 80000.00, 185000.00, '2010-08-01'),
(1, 1, 'Charles Schwab', 'Carlos Brokerage',      'brokerage', 'USD', 20000.00,  48750.00, '2019-03-15'),
(1, 2, 'Fidelity',       'Maria Roth IRA',        'roth',      'USD', 5000.00,   22300.00, '2015-02-01');

-- Investments
INSERT INTO investments (account_id, asset_type, ticker_symbol, asset_name, quantity, avg_buy_price, current_price, current_value, unrealized_gain_loss, purchase_date) VALUES
(2, 'stock',      'AAPL',  'Apple Inc.',          25.0,   145.00, 218.50,  5462.50,  1837.50, '2021-05-10'),
(2, 'stock',      'MSFT',  'Microsoft Corp.',     15.0,   280.00, 415.20,  6228.00,  2028.00, '2021-05-10'),
(2, 'etf',        'VOO',   'Vanguard S&P 500',    30.0,   380.00, 518.30, 15549.00,  4149.00, '2020-03-20'),
(2, 'etf',        'QQQ',   'Invesco Nasdaq',      20.0,   310.00, 485.75,  9715.00,  3515.00, '2020-06-15'),
(2, 'crypto',     'BTC',   'Bitcoin',              0.25, 28000.00,82500.00,20625.00, 13625.00, '2023-01-05'),
(3, 'etf',        'VTI',   'Vanguard Total Mkt',  40.0,   190.00, 278.50, 11140.00,  3540.00, '2019-02-01'),
(3, 'mutual_fund','FXAIX', 'Fidelity 500 Index',  22.5,   130.00, 204.30,  4596.75,  1671.75, '2019-02-01');

-- Investment transactions
INSERT INTO investment_transactions (investment_id, txn_type, quantity, price_per_unit, total_amount, fee, date) VALUES
(1, 'buy',      25.0, 145.00, 3625.00, 0.00, '2021-05-10'),
(2, 'buy',      15.0, 280.00, 4200.00, 0.00, '2021-05-10'),
(3, 'buy',      30.0, 380.00,11400.00, 0.00, '2020-03-20'),
(4, 'buy',      20.0, 310.00, 6200.00, 0.00, '2020-06-15'),
(5, 'buy',       0.25,28000.00,7000.00,15.00,'2023-01-05'),
(1, 'dividend', NULL,    NULL,   42.50, 0.00, '2026-03-15'),
(2, 'dividend', NULL,    NULL,   37.80, 0.00, '2026-03-15'),
(3, 'dividend', NULL,    NULL,  185.00, 0.00, '2026-03-20');

-- Insurance companies
INSERT INTO insurance_companies (name, country, phone, website) VALUES
('State Farm',       'USA', '1-800-732-5246', 'www.statefarm.com'),
('Blue Cross Shield','USA', '1-800-262-2583', 'www.bcbs.com'),
('Geico',            'USA', '1-800-207-7847', 'www.geico.com');

-- Insurance policies
INSERT INTO insurance_policies (household_id, member_id, company_id, policy_number, policy_type, coverage_amount, deductible, premium_amount, premium_frequency, start_date, renewal_date, beneficiary, status) VALUES
(1, 1, 1, 'SF-LIFE-2023-001',  'life',   500000.00, 0.00,    85.00,  'monthly',   '2023-01-01', '2027-01-01', 'Maria Mendoza',  'active'),
(1, 2, 1, 'SF-LIFE-2023-002',  'life',   300000.00, 0.00,    62.00,  'monthly',   '2023-01-01', '2027-01-01', 'Carlos Mendoza', 'active'),
(1, 1, 2, 'BC-HLTH-2024-001',  'health', 200000.00, 2500.00, 480.00, 'monthly',   '2024-01-01', '2027-01-01', NULL,             'active'),
(1, 1, 3, 'GC-AUTO-2024-001',  'auto',    50000.00, 500.00,  175.00, 'monthly',   '2024-06-01', '2027-06-01', NULL,             'active'),
(1, 1, 1, 'SF-HOME-2022-001',  'home',   465000.00, 1000.00, 145.00, 'monthly',   '2022-03-15', '2027-03-15', NULL,             'active');

-- Link auto insurance to vehicles
INSERT INTO insurance_asset_links (policy_id, asset_type, asset_id) VALUES
(4, 'vehicle',  1),
(4, 'vehicle',  2),
(5, 'property', 1);

-- Insurance claims
INSERT INTO insurance_claims (policy_id, claim_number, claim_date, incident_date, description, claimed_amount, approved_amount, status, resolution_date) VALUES
(4, 'CLM-2025-0445', '2025-08-15', '2025-08-14', 'Minor fender bender - parking lot', 1850.00, 1350.00, 'paid',         '2025-09-01'),
(3, 'CLM-2025-0821', '2025-11-20', '2025-11-18', 'Emergency room visit',              3200.00, 2100.00, 'paid',         '2025-12-10'),
(5, 'CLM-2026-0102', '2026-01-10', '2026-01-08', 'Water damage - bathroom leak',      4500.00, 3800.00, 'under_review', NULL);

-- Savings goals
INSERT INTO savings_goals (household_id, name, description, target_amount, current_amount, bank_account_id, deadline, priority, status) VALUES
(1, 'Emergency Fund',     '6 months of expenses',        25000.00, 15000.00, 4, '2026-12-31', 'high',   'active'),
(1, 'Family Vacation',    'Summer trip to Europe 2027',  12000.00,  3400.00, 2, '2027-06-01', 'medium', 'active'),
(1, 'New Car Fund',       'Replace Maria car 2028',      30000.00,  8200.00, 4, '2028-01-01', 'medium', 'active'),
(1, 'Kids College Fund',  'Education fund Luis & Sofia', 80000.00, 22000.00, 2, '2030-09-01', 'high',   'active'),
(1, 'Home Renovation',    'Kitchen and bathrooms',       15000.00, 15000.00, 4, '2025-12-01', 'low',    'completed');

-- Savings contributions
INSERT INTO savings_contributions (goal_id, member_id, amount, date, notes) VALUES
(1, 1, 500.00, '2026-01-15', 'Monthly transfer'),
(1, 1, 500.00, '2026-02-15', 'Monthly transfer'),
(1, 1, 500.00, '2026-03-15', 'Monthly transfer'),
(2, 1, 300.00, '2026-01-15', 'Vacation savings'),
(2, 2, 200.00, '2026-01-20', 'Maria contribution'),
(2, 1, 300.00, '2026-02-15', 'Vacation savings'),
(2, 2, 200.00, '2026-02-20', 'Maria contribution'),
(3, 1, 400.00, '2026-01-15', 'Car fund monthly'),
(3, 1, 400.00, '2026-02-15', 'Car fund monthly'),
(4, 1, 600.00, '2026-01-01', 'College fund'),
(4, 2, 400.00, '2026-01-01', 'College fund Maria'),
(4, 1, 600.00, '2026-02-01', 'College fund'),
(4, 2, 400.00, '2026-02-01', 'College fund Maria');

-- Debts
INSERT INTO debts (household_id, member_id, creditor_name, debt_type, original_amount, outstanding_balance, interest_rate, monthly_payment, start_date, due_date, status) VALUES
(1, 3, 'Sallie Mae',     'student_loan', 28000.00, 18500.00, 5.05, 295.00, '2026-09-01', '2034-09-01', 'active'),
(1, 1, 'Chase Card',     'credit_card',   3200.00,  2340.50, 19.99, 100.00, '2024-06-01', '2026-12-01', 'active'),
(1, 2, 'BofA Card',      'credit_card',   2000.00,  1205.00, 17.99,  65.00, '2024-08-01', '2026-12-01', 'active');

-- Debt payments
INSERT INTO debt_payments (debt_id, amount_paid, principal_paid, interest_paid, payment_date, remaining_balance) VALUES
(1, 295.00, 218.00, 77.00, '2026-01-15', 18718.00),
(1, 295.00, 219.00, 76.00, '2026-02-15', 18499.00),
(2, 100.00,  63.00, 37.00, '2026-01-25', 2277.00),
(2, 100.00,  64.00, 36.00, '2026-02-25', 2213.00),
(3,  65.00,  47.00, 18.00, '2026-01-28', 1158.00),
(3,  65.00,  48.00, 17.00, '2026-02-28', 1110.00);

-- Transfers
INSERT INTO transfers (household_id, from_account_id, to_account_id, amount, date, description, status) VALUES
(1, 1, 2,  500.00, '2026-01-15', 'Transfer to savings',         'completed'),
(1, 1, 4, 1000.00, '2026-01-15', 'Transfer to emergency fund',  'completed'),
(1, 1, 2,  500.00, '2026-02-15', 'Transfer to savings',         'completed'),
(1, 1, 4, 1000.00, '2026-02-15', 'Transfer to emergency fund',  'completed'),
(1, 1, 2,  500.00, '2026-03-15', 'Transfer to savings',         'completed');


-- =============================================================================
-- PART 3: VIEWS
-- =============================================================================

-- ---------------------------------------------------------------------------
-- VIEW 1: Available balance per bank account
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_account_balance AS
SELECT
    ba.account_id,
    ba.account_name,
    ba.account_type,
    b.name                                          AS bank_name,
    m.nickname                                      AS member_name,
    h.name                                          AS household_name,
    ba.currency,
    ba.current_balance,
    COALESCE(out_.total_out, 0)                     AS total_transferred_out,
    COALESCE(in_.total_in,  0)                      AS total_transferred_in,
    ba.current_balance
        + COALESCE(in_.total_in,  0)
        - COALESCE(out_.total_out, 0)               AS available_balance,
    ba.interest_rate
FROM bank_accounts ba
LEFT JOIN banks     b  ON b.bank_id     = ba.bank_id
LEFT JOIN members   m  ON m.member_id   = ba.member_id
LEFT JOIN households h ON h.household_id= ba.household_id
LEFT JOIN (
    SELECT to_account_id, SUM(amount) AS total_in
    FROM transfers WHERE status = 'completed'
    GROUP BY to_account_id
) in_ ON in_.to_account_id = ba.account_id
LEFT JOIN (
    SELECT from_account_id, SUM(amount) AS total_out
    FROM transfers WHERE status = 'completed'
    GROUP BY from_account_id
) out_ ON out_.from_account_id = ba.account_id
WHERE ba.active = TRUE;

-- ---------------------------------------------------------------------------
-- VIEW 2: Budget vs. actual spending (current month)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_budget_vs_actual AS
SELECT
    b.budget_id,
    b.month,
    b.year,
    h.name                                          AS household_name,
    ec.name                                         AS category_name,
    ec.icon,
    ec.color,
    b.amount_limit                                  AS budget_limit,
    COALESCE(SUM(e.amount), 0)                      AS actual_spent,
    b.amount_limit - COALESCE(SUM(e.amount), 0)     AS remaining,
    ROUND(
        COALESCE(SUM(e.amount), 0) * 100.0
        / NULLIF(b.amount_limit, 0), 2
    )                                               AS used_percent,
    CASE
        WHEN COALESCE(SUM(e.amount), 0) >= b.amount_limit THEN 'over_budget'
        WHEN COALESCE(SUM(e.amount), 0) >= b.amount_limit * 0.80 THEN 'warning'
        ELSE 'on_track'
    END                                             AS status
FROM budgets b
JOIN households h         ON h.household_id = b.household_id
JOIN expense_categories ec ON ec.category_id = b.category_id
LEFT JOIN expenses e
    ON  e.category_id   = b.category_id
    AND e.household_id  = b.household_id
    AND EXTRACT(MONTH FROM e.date) = b.month
    AND EXTRACT(YEAR  FROM e.date) = b.year
GROUP BY b.budget_id, b.month, b.year, h.name, ec.name, ec.icon, ec.color, b.amount_limit;

-- ---------------------------------------------------------------------------
-- VIEW 3: Savings goal progress
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_savings_goal_progress AS
SELECT
    sg.goal_id,
    sg.name                                         AS goal_name,
    sg.description,
    sg.priority,
    sg.status,
    sg.target_amount,
    sg.current_amount,
    sg.target_amount - sg.current_amount            AS remaining_amount,
    ROUND(sg.current_amount * 100.0
          / NULLIF(sg.target_amount, 0), 2)         AS progress_percent,
    sg.deadline,
    DATE_PART('day', sg.deadline::timestamp
              - NOW())::INT                         AS days_remaining,
    CASE
        WHEN sg.current_amount >= sg.target_amount    THEN 'completed'
        WHEN sg.deadline < NOW()::date                THEN 'overdue'
        WHEN DATE_PART('day', sg.deadline::timestamp
                       - NOW()) < 30                 THEN 'urgent'
        ELSE 'on_track'
    END                                             AS health_status,
    COALESCE(c.total_contributions, 0)              AS total_contributions,
    COALESCE(c.contributions_count, 0)              AS contributions_count,
    ba.account_name                                 AS linked_account
FROM savings_goals sg
LEFT JOIN bank_accounts ba ON ba.account_id = sg.bank_account_id
LEFT JOIN (
    SELECT goal_id,
           SUM(amount) AS total_contributions,
           COUNT(*)    AS contributions_count
    FROM savings_contributions
    GROUP BY goal_id
) c ON c.goal_id = sg.goal_id;

-- ---------------------------------------------------------------------------
-- VIEW 4: Debt & investment summary
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_debt_investment_summary AS
WITH debt_summary AS (
    SELECT
        d.household_id,
        COUNT(*)                 AS total_debts,
        SUM(d.outstanding_balance) AS total_debt_balance,
        SUM(d.monthly_payment)   AS total_monthly_payments,
        SUM(d.original_amount)   AS total_original_debt
    FROM debts d
    WHERE d.status = 'active'
    GROUP BY d.household_id
),
investment_summary AS (
    SELECT
        ia.household_id,
        COUNT(DISTINCT ia.account_id) AS investment_accounts,
        SUM(ia.current_value)         AS total_investment_value,
        SUM(i.unrealized_gain_loss)   AS total_unrealized_gains
    FROM investment_accounts ia
    LEFT JOIN investments i ON i.account_id = ia.account_id
    WHERE ia.active = TRUE
    GROUP BY ia.household_id
),
mortgage_summary AS (
    SELECT
        p.household_id,
        SUM(mg.outstanding_balance)  AS total_mortgage_balance,
        SUM(mg.monthly_payment)      AS total_mortgage_payments
    FROM properties p
    JOIN mortgages mg ON mg.mortgage_id = p.mortgage_id
    WHERE mg.status = 'active'
    GROUP BY p.household_id
)
SELECT
    h.household_id,
    h.name                                              AS household_name,
    COALESCE(ds.total_debt_balance,       0)            AS total_consumer_debt,
    COALESCE(ms.total_mortgage_balance,   0)            AS total_mortgage_debt,
    COALESCE(ds.total_debt_balance, 0)
        + COALESCE(ms.total_mortgage_balance, 0)        AS total_debt,
    COALESCE(inv.total_investment_value,  0)            AS total_investments,
    COALESCE(inv.total_unrealized_gains,  0)            AS total_unrealized_gains,
    COALESCE(inv.total_investment_value, 0)
        - COALESCE(ds.total_debt_balance, 0)
        - COALESCE(ms.total_mortgage_balance, 0)        AS net_investment_position,
    COALESCE(ds.total_monthly_payments,   0)
        + COALESCE(ms.total_mortgage_payments, 0)       AS total_monthly_debt_service
FROM households h
LEFT JOIN debt_summary       ds  ON ds.household_id  = h.household_id
LEFT JOIN investment_summary inv ON inv.household_id = h.household_id
LEFT JOIN mortgage_summary   ms  ON ms.household_id  = h.household_id;

-- ---------------------------------------------------------------------------
-- VIEW 5: Expenses by category and member
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_expenses_by_category_member AS
SELECT
    EXTRACT(YEAR  FROM e.date)::INT  AS year,
    EXTRACT(MONTH FROM e.date)::INT  AS month,
    h.name                           AS household_name,
    m.nickname                       AS member_name,
    ec.name                          AS category_name,
    ec.icon,
    esc.name                         AS subcategory_name,
    COUNT(e.expense_id)              AS transaction_count,
    SUM(e.amount)                    AS total_amount,
    AVG(e.amount)                    AS avg_amount,
    MIN(e.amount)                    AS min_amount,
    MAX(e.amount)                    AS max_amount,
    SUM(CASE WHEN e.is_fixed THEN e.amount ELSE 0 END) AS fixed_expenses,
    SUM(CASE WHEN NOT e.is_fixed THEN e.amount ELSE 0 END) AS variable_expenses
FROM expenses e
JOIN households          h   ON h.household_id  = e.household_id
LEFT JOIN members        m   ON m.member_id     = e.member_id
LEFT JOIN expense_categories  ec  ON ec.category_id  = e.category_id
LEFT JOIN expense_subcategories esc ON esc.subcategory_id = e.subcategory_id
GROUP BY 1, 2, 3, 4, 5, 6, 7;

-- ---------------------------------------------------------------------------
-- VIEW 6: Insurance policy status
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_insurance_status AS
SELECT
    ip.policy_id,
    h.name                                          AS household_name,
    m.nickname                                      AS insured_member,
    ic.name                                         AS insurance_company,
    ip.policy_number,
    ip.policy_type,
    ip.coverage_amount,
    ip.deductible,
    ip.premium_amount,
    ip.premium_frequency,
    CASE ip.premium_frequency
        WHEN 'monthly'    THEN ip.premium_amount * 12
        WHEN 'quarterly'  THEN ip.premium_amount *  4
        WHEN 'annual'     THEN ip.premium_amount
    END                                             AS annual_premium_cost,
    ip.start_date,
    ip.end_date,
    ip.renewal_date,
    DATE_PART('day', ip.renewal_date::timestamp
              - NOW())::INT                         AS days_to_renewal,
    CASE
        WHEN ip.renewal_date <= NOW()::date + 30   THEN 'renew_soon'
        WHEN ip.status = 'expired'                 THEN 'expired'
        WHEN ip.status = 'cancelled'               THEN 'cancelled'
        ELSE 'active'
    END                                             AS alert_status,
    ip.beneficiary,
    ip.status,
    COALESCE(cl.total_claims, 0)                    AS total_claims,
    COALESCE(cl.total_claimed, 0)                   AS total_claimed_amount,
    COALESCE(cl.total_approved, 0)                  AS total_approved_amount
FROM insurance_policies ip
JOIN households          h  ON h.household_id  = ip.household_id
LEFT JOIN members        m  ON m.member_id     = ip.member_id
LEFT JOIN insurance_companies ic ON ic.company_id = ip.company_id
LEFT JOIN (
    SELECT policy_id,
           COUNT(*)              AS total_claims,
           SUM(claimed_amount)   AS total_claimed,
           SUM(approved_amount)  AS total_approved
    FROM insurance_claims
    GROUP BY policy_id
) cl ON cl.policy_id = ip.policy_id;

-- ---------------------------------------------------------------------------
-- VIEW 7: Monthly income vs. expenses summary
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_monthly_cash_flow AS
WITH monthly_income AS (
    SELECT
        m.household_id,
        EXTRACT(YEAR  FROM i.date)::INT AS year,
        EXTRACT(MONTH FROM i.date)::INT AS month,
        SUM(i.amount)      AS gross_income,
        SUM(i.net_amount)  AS net_income
    FROM incomes i
    JOIN members m ON m.member_id = i.member_id
    WHERE i.active = TRUE
    GROUP BY 1, 2, 3
),
monthly_expenses AS (
    SELECT
        household_id,
        EXTRACT(YEAR  FROM date)::INT AS year,
        EXTRACT(MONTH FROM date)::INT AS month,
        SUM(amount)                   AS total_expenses,
        SUM(CASE WHEN is_fixed THEN amount ELSE 0 END) AS fixed_expenses,
        SUM(CASE WHEN NOT is_fixed THEN amount ELSE 0 END) AS variable_expenses
    FROM expenses
    GROUP BY 1, 2, 3
)
SELECT
    h.name                                           AS household_name,
    mi.year,
    mi.month,
    TO_CHAR(TO_DATE(mi.month::text, 'MM'), 'Month') AS month_name,
    COALESCE(mi.gross_income,  0)                    AS gross_income,
    COALESCE(mi.net_income,    0)                    AS net_income,
    COALESCE(me.total_expenses,0)                    AS total_expenses,
    COALESCE(me.fixed_expenses,0)                    AS fixed_expenses,
    COALESCE(me.variable_expenses,0)                 AS variable_expenses,
    COALESCE(mi.net_income, 0) - COALESCE(me.total_expenses, 0) AS net_cash_flow,
    CASE
        WHEN COALESCE(mi.net_income, 0) - COALESCE(me.total_expenses, 0) > 0 THEN 'surplus'
        WHEN COALESCE(mi.net_income, 0) - COALESCE(me.total_expenses, 0) < 0 THEN 'deficit'
        ELSE 'balanced'
    END                                              AS cash_flow_status
FROM monthly_income mi
JOIN households h ON h.household_id = mi.household_id
LEFT JOIN monthly_expenses me
    ON  me.household_id = mi.household_id
    AND me.year  = mi.year
    AND me.month = mi.month
ORDER BY mi.year, mi.month;


-- =============================================================================
-- PART 4: FUNCTIONS / STORED PROCEDURES
-- =============================================================================

-- ---------------------------------------------------------------------------
-- FUNCTION 1: Get net worth for a household
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_get_net_worth(p_household_id INT)
RETURNS TABLE (
    category        TEXT,
    amount          NUMERIC
) LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    WITH assets AS (
        -- Bank accounts
        SELECT 'Bank Accounts'::text AS category, SUM(current_balance) AS amount
        FROM bank_accounts WHERE household_id = p_household_id AND active = TRUE
        UNION ALL
        -- Property values
        SELECT 'Real Estate'::text,      SUM(current_value)
        FROM properties WHERE household_id = p_household_id AND active = TRUE
        UNION ALL
        -- Vehicles
        SELECT 'Vehicles'::text,         SUM(current_value)
        FROM vehicles WHERE household_id = p_household_id AND active = TRUE
        UNION ALL
        -- Investments
        SELECT 'Investments'::text,      SUM(current_value)
        FROM investment_accounts WHERE household_id = p_household_id AND active = TRUE
        UNION ALL
        -- Other assets
        SELECT 'Other Assets'::text,     SUM(current_value)
        FROM other_assets WHERE household_id = p_household_id AND active = TRUE
    ),
    liabilities AS (
        -- Mortgages
        SELECT 'Mortgages'::text AS category, -SUM(mg.outstanding_balance) AS amount
        FROM properties p
        JOIN mortgages mg ON mg.mortgage_id = p.mortgage_id
        WHERE p.household_id = p_household_id AND mg.status = 'active'
        UNION ALL
        -- Vehicle loans
        SELECT 'Vehicle Loans'::text,    -SUM(vl.outstanding_balance)
        FROM vehicles v
        JOIN vehicle_loans vl ON vl.loan_id = v.loan_id
        WHERE v.household_id = p_household_id AND vl.status = 'active'
        UNION ALL
        -- Other debts
        SELECT 'Other Debts'::text,      -SUM(outstanding_balance)
        FROM debts WHERE household_id = p_household_id AND status = 'active'
        UNION ALL
        -- Credit card balances
        SELECT 'Credit Cards'::text,     -SUM(current_balance)
        FROM cards WHERE household_id = p_household_id AND card_type = 'credit' AND active = TRUE
    )
    SELECT category, amount FROM assets  WHERE amount IS NOT NULL
    UNION ALL
    SELECT category, amount FROM liabilities WHERE amount IS NOT NULL
    UNION ALL
    SELECT 'NET WORTH', (
        SELECT COALESCE(a.v, 0) + COALESCE(l.v, 0)
        FROM (SELECT SUM(current_balance) AS v FROM bank_accounts WHERE household_id = p_household_id AND active = TRUE) a
        CROSS JOIN
             (SELECT -SUM(outstanding_balance) AS v FROM debts WHERE household_id = p_household_id AND status = 'active') l
    );
END;
$$;

-- ---------------------------------------------------------------------------
-- FUNCTION 2: Add expense and check budget alert
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_add_expense(
    p_household_id      INT,
    p_member_id         INT,
    p_category_id       INT,
    p_subcategory_id    INT,
    p_payment_method_id INT,
    p_amount            NUMERIC,
    p_date              DATE,
    p_description       VARCHAR,
    p_is_fixed          BOOLEAN DEFAULT FALSE
)
RETURNS JSONB LANGUAGE plpgsql AS $$
DECLARE
    v_expense_id    INT;
    v_budget        RECORD;
    v_actual        NUMERIC;
    v_used_pct      NUMERIC;
    v_alert         TEXT := NULL;
BEGIN
    -- Insert expense
    INSERT INTO expenses (
        household_id, member_id, category_id, subcategory_id,
        payment_method_id, amount, date, description, is_fixed
    )
    VALUES (
        p_household_id, p_member_id, p_category_id, p_subcategory_id,
        p_payment_method_id, p_amount, p_date, p_description, p_is_fixed
    )
    RETURNING expense_id INTO v_expense_id;

    -- Check budget
    SELECT * INTO v_budget
    FROM budgets
    WHERE household_id = p_household_id
      AND category_id  = p_category_id
      AND month = EXTRACT(MONTH FROM p_date)::SMALLINT
      AND year  = EXTRACT(YEAR  FROM p_date)::SMALLINT
    LIMIT 1;

    IF FOUND THEN
        SELECT COALESCE(SUM(amount), 0) INTO v_actual
        FROM expenses
        WHERE household_id = p_household_id
          AND category_id  = p_category_id
          AND EXTRACT(MONTH FROM date) = EXTRACT(MONTH FROM p_date)
          AND EXTRACT(YEAR  FROM date) = EXTRACT(YEAR  FROM p_date);

        v_used_pct := ROUND(v_actual * 100.0 / NULLIF(v_budget.amount_limit, 0), 2);

        IF v_used_pct >= 100 THEN
            v_alert := 'OVER BUDGET: spent $' || v_actual || ' of $' || v_budget.amount_limit;
        ELSIF v_used_pct >= 80 THEN
            v_alert := 'WARNING: ' || v_used_pct || '% of budget used ($' || v_actual || ' / $' || v_budget.amount_limit || ')';
        END IF;
    END IF;

    RETURN jsonb_build_object(
        'success',     TRUE,
        'expense_id',  v_expense_id,
        'amount',      p_amount,
        'budget_alert',v_alert,
        'used_percent',v_used_pct
    );
END;
$$;

-- ---------------------------------------------------------------------------
-- FUNCTION 3: Add savings contribution and update goal
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_add_savings_contribution(
    p_goal_id   INT,
    p_member_id INT,
    p_amount    NUMERIC,
    p_date      DATE,
    p_notes     TEXT DEFAULT NULL
)
RETURNS JSONB LANGUAGE plpgsql AS $$
DECLARE
    v_goal      RECORD;
    v_new_total NUMERIC;
BEGIN
    SELECT * INTO v_goal FROM savings_goals WHERE goal_id = p_goal_id;
    IF NOT FOUND THEN
        RETURN jsonb_build_object('success', FALSE, 'error', 'Goal not found');
    END IF;

    INSERT INTO savings_contributions (goal_id, member_id, amount, date, notes)
    VALUES (p_goal_id, p_member_id, p_amount, p_date, p_notes);

    v_new_total := v_goal.current_amount + p_amount;

    UPDATE savings_goals
    SET current_amount = v_new_total,
        status = CASE WHEN v_new_total >= target_amount THEN 'completed' ELSE status END
    WHERE goal_id = p_goal_id;

    RETURN jsonb_build_object(
        'success',          TRUE,
        'goal_name',        v_goal.name,
        'previous_amount',  v_goal.current_amount,
        'contribution',     p_amount,
        'new_total',        v_new_total,
        'target',           v_goal.target_amount,
        'progress_percent', ROUND(v_new_total * 100.0 / v_goal.target_amount, 2),
        'completed',        v_new_total >= v_goal.target_amount
    );
END;
$$;

-- ---------------------------------------------------------------------------
-- FUNCTION 4: Monthly expense report
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_monthly_expense_report(
    p_household_id INT,
    p_month        SMALLINT,
    p_year         SMALLINT
)
RETURNS TABLE (
    category_name   TEXT,
    subcategory     TEXT,
    transaction_count BIGINT,
    total_spent     NUMERIC,
    budget_limit    NUMERIC,
    remaining       NUMERIC,
    used_pct        NUMERIC,
    status          TEXT
) LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        ec.name::TEXT,
        COALESCE(esc.name,'—')::TEXT,
        COUNT(e.expense_id),
        COALESCE(SUM(e.amount), 0) AS total_spent,
        b.amount_limit             AS budget_limit,
        b.amount_limit - COALESCE(SUM(e.amount), 0) AS remaining,
        ROUND(COALESCE(SUM(e.amount), 0) * 100.0 / NULLIF(b.amount_limit, 0), 2) AS used_pct,
        CASE
            WHEN COALESCE(SUM(e.amount), 0) >= b.amount_limit         THEN 'over_budget'
            WHEN COALESCE(SUM(e.amount), 0) >= b.amount_limit * 0.80  THEN 'warning'
            ELSE 'on_track'
        END::TEXT AS status
    FROM budgets b
    JOIN expense_categories ec ON ec.category_id = b.category_id
    LEFT JOIN expenses e
        ON  e.category_id  = b.category_id
        AND e.household_id = p_household_id
        AND EXTRACT(MONTH FROM e.date)::SMALLINT = p_month
        AND EXTRACT(YEAR  FROM e.date)::SMALLINT = p_year
    LEFT JOIN expense_subcategories esc ON esc.subcategory_id = e.subcategory_id
    WHERE b.household_id = p_household_id
      AND b.month = p_month
      AND b.year  = p_year
    GROUP BY ec.name, esc.name, b.amount_limit
    ORDER BY 4 DESC;
END;
$$;

-- ---------------------------------------------------------------------------
-- FUNCTION 5: Transfer between accounts
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_transfer_funds(
    p_household_id  INT,
    p_from_account  INT,
    p_to_account    INT,
    p_amount        NUMERIC,
    p_description   VARCHAR DEFAULT 'Transfer'
)
RETURNS JSONB LANGUAGE plpgsql AS $$
DECLARE
    v_from_balance NUMERIC;
BEGIN
    SELECT current_balance INTO v_from_balance
    FROM bank_accounts WHERE account_id = p_from_account;

    IF v_from_balance < p_amount THEN
        RETURN jsonb_build_object(
            'success', FALSE,
            'error',   'Insufficient funds',
            'balance', v_from_balance,
            'requested', p_amount
        );
    END IF;

    UPDATE bank_accounts SET current_balance = current_balance - p_amount
    WHERE account_id = p_from_account;

    UPDATE bank_accounts SET current_balance = current_balance + p_amount
    WHERE account_id = p_to_account;

    INSERT INTO transfers (household_id, from_account_id, to_account_id, amount, date, description, status)
    VALUES (p_household_id, p_from_account, p_to_account, p_amount, NOW()::date, p_description, 'completed');

    RETURN jsonb_build_object(
        'success',     TRUE,
        'transferred', p_amount,
        'from_account',p_from_account,
        'to_account',  p_to_account,
        'new_balance', v_from_balance - p_amount
    );
END;
$$;


-- =============================================================================
-- PART 5: TRIGGERS
-- =============================================================================

-- ---------------------------------------------------------------------------
-- TRIGGER 1: Auto-update bank account balance when expense is added
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_expense_update_balance()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
DECLARE
    v_account_id INT;
BEGIN
    -- Get the bank account linked to the payment method
    SELECT bank_account_id INTO v_account_id
    FROM payment_methods
    WHERE method_id = NEW.payment_method_id
      AND type IN ('transfer','debit_card');

    IF v_account_id IS NOT NULL THEN
        UPDATE bank_accounts
        SET current_balance = current_balance - NEW.amount
        WHERE account_id = v_account_id;
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_expense_update_balance
AFTER INSERT ON expenses
FOR EACH ROW
EXECUTE FUNCTION trg_fn_expense_update_balance();

-- ---------------------------------------------------------------------------
-- TRIGGER 2: Auto-update bank account balance when income is added
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_income_update_balance()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.bank_account_id IS NOT NULL THEN
        UPDATE bank_accounts
        SET current_balance = current_balance + NEW.amount
        WHERE account_id = NEW.bank_account_id;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_income_update_balance
AFTER INSERT ON incomes
FOR EACH ROW
EXECUTE FUNCTION trg_fn_income_update_balance();

-- ---------------------------------------------------------------------------
-- TRIGGER 3: Auto-update savings goal current_amount on new contribution
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_savings_update_goal()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    UPDATE savings_goals
    SET current_amount = current_amount + NEW.amount,
        status = CASE
            WHEN current_amount + NEW.amount >= target_amount THEN 'completed'
            ELSE status
        END
    WHERE goal_id = NEW.goal_id;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_savings_update_goal
AFTER INSERT ON savings_contributions
FOR EACH ROW
EXECUTE FUNCTION trg_fn_savings_update_goal();

-- ---------------------------------------------------------------------------
-- TRIGGER 4: Audit log on sensitive table changes (users)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_audit_users()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO audit_logs (action, module, entity_name, entity_id, old_value, new_value)
    VALUES (
        TG_OP,
        'security',
        'users',
        COALESCE(NEW.user_id, OLD.user_id),
        CASE WHEN TG_OP = 'DELETE' THEN row_to_json(OLD)::jsonb END,
        CASE WHEN TG_OP IN ('INSERT','UPDATE') THEN row_to_json(NEW)::jsonb END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_audit_users
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW
EXECUTE FUNCTION trg_fn_audit_users();

-- ---------------------------------------------------------------------------
-- TRIGGER 5: Prevent negative bank balance on debit payment methods
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_check_balance_before_expense()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
DECLARE
    v_account_id  INT;
    v_balance     NUMERIC;
    v_method_type VARCHAR;
BEGIN
    SELECT type, bank_account_id INTO v_method_type, v_account_id
    FROM payment_methods WHERE method_id = NEW.payment_method_id;

    IF v_method_type IN ('transfer','debit_card') AND v_account_id IS NOT NULL THEN
        SELECT current_balance INTO v_balance
        FROM bank_accounts WHERE account_id = v_account_id;

        IF v_balance < NEW.amount THEN
            RAISE EXCEPTION 'Insufficient funds: balance is % but expense is %',
                            v_balance, NEW.amount;
        END IF;
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_check_balance_before_expense
BEFORE INSERT ON expenses
FOR EACH ROW
EXECUTE FUNCTION trg_fn_check_balance_before_expense();

-- ---------------------------------------------------------------------------
-- TRIGGER 6: Auto-mark budget alert as notified when threshold is reached
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_check_budget_alert()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
DECLARE
    v_budget    RECORD;
    v_actual    NUMERIC;
    v_used_pct  NUMERIC;
    v_alert     RECORD;
BEGIN
    FOR v_budget IN
        SELECT * FROM budgets
        WHERE household_id = NEW.household_id
          AND category_id  = NEW.category_id
          AND month = EXTRACT(MONTH FROM NEW.date)::SMALLINT
          AND year  = EXTRACT(YEAR  FROM NEW.date)::SMALLINT
    LOOP
        SELECT COALESCE(SUM(amount), 0) INTO v_actual
        FROM expenses
        WHERE household_id = NEW.household_id
          AND category_id  = NEW.category_id
          AND EXTRACT(MONTH FROM date) = EXTRACT(MONTH FROM NEW.date)
          AND EXTRACT(YEAR  FROM date) = EXTRACT(YEAR  FROM NEW.date);

        v_used_pct := ROUND(v_actual * 100.0 / NULLIF(v_budget.amount_limit, 0), 2);

        FOR v_alert IN
            SELECT * FROM budget_alerts
            WHERE budget_id = v_budget.budget_id
              AND threshold_percent <= v_used_pct
              AND notified_at IS NULL
        LOOP
            UPDATE budget_alerts
            SET notified_at = NOW()
            WHERE alert_id = v_alert.alert_id;

            RAISE NOTICE 'Budget alert: % - Budget [%] reached %%% used (threshold: %%%)',
                v_alert.channel, v_budget.budget_id, v_used_pct, v_alert.threshold_percent;
        END LOOP;
    END LOOP;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_check_budget_alert
AFTER INSERT ON expenses
FOR EACH ROW
EXECUTE FUNCTION trg_fn_check_budget_alert();


-- =============================================================================
-- PART 6: SAMPLE QUERIES — HOW TO USE
-- =============================================================================

-- Net worth breakdown:
-- SELECT * FROM fn_get_net_worth(1);

-- Monthly cash flow (all months):
-- SELECT * FROM vw_monthly_cash_flow WHERE household_name = 'Mendoza Family';

-- Budget vs. actual for March 2026:
-- SELECT * FROM vw_budget_vs_actual WHERE month = 3 AND year = 2026;

-- Savings goal progress:
-- SELECT goal_name, progress_percent, health_status, days_remaining FROM vw_savings_goal_progress;

-- Insurance policies due for renewal:
-- SELECT policy_type, insurance_company, renewal_date, days_to_renewal, alert_status
-- FROM vw_insurance_status WHERE alert_status = 'renew_soon';

-- Debt & investment summary:
-- SELECT * FROM vw_debt_investment_summary;

-- Expenses by member March 2026:
-- SELECT member_name, category_name, total_amount
-- FROM vw_expenses_by_category_member WHERE month = 3 AND year = 2026
-- ORDER BY total_amount DESC;

-- Add new expense and check budget:
-- SELECT fn_add_expense(1, 1, 2, 1, 5, 85.00, '2026-03-30', 'Weekend groceries');

-- Add savings contribution:
-- SELECT fn_add_savings_contribution(1, 1, 500.00, '2026-03-31', 'End of month savings');

-- Monthly report:
-- SELECT * FROM fn_monthly_expense_report(1, 3, 2026);

-- Transfer funds between accounts:
-- SELECT fn_transfer_funds(1, 1, 2, 1000.00, 'Monthly savings transfer');

-- =============================================================================
-- END OF SCRIPT
-- =============================================================================
