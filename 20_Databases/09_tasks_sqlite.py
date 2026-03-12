"""
SQLite3 project and task management database.

Built from the project/task model in python_exercises.sql and extended with:
- task status and priority
- task dependencies
- task checklists
- automatic spent-hours accumulation from time logs
- lightweight activity tracking
"""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Data"
REPORTS_DIR = DATA_DIR / "reports"
DATA_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
DB_FILE = DATA_DIR / "project_tasks.sqlite3.db"


def print_section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def print_rows(cursor: sqlite3.Cursor, query: str, params: tuple = ()) -> None:
    cursor.execute(query, params)
    rows = cursor.fetchall()
    headers = [d[0] for d in cursor.description]

    if not rows:
        print("(no rows)")
        return

    widths = [max(len(str(h)), max(len(str(r[i])) for r in rows)) for i, h in enumerate(headers)]
    header_line = " | ".join(str(headers[i]).ljust(widths[i]) for i in range(len(headers)))
    sep_line = "-+-".join("-" * widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep_line)
    for row in rows:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(headers))))


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;

        DROP TABLE IF EXISTS activities;
        DROP TABLE IF EXISTS task_checklists;
        DROP TABLE IF EXISTS task_dependencies;
        DROP TABLE IF EXISTS comments;
        DROP TABLE IF EXISTS time_logs;
        DROP TABLE IF EXISTS attachments_task;
        DROP TABLE IF EXISTS subscribe_task;
        DROP TABLE IF EXISTS label_task;
        DROP TABLE IF EXISTS labels;
        DROP TABLE IF EXISTS tasks;
        DROP TABLE IF EXISTS task_groups;
        DROP TABLE IF EXISTS project_user_access;
        DROP TABLE IF EXISTS projects;
        DROP TABLE IF EXISTS client_companies;
        DROP TABLE IF EXISTS users;

        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL DEFAULT 'member',
            hourly_rate REAL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE client_companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            city TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_company_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            pricing_type TEXT NOT NULL DEFAULT 'hourly'
                CHECK (pricing_type IN ('hourly', 'fixed', 'monthly')),
            status TEXT NOT NULL DEFAULT 'planning'
                CHECK (status IN ('planning', 'active', 'on_hold', 'completed')),
            start_date TEXT,
            due_date TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (client_company_id) REFERENCES client_companies(id) ON DELETE RESTRICT
        );

        CREATE TABLE project_user_access (
            user_id INTEGER NOT NULL,
            project_id INTEGER NOT NULL,
            access_level TEXT NOT NULL DEFAULT 'member'
                CHECK (access_level IN ('admin', 'member', 'viewer')),
            PRIMARY KEY (user_id, project_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
        );

        CREATE TABLE task_groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            order_column INTEGER NOT NULL,
            archived_at TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
        );

        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            group_id INTEGER NOT NULL,
            created_by_user_id INTEGER,
            assigned_to_user_id INTEGER,
            name TEXT NOT NULL,
            task_number INTEGER NOT NULL,
            description TEXT,
            priority TEXT NOT NULL DEFAULT 'medium'
                CHECK (priority IN ('low', 'medium', 'high', 'critical')),
            status TEXT NOT NULL DEFAULT 'todo'
                CHECK (status IN ('todo', 'in_progress', 'review', 'blocked', 'done')),
            due_on TEXT,
            estimation_hours REAL,
            spent_hours REAL NOT NULL DEFAULT 0,
            billable INTEGER NOT NULL DEFAULT 1 CHECK (billable IN (0, 1)),
            order_column INTEGER NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now')),
            started_at TEXT,
            completed_at TEXT,
            archived_at TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
            FOREIGN KEY (group_id) REFERENCES task_groups(id) ON DELETE CASCADE,
            FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE SET NULL,
            FOREIGN KEY (assigned_to_user_id) REFERENCES users(id) ON DELETE SET NULL,
            UNIQUE (project_id, task_number)
        );

        CREATE TABLE labels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT NOT NULL
        );

        CREATE TABLE label_task (
            label_id INTEGER NOT NULL,
            task_id INTEGER NOT NULL,
            PRIMARY KEY (label_id, task_id),
            FOREIGN KEY (label_id) REFERENCES labels(id) ON DELETE CASCADE,
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
        );

        CREATE TABLE subscribe_task (
            user_id INTEGER NOT NULL,
            task_id INTEGER NOT NULL,
            PRIMARY KEY (user_id, task_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
        );

        CREATE TABLE attachments_task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            file_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            mime_type TEXT NOT NULL,
            file_size_bytes INTEGER NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE time_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            minutes INTEGER NOT NULL CHECK (minutes > 0),
            work_date TEXT NOT NULL,
            note TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
        );

        CREATE TABLE task_dependencies (
            task_id INTEGER NOT NULL,
            depends_on_task_id INTEGER NOT NULL,
            PRIMARY KEY (task_id, depends_on_task_id),
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
            FOREIGN KEY (depends_on_task_id) REFERENCES tasks(id) ON DELETE CASCADE,
            CHECK (task_id <> depends_on_task_id)
        );

        CREATE TABLE task_checklists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            item_text TEXT NOT NULL,
            is_done INTEGER NOT NULL DEFAULT 0 CHECK (is_done IN (0, 1)),
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            done_at TEXT,
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
        );

        CREATE TABLE activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            subtitle TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE INDEX idx_tasks_project ON tasks(project_id);
        CREATE INDEX idx_tasks_group ON tasks(group_id);
        CREATE INDEX idx_tasks_assigned_user ON tasks(assigned_to_user_id);
        CREATE INDEX idx_tasks_status ON tasks(status);
        CREATE INDEX idx_time_logs_task ON time_logs(task_id);
        CREATE INDEX idx_comments_task ON comments(task_id);

        CREATE TRIGGER trg_projects_updated_at
        AFTER UPDATE ON projects
        FOR EACH ROW
        BEGIN
            UPDATE projects SET updated_at = datetime('now') WHERE id = NEW.id;
        END;

        CREATE TRIGGER trg_tasks_updated_at
        AFTER UPDATE ON tasks
        FOR EACH ROW
        BEGIN
            UPDATE tasks SET updated_at = datetime('now') WHERE id = NEW.id;
        END;

        CREATE TRIGGER trg_time_log_accumulate_task_hours
        AFTER INSERT ON time_logs
        FOR EACH ROW
        BEGIN
            UPDATE tasks
            SET spent_hours = ROUND(spent_hours + (NEW.minutes / 60.0), 2)
            WHERE id = NEW.task_id;
        END;

        CREATE TRIGGER trg_checklist_done_timestamp
        AFTER UPDATE ON task_checklists
        FOR EACH ROW
        WHEN NEW.is_done = 1 AND OLD.is_done = 0
        BEGIN
            UPDATE task_checklists
            SET done_at = datetime('now')
            WHERE id = NEW.id;
        END;
        """
    )


def seed_data(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    cur.executemany(
        "INSERT INTO users(name, email, role, hourly_rate) VALUES (?, ?, ?, ?)",
        [
            ("Carlos Mendoza", "carlos@pmhub.local", "admin", 80),
            ("Maria Silva", "maria@pmhub.local", "member", 65),
            ("Luis Ortega", "luis@pmhub.local", "member", 55),
            ("Sofia Kim", "sofia@pmhub.local", "viewer", 0),
        ],
    )

    cur.executemany(
        "INSERT INTO client_companies(name, email, city) VALUES (?, ?, ?)",
        [
            ("Northwind Labs", "contact@northwind.test", "New York"),
            ("BlueOcean Retail", "hello@blueocean.test", "Miami"),
        ],
    )

    cur.executemany(
        """
        INSERT INTO projects(client_company_id, name, description, pricing_type, status, start_date, due_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1, "Customer Portal v2", "Modernize portal UX and backend integrations.", "hourly", "active", "2026-03-01", "2026-06-15"),
            (2, "Inventory Automation", "Automate inventory sync between stores.", "fixed", "planning", "2026-04-01", "2026-08-01"),
        ],
    )

    cur.executemany(
        "INSERT INTO project_user_access(user_id, project_id, access_level) VALUES (?, ?, ?)",
        [
            (1, 1, "admin"),
            (2, 1, "member"),
            (3, 1, "member"),
            (4, 1, "viewer"),
            (1, 2, "admin"),
            (2, 2, "member"),
        ],
    )

    cur.executemany(
        "INSERT INTO task_groups(project_id, name, order_column) VALUES (?, ?, ?)",
        [
            (1, "Backlog", 1),
            (1, "In Progress", 2),
            (1, "Review", 3),
            (1, "Done", 4),
            (2, "Backlog", 1),
        ],
    )

    cur.executemany(
        """
        INSERT INTO tasks(
            project_id, group_id, created_by_user_id, assigned_to_user_id, name, task_number,
            description, priority, status, due_on, estimation_hours, billable, order_column, started_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1, 1, 1, 2, "Design auth flow", 101, "OAuth + refresh tokens + RBAC matrix.", "high", "todo", "2026-04-10", 10, 1, 1, None),
            (1, 2, 1, 3, "Build user profile API", 102, "CRUD + validations + pagination.", "medium", "in_progress", "2026-04-08", 14, 1, 1, "2026-03-20 09:00:00"),
            (1, 3, 2, 1, "Frontend integration tests", 103, "Smoke tests for profile and login.", "medium", "review", "2026-04-12", 8, 1, 1, "2026-03-22 11:00:00"),
            (1, 4, 2, 2, "Notification preferences page", 104, "UI + API for email/push settings.", "low", "done", "2026-03-30", 6, 1, 1, "2026-03-15 10:00:00"),
            (2, 5, 1, 2, "Data mapping workshop", 201, "Define source->target mapping rules.", "high", "todo", "2026-04-20", 5, 0, 1, None),
        ],
    )

    cur.executemany(
        "INSERT INTO labels(name, color) VALUES (?, ?)",
        [
            ("backend", "#2563EB"),
            ("frontend", "#7C3AED"),
            ("qa", "#059669"),
            ("urgent", "#DC2626"),
        ],
    )

    cur.executemany(
        "INSERT INTO label_task(label_id, task_id) VALUES (?, ?)",
        [(1, 1), (1, 2), (2, 4), (3, 3), (4, 1)],
    )

    cur.executemany(
        "INSERT INTO subscribe_task(user_id, task_id) VALUES (?, ?)",
        [(1, 1), (2, 1), (3, 2), (1, 3), (4, 4)],
    )

    cur.executemany(
        "INSERT INTO time_logs(task_id, user_id, minutes, work_date, note) VALUES (?, ?, ?, ?, ?)",
        [
            (2, 3, 90, "2026-03-24", "Initial API endpoints and schema."),
            (2, 3, 120, "2026-03-25", "Validation and unit tests."),
            (3, 1, 60, "2026-03-26", "Review fixes before merge."),
            (4, 2, 45, "2026-03-18", "Final polish and docs."),
        ],
    )

    cur.executemany(
        "INSERT INTO comments(user_id, task_id, content) VALUES (?, ?, ?)",
        [
            (2, 1, "Need final approval for OAuth provider."),
            (3, 2, "Pagination strategy updated to cursor-based."),
            (1, 3, "Please add edge case for deactivated users."),
        ],
    )

    cur.executemany(
        "INSERT INTO task_dependencies(task_id, depends_on_task_id) VALUES (?, ?)",
        [(2, 1), (3, 2)],
    )

    cur.executemany(
        "INSERT INTO task_checklists(task_id, item_text, is_done) VALUES (?, ?, ?)",
        [
            (1, "Define role matrix", 1),
            (1, "Document token lifetimes", 0),
            (2, "Add request validation", 1),
            (2, "Cover pagination in tests", 0),
            (3, "Run full CI pipeline", 0),
        ],
    )

    cur.executemany(
        "INSERT INTO activities(project_id, user_id, title, subtitle) VALUES (?, ?, ?, ?)",
        [
            (1, 1, "Project created", "Customer Portal v2"),
            (1, 2, "Task completed", "Notification preferences page"),
            (1, 3, "Time logged", "Build user profile API"),
        ],
    )

    conn.commit()


def run_demo_queries(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    print_section("PROJECT BOARD WITH TASKS")
    print_rows(
        cur,
        """
        SELECT p.name AS project, tg.name AS task_group, t.task_number, t.name AS task_name,
               t.status, t.priority, u.name AS assigned_to, t.estimation_hours, t.spent_hours
        FROM tasks t
        JOIN projects p ON p.id = t.project_id
        JOIN task_groups tg ON tg.id = t.group_id
        LEFT JOIN users u ON u.id = t.assigned_to_user_id
        ORDER BY p.id, tg.order_column, t.order_column
        """,
    )

    print_section("PROJECT PROGRESS BY STATUS")
    print_rows(
        cur,
        """
        SELECT p.name AS project, t.status, COUNT(*) AS total_tasks
        FROM tasks t
        JOIN projects p ON p.id = t.project_id
        GROUP BY p.name, t.status
        ORDER BY p.name, total_tasks DESC
        """,
    )

    print_section("WORKLOAD BY ASSIGNEE")
    print_rows(
        cur,
        """
        SELECT u.name AS assignee,
               COUNT(t.id) AS assigned_tasks,
               ROUND(COALESCE(SUM(t.estimation_hours), 0), 2) AS estimated_hours,
               ROUND(COALESCE(SUM(t.spent_hours), 0), 2) AS spent_hours,
               ROUND(COALESCE(SUM(t.estimation_hours), 0) - COALESCE(SUM(t.spent_hours), 0), 2) AS remaining_estimate
        FROM users u
        LEFT JOIN tasks t ON t.assigned_to_user_id = u.id
        GROUP BY u.id, u.name
        ORDER BY assigned_tasks DESC, u.name
        """,
    )

    print_section("OVERDUE OR NEAR-DUE OPEN TASKS")
    print_rows(
        cur,
        """
        SELECT t.task_number, t.name, t.status, t.due_on, u.name AS assigned_to
        FROM tasks t
        LEFT JOIN users u ON u.id = t.assigned_to_user_id
        WHERE t.status <> 'done'
          AND t.due_on IS NOT NULL
        ORDER BY date(t.due_on) ASC
        """,
    )

    print_section("LABEL USAGE")
    print_rows(
        cur,
        """
        SELECT l.name AS label, COUNT(*) AS usage_count
        FROM label_task lt
        JOIN labels l ON l.id = lt.label_id
        GROUP BY l.id, l.name
        ORDER BY usage_count DESC, l.name
        """,
    )

    print_section("CHECKLIST COMPLETION")
    print_rows(
        cur,
        """
        SELECT t.task_number, t.name,
               SUM(CASE WHEN tc.is_done = 1 THEN 1 ELSE 0 END) AS done_items,
               COUNT(tc.id) AS total_items
        FROM tasks t
        LEFT JOIN task_checklists tc ON tc.task_id = t.id
        GROUP BY t.id, t.task_number, t.name
        ORDER BY t.task_number
        """,
    )


def run_business_flow(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    print_section("TRANSACTION DEMO: CREATE + MOVE + LOG + COMMENT")

    cur.execute(
        """
        INSERT INTO tasks(
            project_id, group_id, created_by_user_id, assigned_to_user_id, name, task_number,
            description, priority, status, due_on, estimation_hours, billable, order_column
        )
        VALUES (1, 1, 1, 3, ?, 105, ?, 'high', 'todo', '2026-04-15', 7, 1, 2)
        """,
        (
            "Implement audit export endpoint",
            "Endpoint to export project activities in CSV/JSON.",
        ),
    )
    new_task_id = cur.lastrowid

    # Move to In Progress group and update status.
    cur.execute(
        """
        UPDATE tasks
        SET group_id = 2, status = 'in_progress', started_at = datetime('now')
        WHERE id = ?
        """,
        (new_task_id,),
    )

    # Log work and add discussion.
    cur.execute(
        """
        INSERT INTO time_logs(task_id, user_id, minutes, work_date, note)
        VALUES (?, 3, 75, date('now'), ?)
        """,
        (new_task_id, "Built CSV export and response streaming."),
    )
    cur.execute(
        """
        INSERT INTO comments(user_id, task_id, content)
        VALUES (1, ?, ?)
        """,
        (new_task_id, "Please include filters by date range and user."),
    )
    cur.execute(
        """
        INSERT INTO activities(project_id, user_id, title, subtitle)
        VALUES (1, 3, 'Task moved to in_progress', 'Implement audit export endpoint')
        """
    )

    conn.commit()

    print_rows(
        cur,
        """
        SELECT task_number, name, status, spent_hours, started_at
        FROM tasks
        WHERE id = ?
        """,
        (new_task_id,),
    )


def export_reports(conn: sqlite3.Connection) -> None:
    print_section("EXPORT REPORTS TO CSV")

    tasks_report = pd.read_sql_query(
        """
        SELECT p.name AS project, tg.name AS task_group, t.task_number, t.name AS task_name,
               t.status, t.priority, t.due_on, t.estimation_hours, t.spent_hours
        FROM tasks t
        JOIN projects p ON p.id = t.project_id
        JOIN task_groups tg ON tg.id = t.group_id
        ORDER BY p.id, tg.order_column, t.order_column
        """,
        conn,
    )

    workload_report = pd.read_sql_query(
        """
        SELECT u.name AS assignee,
               COUNT(t.id) AS assigned_tasks,
               ROUND(COALESCE(SUM(t.estimation_hours), 0), 2) AS estimated_hours,
               ROUND(COALESCE(SUM(t.spent_hours), 0), 2) AS spent_hours
        FROM users u
        LEFT JOIN tasks t ON t.assigned_to_user_id = u.id
        GROUP BY u.id, u.name
        ORDER BY assigned_tasks DESC, u.name
        """,
        conn,
    )

    project_progress_report = pd.read_sql_query(
        """
        SELECT p.name AS project, t.status, COUNT(*) AS total_tasks
        FROM tasks t
        JOIN projects p ON p.id = t.project_id
        GROUP BY p.name, t.status
        ORDER BY p.name, total_tasks DESC
        """,
        conn,
    )

    files = {
        "tasks_report.csv": tasks_report,
        "workload_report.csv": workload_report,
        "project_progress_report.csv": project_progress_report,
    }

    for filename, dataframe in files.items():
        target = REPORTS_DIR / filename
        dataframe.to_csv(target, index=False)
        print(f"- {target}")


def main() -> None:
    if DB_FILE.exists():
        DB_FILE.unlink()

    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")

    create_schema(conn)
    seed_data(conn)
    run_demo_queries(conn)
    run_business_flow(conn)
    export_reports(conn)

    print_section("DATABASE METADATA")
    cur = conn.cursor()
    print_rows(
        cur,
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name
        """,
    )

    print(f"\nDatabase file created: {DB_FILE}")
    print(f"Generated at: {datetime.now().isoformat(timespec='seconds')}")

    conn.close()


if __name__ == "__main__":
    main()
