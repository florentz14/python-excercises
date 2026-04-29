from __future__ import annotations

import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "database": os.getenv("MYSQL_DATABASE", "ATM_Database_Schema"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "port": int(os.getenv("MYSQL_PORT", 3306)),
}


class DatabaseConnection:
    """Manages database connection with context manager support."""

    def __init__(self, config: dict | None = None):
        self.config = config or DB_CONFIG
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor(dictionary=True)
            return self
        except Error as exc:
            print(f"Database connection error: {exc}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute(self, query: str, params: tuple | None = None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor
        except Error as exc:
            print(f"Query execution error: {exc}")
            raise

    def commit(self):
        if self.connection:
            self.connection.commit()

    def rollback(self):
        if self.connection:
            self.connection.rollback()
