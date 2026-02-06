-- ------------------------------------------------------------
-- File Name: ATM_Database_Schema.sql
-- Author: Florentino Baez
-- Date: February 06, 2026
-- Description: Database schema for ATM Simulation Program
-- Database: MySQL/MariaDB
-- ------------------------------------------------------------

USE python_exercises;

-- ============================================================================
-- TABLAS BASE
-- ============================================================================

-- Tabla: atm_users
-- Descripción: Almacena información de los usuarios del ATM
DROP TABLE IF EXISTS atm_users;

CREATE TABLE atm_users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NULL,
    phone VARCHAR(50) NULL,
    initial_balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    current_balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    is_active BOOLEAN DEFAULT TRUE,
    failed_login_attempts SMALLINT UNSIGNED DEFAULT 0,
    last_login_at TIMESTAMP NULL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_atm_users_username (username),
    INDEX idx_atm_users_active (is_active)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- TABLAS DE TRANSACCIONES
-- ============================================================================

-- Tabla: atm_sessions
-- Descripción: Registra cada sesión de usuario en el ATM
DROP TABLE IF EXISTS atm_sessions;

CREATE TABLE atm_sessions (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user BIGINT UNSIGNED NOT NULL,
    session_token VARCHAR(255) NULL,
    ip_address VARCHAR(45) NULL,
    user_agent VARCHAR(500) NULL,
    login_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    logout_at TIMESTAMP NULL DEFAULT NULL,
    session_duration INT UNSIGNED NULL COMMENT 'Duration in seconds',
    
    CONSTRAINT fk_sessions_user
        FOREIGN KEY (id_user)
        REFERENCES atm_users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    INDEX idx_sessions_user (id_user),
    INDEX idx_sessions_login (login_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: atm_transactions
-- Descripción: Almacena todas las transacciones (depósitos y retiros)
DROP TABLE IF EXISTS atm_transactions;

CREATE TABLE atm_transactions (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user BIGINT UNSIGNED NOT NULL,
    id_session BIGINT UNSIGNED NULL,
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    balance_before DECIMAL(15,2) NOT NULL,
    balance_after DECIMAL(15,2) NOT NULL,
    transaction_status ENUM('completed', 'failed', 'cancelled') DEFAULT 'completed',
    failure_reason VARCHAR(500) NULL,
    notes TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_transactions_user
        FOREIGN KEY (id_user)
        REFERENCES atm_users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_transactions_session
        FOREIGN KEY (id_session)
        REFERENCES atm_sessions(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
        
    INDEX idx_transactions_user (id_user),
    INDEX idx_transactions_type (transaction_type),
    INDEX idx_transactions_date (created_at),
    INDEX idx_transactions_user_date (id_user, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: atm_balance_snapshots
-- Descripción: Guarda instantáneas del balance después de cada transacción
DROP TABLE IF EXISTS atm_balance_snapshots;

CREATE TABLE atm_balance_snapshots (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user BIGINT UNSIGNED NOT NULL,
    id_transaction BIGINT UNSIGNED NOT NULL,
    balance DECIMAL(15,2) NOT NULL,
    snapshot_type ENUM('after_deposit', 'after_withdrawal', 'daily_snapshot', 'manual') DEFAULT 'after_deposit',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_snapshots_user
        FOREIGN KEY (id_user)
        REFERENCES atm_users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_snapshots_transaction
        FOREIGN KEY (id_transaction)
        REFERENCES atm_transactions(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    INDEX idx_snapshots_user (id_user),
    INDEX idx_snapshots_transaction (id_transaction),
    INDEX idx_snapshots_date (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- TABLAS DE AUDITORÍA Y LOGS
-- ============================================================================

-- Tabla: atm_login_attempts
-- Descripción: Registra todos los intentos de login (exitosos y fallidos)
DROP TABLE IF EXISTS atm_login_attempts;

CREATE TABLE atm_login_attempts (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    id_user BIGINT UNSIGNED NULL,
    attempt_status ENUM('success', 'failed', 'blocked') NOT NULL,
    ip_address VARCHAR(45) NULL,
    user_agent VARCHAR(500) NULL,
    failure_reason VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_login_attempts_user
        FOREIGN KEY (id_user)
        REFERENCES atm_users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
        
    INDEX idx_login_attempts_username (username),
    INDEX idx_login_attempts_user (id_user),
    INDEX idx_login_attempts_date (created_at),
    INDEX idx_login_attempts_status (attempt_status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: atm_activity_log
-- Descripción: Log general de actividades del sistema
DROP TABLE IF EXISTS atm_activity_log;

CREATE TABLE atm_activity_log (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user BIGINT UNSIGNED NULL,
    id_session BIGINT UNSIGNED NULL,
    activity_type VARCHAR(100) NOT NULL,
    description TEXT NULL,
    metadata JSON NULL,
    ip_address VARCHAR(45) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_activity_log_user
        FOREIGN KEY (id_user)
        REFERENCES atm_users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_activity_log_session
        FOREIGN KEY (id_session)
        REFERENCES atm_sessions(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
        
    INDEX idx_activity_log_user (id_user),
    INDEX idx_activity_log_type (activity_type),
    INDEX idx_activity_log_date (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- TABLAS DE EXPORTACIÓN DE DATOS
-- ============================================================================

-- Tabla: atm_history_exports
-- Descripción: Registra las exportaciones de historial a archivo
DROP TABLE IF EXISTS atm_history_exports;

CREATE TABLE atm_history_exports (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user BIGINT UNSIGNED NOT NULL,
    id_session BIGINT UNSIGNED NULL,
    filename VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NULL,
    export_type ENUM('full_history', 'deposits_only', 'withdrawals_only', 'balance_only') DEFAULT 'full_history',
    date_from TIMESTAMP NULL,
    date_to TIMESTAMP NULL,
    total_deposits INT UNSIGNED DEFAULT 0,
    total_withdrawals INT UNSIGNED DEFAULT 0,
    total_snapshots INT UNSIGNED DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_exports_user
        FOREIGN KEY (id_user)
        REFERENCES atm_users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_exports_session
        FOREIGN KEY (id_session)
        REFERENCES atm_sessions(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
        
    INDEX idx_exports_user (id_user),
    INDEX idx_exports_date (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- DATOS DE EJEMPLO
-- ============================================================================

-- Usuario de prueba (password: 1234)
-- Nota: En producción, usar bcrypt o argon2 para hashear passwords
INSERT INTO atm_users (username, password_hash, full_name, email, initial_balance, current_balance) VALUES
('test_user', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5ztP.dQNQ/F6i', 'Test User', 'test@example.com', 0.00, 0.00),
('florentino', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5ztP.dQNQ/F6i', 'Florentino Baez', 'florentino@example.com', 1000.00, 1000.00);

-- ============================================================================
-- VISTAS ÚTILES
-- ============================================================================

-- Vista: Resumen de transacciones por usuario
CREATE OR REPLACE VIEW v_user_transaction_summary AS
SELECT 
    u.id AS user_id,
    u.username,
    u.full_name,
    u.current_balance,
    COUNT(t.id) AS total_transactions,
    SUM(CASE WHEN t.transaction_type = 'deposit' THEN 1 ELSE 0 END) AS total_deposits,
    SUM(CASE WHEN t.transaction_type = 'withdrawal' THEN 1 ELSE 0 END) AS total_withdrawals,
    SUM(CASE WHEN t.transaction_type = 'deposit' THEN t.amount ELSE 0 END) AS total_deposited,
    SUM(CASE WHEN t.transaction_type = 'withdrawal' THEN t.amount ELSE 0 END) AS total_withdrawn,
    MAX(t.created_at) AS last_transaction_date
FROM atm_users u
LEFT JOIN atm_transactions t ON u.id = t.id_user
GROUP BY u.id, u.username, u.full_name, u.current_balance;

-- Vista: Historial completo de transacciones
CREATE OR REPLACE VIEW v_transaction_history AS
SELECT 
    t.id,
    t.id_user,
    u.username,
    u.full_name,
    t.transaction_type,
    t.amount,
    t.balance_before,
    t.balance_after,
    t.transaction_status,
    t.created_at,
    s.id AS session_id,
    s.login_at AS session_start
FROM atm_transactions t
INNER JOIN atm_users u ON t.id_user = u.id
LEFT JOIN atm_sessions s ON t.id_session = s.id
ORDER BY t.created_at DESC;

-- Vista: Actividad de login
CREATE OR REPLACE VIEW v_login_activity AS
SELECT 
    la.id,
    la.username,
    u.full_name,
    la.attempt_status,
    la.ip_address,
    la.failure_reason,
    la.created_at
FROM atm_login_attempts la
LEFT JOIN atm_users u ON la.id_user = u.id
ORDER BY la.created_at DESC;

-- ============================================================================
-- PROCEDIMIENTOS ALMACENADOS
-- ============================================================================

-- Procedimiento: Realizar depósito
DELIMITER //

DROP PROCEDURE IF EXISTS sp_make_deposit//

CREATE PROCEDURE sp_make_deposit(
    IN p_user_id BIGINT UNSIGNED,
    IN p_session_id BIGINT UNSIGNED,
    IN p_amount DECIMAL(15,2),
    OUT p_new_balance DECIMAL(15,2),
    OUT p_transaction_id BIGINT UNSIGNED
)
BEGIN
    DECLARE v_current_balance DECIMAL(15,2);
    
    -- Obtener balance actual
    SELECT current_balance INTO v_current_balance
    FROM atm_users
    WHERE id = p_user_id;
    
    -- Insertar transacción
    INSERT INTO atm_transactions (id_user, id_session, transaction_type, amount, balance_before, balance_after)
    VALUES (p_user_id, p_session_id, 'deposit', p_amount, v_current_balance, v_current_balance + p_amount);
    
    SET p_transaction_id = LAST_INSERT_ID();
    
    -- Actualizar balance del usuario
    UPDATE atm_users
    SET current_balance = current_balance + p_amount
    WHERE id = p_user_id;
    
    -- Obtener nuevo balance
    SELECT current_balance INTO p_new_balance
    FROM atm_users
    WHERE id = p_user_id;
    
    -- Crear snapshot
    INSERT INTO atm_balance_snapshots (id_user, id_transaction, balance, snapshot_type)
    VALUES (p_user_id, p_transaction_id, p_new_balance, 'after_deposit');
END//

DELIMITER ;

-- Procedimiento: Realizar retiro
DELIMITER //

DROP PROCEDURE IF EXISTS sp_make_withdrawal//

CREATE PROCEDURE sp_make_withdrawal(
    IN p_user_id BIGINT UNSIGNED,
    IN p_session_id BIGINT UNSIGNED,
    IN p_amount DECIMAL(15,2),
    OUT p_new_balance DECIMAL(15,2),
    OUT p_transaction_id BIGINT UNSIGNED,
    OUT p_success BOOLEAN,
    OUT p_message VARCHAR(255)
)
BEGIN
    DECLARE v_current_balance DECIMAL(15,2);
    
    -- Obtener balance actual
    SELECT current_balance INTO v_current_balance
    FROM atm_users
    WHERE id = p_user_id;
    
    -- Verificar fondos suficientes
    IF v_current_balance < p_amount THEN
        SET p_success = FALSE;
        SET p_message = CONCAT('Insufficient funds. Current balance: $', FORMAT(v_current_balance, 2));
        SET p_new_balance = v_current_balance;
        
        -- Registrar transacción fallida
        INSERT INTO atm_transactions (id_user, id_session, transaction_type, amount, balance_before, balance_after, transaction_status, failure_reason)
        VALUES (p_user_id, p_session_id, 'withdrawal', p_amount, v_current_balance, v_current_balance, 'failed', p_message);
        
        SET p_transaction_id = LAST_INSERT_ID();
    ELSE
        -- Insertar transacción exitosa
        INSERT INTO atm_transactions (id_user, id_session, transaction_type, amount, balance_before, balance_after)
        VALUES (p_user_id, p_session_id, 'withdrawal', p_amount, v_current_balance, v_current_balance - p_amount);
        
        SET p_transaction_id = LAST_INSERT_ID();
        
        -- Actualizar balance del usuario
        UPDATE atm_users
        SET current_balance = current_balance - p_amount
        WHERE id = p_user_id;
        
        -- Obtener nuevo balance
        SELECT current_balance INTO p_new_balance
        FROM atm_users
        WHERE id = p_user_id;
        
        -- Crear snapshot
        INSERT INTO atm_balance_snapshots (id_user, id_transaction, balance, snapshot_type)
        VALUES (p_user_id, p_transaction_id, p_new_balance, 'after_withdrawal');
        
        SET p_success = TRUE;
        SET p_message = 'Withdrawal successful';
    END IF;
END//

DELIMITER ;

-- Procedimiento: Obtener historial de depósitos
DELIMITER //

DROP PROCEDURE IF EXISTS sp_get_deposit_history//

CREATE PROCEDURE sp_get_deposit_history(
    IN p_user_id BIGINT UNSIGNED
)
BEGIN
    SELECT 
        id,
        amount,
        balance_before,
        balance_after,
        created_at,
        transaction_status
    FROM atm_transactions
    WHERE id_user = p_user_id 
        AND transaction_type = 'deposit'
    ORDER BY created_at ASC;
END//

DELIMITER ;

-- Procedimiento: Obtener historial de retiros
DELIMITER //

DROP PROCEDURE IF EXISTS sp_get_withdrawal_history//

CREATE PROCEDURE sp_get_withdrawal_history(
    IN p_user_id BIGINT UNSIGNED
)
BEGIN
    SELECT 
        id,
        amount,
        balance_before,
        balance_after,
        created_at,
        transaction_status,
        failure_reason
    FROM atm_transactions
    WHERE id_user = p_user_id 
        AND transaction_type = 'withdrawal'
    ORDER BY created_at ASC;
END//

DELIMITER ;

-- Procedimiento: Obtener historial de balances
DELIMITER //

DROP PROCEDURE IF EXISTS sp_get_balance_history//

CREATE PROCEDURE sp_get_balance_history(
    IN p_user_id BIGINT UNSIGNED
)
BEGIN
    SELECT 
        bs.id,
        bs.balance,
        bs.snapshot_type,
        bs.created_at,
        t.transaction_type,
        t.amount
    FROM atm_balance_snapshots bs
    INNER JOIN atm_transactions t ON bs.id_transaction = t.id
    WHERE bs.id_user = p_user_id
    ORDER BY bs.created_at ASC;
END//

DELIMITER ;