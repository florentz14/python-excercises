USE python_exercises;

-- ============================================================================
-- TABLAS BASE (sin dependencias)
-- ============================================================================

-- Tabla: countries (necesaria para owner_company y client_companies)
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_countries_code (code),
    UNIQUE KEY uq_countries_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: currencies
DROP TABLE IF EXISTS currencies;

CREATE TABLE currencies (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    code VARCHAR(3) NOT NULL,
    symbol VARCHAR(5) NOT NULL,
    decimals SMALLINT NOT NULL DEFAULT 2,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_currencies_code (code),
    UNIQUE KEY uq_currencies_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos de ejemplo para currencies
INSERT INTO currencies (name, code, symbol, decimals) VALUES
('Australian Dollar', 'AUD', '$', 2),
('Brazilian Real', 'BRL', 'R$', 2),
('British Pound', 'GBP', '£', 2),
('Canadian Dollar', 'CAD', '$', 2),
('Chinese Yuan', 'CNY', '¥', 2),
('Dominican Peso', 'DOP', 'RD$', 2),
('Euro', 'EUR', '€', 2),
('Japanese Yen', 'JPY', '¥', 0),
('Mexican Peso', 'MXN', '$', 2),
('Swiss Franc', 'CHF', 'Fr', 2),
('United States Dollar', 'USD', '$', 2);

-- Tabla: teams
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: users
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    avatar VARCHAR(255) DEFAULT NULL,
    phone VARCHAR(50) DEFAULT NULL,
    job_title VARCHAR(100) DEFAULT NULL,
    rate INT UNSIGNED DEFAULT NULL,
    google_id VARCHAR(255) DEFAULT NULL,
    remember_token VARCHAR(100) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    archived_at TIMESTAMP NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: permissions
DROP TABLE IF EXISTS permissions;

CREATE TABLE permissions (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    guard_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_permissions_name_guard (name, guard_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: roles
DROP TABLE IF EXISTS roles;

CREATE TABLE roles (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    team_id BIGINT UNSIGNED NULL,
    name VARCHAR(255) NOT NULL,
    guard_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_roles_team_name_guard (team_id, name, guard_name),
    INDEX idx_roles_team (team_id),
    CONSTRAINT fk_roles_team
        FOREIGN KEY (team_id)
        REFERENCES teams(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: labels
DROP TABLE IF EXISTS labels;

CREATE TABLE labels (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    color VARCHAR(50) NOT NULL,
    archived_at TIMESTAMP NULL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- TABLAS CON DEPENDENCIAS DE PRIMER NIVEL
-- ============================================================================

-- Tabla: owner_company
DROP TABLE IF EXISTS owner_company;

CREATE TABLE owner_company (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_country BIGINT UNSIGNED NULL,
    id_currency BIGINT UNSIGNED NULL,
    name VARCHAR(255) NOT NULL,
    logo VARCHAR(255) NULL,
    address VARCHAR(255) NULL,
    postal_code VARCHAR(50) NULL,
    city VARCHAR(100) NULL,
    email VARCHAR(255) NULL,
    phone VARCHAR(50) NULL,
    web VARCHAR(255) NULL,
    iban VARCHAR(100) NULL,
    swift VARCHAR(100) NULL,
    business_id VARCHAR(100) NULL,
    tax_id VARCHAR(100) NULL,
    vat VARCHAR(100) NULL,
    tax SMALLINT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_owner_company_country
        FOREIGN KEY (id_country)
        REFERENCES countries(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT fk_owner_company_currency
        FOREIGN KEY (id_currency)
        REFERENCES currencies(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: client_companies
DROP TABLE IF EXISTS client_companies;

CREATE TABLE client_companies (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_country BIGINT UNSIGNED NULL,
    id_currency BIGINT UNSIGNED NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NULL,
    postal_code VARCHAR(50) NULL,
    city VARCHAR(100) NULL,
    email VARCHAR(255) NULL,
    phone VARCHAR(50) NULL,
    web VARCHAR(255) NULL,
    iban VARCHAR(100) NULL,
    swift VARCHAR(100) NULL,
    business_id VARCHAR(100) NULL,
    tax_id VARCHAR(100) NULL,
    vat VARCHAR(100) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    archived_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_client_companies_country
        FOREIGN KEY (id_country)
        REFERENCES countries(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT fk_client_companies_currency
        FOREIGN KEY (id_currency)
        REFERENCES currencies(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: client_company (relación many-to-many entre users y client_companies)
DROP TABLE IF EXISTS client_company;

CREATE TABLE client_company (
    id_client BIGINT UNSIGNED NOT NULL,
    id_client_company BIGINT UNSIGNED NOT NULL,
    CONSTRAINT pk_client_company PRIMARY KEY (id_client, id_client_company),
    CONSTRAINT fk_client_company_user
        FOREIGN KEY (id_client)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_client_company_company
        FOREIGN KEY (id_client_company)
        REFERENCES client_companies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: invoices
DROP TABLE IF EXISTS invoices;

CREATE TABLE invoices (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_client_company BIGINT UNSIGNED NOT NULL,
    id_user_created_by BIGINT UNSIGNED NOT NULL,
    number VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL,
    note TEXT NULL,
    amount INT UNSIGNED NOT NULL,
    amount_with_tax INT UNSIGNED DEFAULT NULL,
    hourly_rate INT UNSIGNED DEFAULT NULL,
    due_date DATE DEFAULT NULL,
    filename VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP NULL DEFAULT NULL,
    archived_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_invoices_client_company
        FOREIGN KEY (id_client_company)
        REFERENCES client_companies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_invoices_user_created_by
        FOREIGN KEY (id_user_created_by)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: notifications
DROP TABLE IF EXISTS notifications;

CREATE TABLE notifications (
    id CHAR(36) PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    notifiable_type VARCHAR(255) NOT NULL,
    notifiable_id BIGINT UNSIGNED NOT NULL,
    data TEXT NOT NULL,
    read_at TIMESTAMP NULL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_notifications_notifiable (notifiable_type, notifiable_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: model_has_permissions
DROP TABLE IF EXISTS model_has_permissions;

CREATE TABLE model_has_permissions (
    permission_id BIGINT UNSIGNED NOT NULL,
    model_type VARCHAR(255) NOT NULL,
    model_id BIGINT UNSIGNED NOT NULL,
    team_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (team_id, permission_id, model_id, model_type),
    INDEX idx_model_has_permissions_model (model_id, model_type),
    INDEX idx_model_has_permissions_team (team_id),
    CONSTRAINT fk_model_has_permissions_permission
        FOREIGN KEY (permission_id)
        REFERENCES permissions(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_model_has_permissions_team
        FOREIGN KEY (team_id)
        REFERENCES teams(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: model_has_roles
DROP TABLE IF EXISTS model_has_roles;

CREATE TABLE model_has_roles (
    role_id BIGINT UNSIGNED NOT NULL,
    model_type VARCHAR(255) NOT NULL,
    model_id BIGINT UNSIGNED NOT NULL,
    team_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (team_id, role_id, model_id, model_type),
    INDEX idx_model_has_roles_model (model_id, model_type),
    INDEX idx_model_has_roles_team (team_id),
    CONSTRAINT fk_model_has_roles_role
        FOREIGN KEY (role_id)
        REFERENCES roles(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_model_has_roles_team
        FOREIGN KEY (team_id)
        REFERENCES teams(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: role_has_permissions
DROP TABLE IF EXISTS role_has_permissions;

CREATE TABLE role_has_permissions (
    permission_id BIGINT UNSIGNED NOT NULL,
    role_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (permission_id, role_id),
    CONSTRAINT fk_role_has_permissions_permission
        FOREIGN KEY (permission_id)
        REFERENCES permissions(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_role_has_permissions_role
        FOREIGN KEY (role_id)
        REFERENCES roles(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: favorites
DROP TABLE IF EXISTS favorites;

CREATE TABLE favorites (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL COMMENT 'user_id',
    favoriteable_id BIGINT UNSIGNED NOT NULL,
    favoriteable_type VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_favorites_user (user_id),
    INDEX idx_favorites_favoriteable (favoriteable_type, favoriteable_id),
    CONSTRAINT fk_favorites_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- TABLAS DE PROYECTOS Y TAREAS
-- ============================================================================

-- Tabla: projects
DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_client_company BIGINT UNSIGNED NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT NULL,
    default_pricing_type ENUM('hourly', 'fixed', 'monthly') NOT NULL DEFAULT 'hourly',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    archived_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_projects_client_company
        FOREIGN KEY (id_client_company)
        REFERENCES client_companies(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: project_user_access
DROP TABLE IF EXISTS project_user_access;

CREATE TABLE project_user_access (
    id_user BIGINT UNSIGNED NOT NULL,
    id_project BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_user, id_project),
    CONSTRAINT fk_project_user_access_user
        FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_project_user_access_project
        FOREIGN KEY (id_project)
        REFERENCES projects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: task_groups
DROP TABLE IF EXISTS task_groups;

CREATE TABLE task_groups (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_project BIGINT UNSIGNED NOT NULL,
    name VARCHAR(255) NOT NULL,
    order_column INT UNSIGNED NOT NULL,
    archived_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_task_groups_project
        FOREIGN KEY (id_project)
        REFERENCES projects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: tasks
DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_project BIGINT UNSIGNED NOT NULL,
    id_group BIGINT UNSIGNED NOT NULL,
    id_user_created_by BIGINT UNSIGNED NULL,
    id_user_assigned_to BIGINT UNSIGNED NULL,
    id_invoice BIGINT UNSIGNED NULL,
    name VARCHAR(255) NOT NULL,
    number INT UNSIGNED NOT NULL,
    description TEXT NULL,
    due_on DATE NULL,
    estimation DECIMAL(6,2) UNSIGNED NULL,
    hidden_from_clients BOOLEAN DEFAULT FALSE,
    billable BOOLEAN DEFAULT TRUE,
    order_column INT UNSIGNED NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    assigned_at TIMESTAMP NULL DEFAULT NULL,
    completed_at TIMESTAMP NULL DEFAULT NULL,
    archived_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_tasks_project
        FOREIGN KEY (id_project)
        REFERENCES projects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_tasks_group
        FOREIGN KEY (id_group)
        REFERENCES task_groups(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_tasks_user_created_by
        FOREIGN KEY (id_user_created_by)
        REFERENCES users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT fk_tasks_user_assigned_to
        FOREIGN KEY (id_user_assigned_to)
        REFERENCES users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT fk_tasks_invoice
        FOREIGN KEY (id_invoice)
        REFERENCES invoices(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: label_task
DROP TABLE IF EXISTS label_task;

CREATE TABLE label_task (
    id_label BIGINT UNSIGNED NOT NULL,
    id_task BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_label, id_task),
    CONSTRAINT fk_label_task_label
        FOREIGN KEY (id_label)
        REFERENCES labels(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_label_task_task
        FOREIGN KEY (id_task)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: subscribe_task
DROP TABLE IF EXISTS subscribe_task;

CREATE TABLE subscribe_task (
    id_user BIGINT UNSIGNED NOT NULL,
    id_task BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_user, id_task),
    CONSTRAINT fk_subscribe_task_user
        FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_subscribe_task_task
        FOREIGN KEY (id_task)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: attachments_task
DROP TABLE IF EXISTS attachments_task;

CREATE TABLE attachments_task (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_task BIGINT UNSIGNED NOT NULL,
    id_user BIGINT UNSIGNED NOT NULL,
    name VARCHAR(255) NOT NULL,
    path VARCHAR(500) NOT NULL,
    thumb VARCHAR(500) DEFAULT NULL,
    type VARCHAR(100) NOT NULL,
    size INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_attachments_task_task
        FOREIGN KEY (id_task)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_attachments_task_user
        FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: time_logs
DROP TABLE IF EXISTS time_logs;

CREATE TABLE time_logs (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_task BIGINT UNSIGNED NOT NULL,
    id_user BIGINT UNSIGNED NOT NULL,
    minutes SMALLINT UNSIGNED DEFAULT NULL,
    timer_start INT UNSIGNED DEFAULT NULL,
    timer_stop INT UNSIGNED DEFAULT NULL,
    created_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_time_logs_task
        FOREIGN KEY (id_task)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_time_logs_user
        FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: comments
DROP TABLE IF EXISTS comments;

CREATE TABLE comments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user BIGINT UNSIGNED NOT NULL,
    id_task BIGINT UNSIGNED NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_comments_user
        FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_comments_task
        FOREIGN KEY (id_task)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- TABLAS DE AUDITORÍA Y ACTIVIDADES
-- ============================================================================

-- Tabla: audits
DROP TABLE IF EXISTS audits;

CREATE TABLE audits (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_type VARCHAR(255) NULL,
    user_id BIGINT UNSIGNED NULL,
    event VARCHAR(255) NOT NULL,
    auditable_type VARCHAR(255) NOT NULL,
    auditable_id BIGINT UNSIGNED NOT NULL,
    old_values TEXT NULL,
    new_values TEXT NULL,
    url TEXT NULL,
    ip_address VARCHAR(45) NULL,
    user_agent VARCHAR(1023) NULL,
    tags VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_audits_user (user_id, user_type),
    INDEX idx_audits_auditable (auditable_id, auditable_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla: activities
DROP TABLE IF EXISTS activities;

CREATE TABLE activities (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_project BIGINT UNSIGNED NOT NULL,
    id_user BIGINT UNSIGNED NOT NULL,
    title VARCHAR(255) NOT NULL,
    subtitle VARCHAR(255) NOT NULL,
    activity_capable_id BIGINT UNSIGNED NOT NULL,
    activity_capable_type VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_activities_project
        FOREIGN KEY (id_project)
        REFERENCES projects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_activities_user
        FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    INDEX idx_activities_activity_capable (activity_capable_id, activity_capable_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
