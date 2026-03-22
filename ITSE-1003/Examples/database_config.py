# -------------------------------------------------
# File Name: database_config.py
# Author: Florentino
# Date: 3/21/26
# Description: Database configuration from ITSE-1003/Examples/.env via python-dotenv.
#              Supports multiple database types and connection management.
# -------------------------------------------------

import os
from pathlib import Path
from typing import Optional, Dict, Any, Union

from dotenv import load_dotenv

# Default: ITSE-1003/Examples/.env (copy from .env.example)
DEFAULT_ENV_PATH = Path(__file__).resolve().parent / ".env"


class DatabaseConfig:
    """Database configuration manager with support for multiple database types."""

    def __init__(self, env_file: Optional[Union[str, Path]] = None):
        """Initialize database configuration from environment variables."""
        self._env_path = Path(env_file) if env_file else DEFAULT_ENV_PATH
        self._load_env_file()
        self._validate_config()

    def _load_env_file(self) -> None:
        """Load variables from ``.env`` via python-dotenv (does not override existing OS env)."""
        load_dotenv(self._env_path)

    @property
    def env_path(self) -> Path:
        """Path to the loaded ``.env`` file."""
        return self._env_path

    def _validate_config(self):
        """Validate required configuration values."""
        db_type = self.db_type
        if db_type not in ['sqlite', 'postgresql', 'mysql', 'mssql']:
            raise ValueError(f"Unsupported database type: {db_type}")
    
    @property
    def db_type(self) -> str:
        """Get database type."""
        return os.getenv('DB_TYPE', 'sqlite').lower()
    
    @property
    def db_host(self) -> str:
        """Get database host."""
        return os.getenv('DB_HOST', 'localhost')
    
    @property
    def db_port(self) -> int:
        """Get database port."""
        return int(os.getenv('DB_PORT', '5432'))
    
    @property
    def db_name(self) -> str:
        """Get database name."""
        return os.getenv('DB_NAME', 'school.db')
    
    @property
    def db_user(self) -> Optional[str]:
        """Get database user."""
        return os.getenv('DB_USER') or None
    
    @property
    def db_password(self) -> Optional[str]:
        """Get database password."""
        return os.getenv('DB_PASSWORD') or None
    
    @property
    def ssl_mode(self) -> str:
        """Get SSL mode."""
        return os.getenv('DB_SSL_MODE', 'disable')
    
    @property
    def timeout(self) -> int:
        """Get connection timeout."""
        return int(os.getenv('DB_TIMEOUT', '30'))
    
    @property
    def pool_size(self) -> int:
        """Get connection pool size."""
        return int(os.getenv('DB_POOL_SIZE', '5'))
    
    @property
    def max_overflow(self) -> int:
        """Get max overflow connections."""
        return int(os.getenv('DB_MAX_OVERFLOW', '10'))
    
    @property
    def pool_recycle(self) -> int:
        """Get pool recycle time."""
        return int(os.getenv('DB_POOL_RECYCLE', '3600'))
    
    @property
    def echo(self) -> bool:
        """Get echo setting for SQLAlchemy."""
        return os.getenv('DB_ECHO', 'false').lower() == 'true'
    
    def get_connection_string(self) -> str:
        """Generate database connection string based on type."""
        db_type = self.db_type
        
        if db_type == 'sqlite':
            return self._get_sqlite_connection_string()
        elif db_type == 'postgresql':
            return self._get_postgresql_connection_string()
        elif db_type == 'mysql':
            return self._get_mysql_connection_string()
        elif db_type == 'mssql':
            return self._get_mssql_connection_string()
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
    
    def get_sqlite_path(self) -> Path:
        """Resolved filesystem path to the SQLite file (under Examples/data/ if relative name)."""
        db_path = Path(self.db_name)
        if not db_path.is_absolute():
            examples_dir = Path(__file__).resolve().parent
            db_path = examples_dir / "data" / self.db_name
        return db_path.resolve()

    def _get_sqlite_connection_string(self) -> str:
        """Generate SQLite connection string (forward slashes for SQLAlchemy)."""
        return f"sqlite:///{self.get_sqlite_path().as_posix()}"
    
    def _get_postgresql_connection_string(self) -> str:
        """Generate PostgreSQL connection string."""
        return (
            f"postgresql://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )
    
    def _get_mysql_connection_string(self) -> str:
        """Generate MySQL connection string."""
        return (
            f"mysql+pymysql://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )
    
    def _get_mssql_connection_string(self) -> str:
        """Generate SQL Server connection string."""
        driver = "ODBC+Driver+17+for+SQL+Server"
        return (
            f"mssql+pyodbc://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
            f"?driver={driver}&TrustServerCertificate=yes"
        )
    
    def get_sqlalchemy_config(self) -> Dict[str, Any]:
        """Get SQLAlchemy configuration dictionary."""
        return {
            'url': self.get_connection_string(),
            'echo': self.echo,
            'pool_size': self.pool_size,
            'max_overflow': self.max_overflow,
            'pool_recycle': self.pool_recycle,
            'pool_pre_ping': True,
            'connect_args': self._get_connect_args()
        }
    
    def _get_connect_args(self) -> Dict[str, Any]:
        """Get database-specific connection arguments."""
        if self.db_type == 'sqlite':
            return {
                'timeout': self.timeout,
                'check_same_thread': False
            }
        elif self.db_type == 'postgresql':
            return {
                'sslmode': self.ssl_mode,
                'connect_timeout': self.timeout
            }
        elif self.db_type == 'mysql':
            return {
                'connect_timeout': self.timeout,
                'charset': 'utf8mb4'
            }
        elif self.db_type == 'mssql':
            return {
                'timeout': self.timeout,
                'TrustServerCertificate': 'yes'
            }
        return {}
    
    def print_config(self):
        """Print current database configuration."""
        print("🗄️ Database Configuration")
        print("=" * 50)
        print(f"📊 Type: {self.db_type}")
        print(f"🌐 Host: {self.db_host}")
        print(f"🔌 Port: {self.db_port}")
        print(f"📁 Database: {self.db_name}")
        print(f"👤 User: {self.db_user or 'N/A'}")
        print(f"🔒 SSL: {self.ssl_mode}")
        print(f"⏱️  Timeout: {self.timeout}s")
        print(f"🏊 Pool Size: {self.pool_size}")
        print("=" * 50)
        print(f"🔗 Connection String: {self.get_connection_string()}")
        print("=" * 50)
    
    def test_connection(self) -> bool:
        """Test database connection."""
        try:
            if self.db_type == 'sqlite':
                import sqlite3

                conn = sqlite3.connect(str(self.get_sqlite_path()))
                conn.close()
                return True
            elif self.db_type == 'postgresql':
                import psycopg2

                conn = psycopg2.connect(
                    host=self.db_host,
                    port=self.db_port,
                    database=self.db_name,
                    user=self.db_user or "",
                    password=self.db_password or "",
                )
                conn.close()
                return True
            elif self.db_type == 'mysql':
                import pymysql  # type: ignore[import-not-found]

                # Stubs expect `db=` (not `database=`) and non-optional user/password.
                conn = pymysql.connect(
                    host=self.db_host,
                    port=self.db_port,
                    db=self.db_name,
                    user=self.db_user or "",
                    password=self.db_password or "",
                )
                conn.close()
                return True
            elif self.db_type == 'mssql':
                import pyodbc  # type: ignore[import-not-found]

                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={self.db_host};"
                    f"DATABASE={self.db_name};"
                    f"UID={self.db_user or ''};"
                    f"PWD={self.db_password or ''};"
                    f"TrustServerCertificate=yes"
                )
                conn = pyodbc.connect(conn_str)
                conn.close()
                return True
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False
        
        return False

# Global configuration instance
db_config = DatabaseConfig()

def get_database_url() -> str:
    """Get database connection URL."""
    return db_config.get_connection_string()

def get_sqlalchemy_config() -> Dict[str, Any]:
    """Get SQLAlchemy configuration."""
    return db_config.get_sqlalchemy_config()

if __name__ == "__main__":
    # Test configuration
    print("🔧 Database Configuration Test")
    print("=" * 50)
    env_path = db_config.env_path
    if env_path.is_file():
        print(f"📄 Env file: {env_path}")
    else:
        print(f"📄 Env file: {env_path} (missing — using defaults / OS environment only)")

    # Print current configuration
    db_config.print_config()
    
    # Test connection
    print("🧪 Testing database connection...")
    if db_config.test_connection():
        print("✅ Connection successful!")
    else:
        print("❌ Connection failed!")
    
    print("=" * 50)
    print("🎯 Database configuration complete!")
