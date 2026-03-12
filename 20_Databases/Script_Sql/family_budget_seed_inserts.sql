-- =============================================================================
-- FAMILY BUDGET - COMPLEMENTARY SEED INSERTS
-- Fills tables that are not populated in family_budget_complete.sql sample data.
-- Safe to run multiple times (uses WHERE NOT EXISTS guards).
-- =============================================================================

BEGIN;

-- ---------------------------------------------------------------------------
-- 1) user_permission
-- ---------------------------------------------------------------------------
-- Grant explicit permission to Sofia (viewer) for report:read.
INSERT INTO user_permission (user_id, permission_id, granted, granted_by)
SELECT u.user_id, p.permission_id, TRUE, 1
FROM users u
JOIN permissions p ON p.code = 'report:read'
WHERE u.email = 'sofia@family.com'
  AND NOT EXISTS (
      SELECT 1
      FROM user_permission up
      WHERE up.user_id = u.user_id
        AND up.permission_id = p.permission_id
  );

-- ---------------------------------------------------------------------------
-- 2) sessions
-- ---------------------------------------------------------------------------
INSERT INTO sessions (user_id, token_hash, device_info, ip_address, expires_at)
SELECT 1, 'token_carlos_2026_01', 'Chrome on Windows', '192.168.1.10', NOW() + INTERVAL '30 days'
WHERE EXISTS (SELECT 1 FROM users WHERE user_id = 1)
  AND NOT EXISTS (SELECT 1 FROM sessions WHERE token_hash = 'token_carlos_2026_01');

INSERT INTO sessions (user_id, token_hash, device_info, ip_address, expires_at)
SELECT 2, 'token_maria_2026_01', 'Safari on iPhone', '192.168.1.11', NOW() + INTERVAL '30 days'
WHERE EXISTS (SELECT 1 FROM users WHERE user_id = 2)
  AND NOT EXISTS (SELECT 1 FROM sessions WHERE token_hash = 'token_maria_2026_01');

-- ---------------------------------------------------------------------------
-- 3) vehicle_loan_payments
-- ---------------------------------------------------------------------------
INSERT INTO vehicle_loan_payments (
    loan_id, payment_date, amount_paid, principal_paid, interest_paid, remaining_balance
)
SELECT 1, '2026-01-05', 620.00, 445.00, 175.00, 18005.00
WHERE EXISTS (SELECT 1 FROM vehicle_loans WHERE loan_id = 1)
  AND NOT EXISTS (
      SELECT 1
      FROM vehicle_loan_payments
      WHERE loan_id = 1 AND payment_date = '2026-01-05'
  );

INSERT INTO vehicle_loan_payments (
    loan_id, payment_date, amount_paid, principal_paid, interest_paid, remaining_balance
)
SELECT 1, '2026-02-05', 620.00, 448.00, 172.00, 17557.00
WHERE EXISTS (SELECT 1 FROM vehicle_loans WHERE loan_id = 1)
  AND NOT EXISTS (
      SELECT 1
      FROM vehicle_loan_payments
      WHERE loan_id = 1 AND payment_date = '2026-02-05'
  );

-- ---------------------------------------------------------------------------
-- 4) recurring_items
-- ---------------------------------------------------------------------------
-- Monthly mortgage expense.
INSERT INTO recurring_items (
    household_id, item_type, name, amount, category_id, payment_method_id,
    frequency, start_date, next_due_date, active
)
SELECT 1, 'expense', 'Mortgage Payment', 2200.00, 1, 1,
       'monthly', '2026-01-01', '2026-04-01', TRUE
WHERE EXISTS (SELECT 1 FROM households WHERE household_id = 1)
  AND EXISTS (SELECT 1 FROM expense_categories WHERE category_id = 1)
  AND EXISTS (SELECT 1 FROM payment_methods WHERE method_id = 1)
  AND NOT EXISTS (
      SELECT 1
      FROM recurring_items
      WHERE household_id = 1
        AND item_type = 'expense'
        AND name = 'Mortgage Payment'
  );

-- Monthly electric/gas expense.
INSERT INTO recurring_items (
    household_id, item_type, name, amount, category_id, payment_method_id,
    frequency, start_date, next_due_date, active
)
SELECT 1, 'expense', 'Electric and Gas', 185.00, 7, 1,
       'monthly', '2026-01-05', '2026-04-05', TRUE
WHERE EXISTS (SELECT 1 FROM households WHERE household_id = 1)
  AND EXISTS (SELECT 1 FROM expense_categories WHERE category_id = 7)
  AND EXISTS (SELECT 1 FROM payment_methods WHERE method_id = 1)
  AND NOT EXISTS (
      SELECT 1
      FROM recurring_items
      WHERE household_id = 1
        AND item_type = 'expense'
        AND name = 'Electric and Gas'
  );

-- Monthly salary income.
INSERT INTO recurring_items (
    household_id, item_type, name, amount, category_id, payment_method_id,
    frequency, start_date, next_due_date, active
)
SELECT 1, 'income', 'Carlos Monthly Salary', 8500.00, 1, 1,
       'monthly', '2026-01-01', '2026-04-01', TRUE
WHERE EXISTS (SELECT 1 FROM households WHERE household_id = 1)
  AND EXISTS (SELECT 1 FROM income_categories WHERE category_id = 1)
  AND EXISTS (SELECT 1 FROM payment_methods WHERE method_id = 1)
  AND NOT EXISTS (
      SELECT 1
      FROM recurring_items
      WHERE household_id = 1
        AND item_type = 'income'
        AND name = 'Carlos Monthly Salary'
  );

-- ---------------------------------------------------------------------------
-- Optional seed in audit_logs to avoid empty table in first audit.
-- ---------------------------------------------------------------------------
INSERT INTO audit_logs (user_id, action, module, entity_name, entity_id, new_value, ip_address, device)
SELECT NULL, 'SEED_INSERT', 'system', 'seed', 0,
       '{"note":"Initial complementary seed inserts applied"}'::jsonb,
       '127.0.0.1',
       'seed-script'
WHERE NOT EXISTS (
    SELECT 1
    FROM audit_logs
    WHERE action = 'SEED_INSERT'
      AND module = 'system'
      AND entity_name = 'seed'
);

COMMIT;
