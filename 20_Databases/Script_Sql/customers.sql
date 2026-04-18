PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    city TEXT,
    country TEXT NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1)),
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

INSERT INTO customers (name, email, phone, city, country, is_active, notes) VALUES
    ('Ana Ruiz', 'ana@example.com', '+34 600 111 222', 'Madrid', 'ES', 1, 'Prefers email in Spanish.'),
    ('Ben Carter', 'ben@example.com', '+44 7700 900123', 'London', 'GB', 1, NULL),
    ('Chloe Park', 'chloe@example.com', '+82 10-1234-5678', 'Seoul', 'KR', 1, 'Enterprise tier.'),
    ('Diego Lopez', 'diego@example.com', '+57 300 555 0101', 'Bogota', 'CO', 1, NULL),
    ('Elena Novak', 'elena@example.com', NULL, 'Prague', 'CZ', 0, 'Paused account; follow up Q3.'),
    ('Frank Weber', 'frank@example.com', '+49 151 23456789', 'Berlin', 'DE', 1, 'VAT ID on file.');
