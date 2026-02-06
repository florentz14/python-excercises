# -------------------------------------------------
# File: 01_connection_test.py
# Description: Test MySQL database connection.
#              Uses .env file for credentials.
# -------------------------------------------------

import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()


def test_connection():
    """Test connection to MySQL database."""
    
    # Get credentials from environment variables
    config = {
        'host': os.getenv('MYSQL_HOST', 'localhost'),
        'user': os.getenv('MYSQL_USER', 'root'),
        'password': os.getenv('MYSQL_PASSWORD', ''),
        'database': os.getenv('MYSQL_DATABASE', 'mydatabase'),
        'port': int(os.getenv('MYSQL_PORT', 3306))
    }
    
    print("=" * 50)
    print("MySQL Connection Test")
    print("=" * 50)
    print(f"Host: {config['host']}")
    print(f"Port: {config['port']}")
    print(f"User: {config['user']}")
    print(f"Database: {config['database']}")
    print("=" * 50)
    
    try:
        # Attempt to connect
        print("\nConnecting to MySQL...")
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            # Get server info
            db_info = connection.server_info
            print(f"[OK] Connected to MySQL Server version {db_info}")
            
            # Get cursor and check database
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()[0]
            print(f"[OK] Connected to database: {db_name}")
            
            # Show tables in the database
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            
            if tables:
                print(f"\nTables in '{db_name}':")
                for table in tables:
                    print(f"  - {table[0]}")
            else:
                print(f"\nNo tables found in '{db_name}'")
            
            cursor.close()
            connection.close()
            print("\n[OK] Connection closed successfully")
            return True
            
    except Error as e:
        print(f"\n[ERROR] Connecting to MySQL: {e}")
        print("\nPossible solutions:")
        print("  1. Make sure MySQL server is running")
        print("  2. Check your credentials in .env file")
        print("  3. Verify the database exists")
        print("  4. Check if the port is correct (default: 3306)")
        return False


def test_connection_without_database():
    """Test connection to MySQL server (without specifying database)."""
    
    config = {
        'host': os.getenv('MYSQL_HOST', 'localhost'),
        'user': os.getenv('MYSQL_USER', 'root'),
        'password': os.getenv('MYSQL_PASSWORD', ''),
        'port': int(os.getenv('MYSQL_PORT', 3306))
    }
    
    print("\n" + "=" * 50)
    print("Testing connection to MySQL Server (no database)")
    print("=" * 50)
    
    try:
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            print("[OK] Connected to MySQL Server")
            
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            
            print("\nAvailable databases:")
            for db in databases:
                print(f"  - {db[0]}")
            
            cursor.close()
            connection.close()
            return True
            
    except Error as e:
        print(f"[ERROR] {e}")
        return False


if __name__ == "__main__":
    # Check if using default placeholder credentials
    if os.getenv('MYSQL_USER') == 'yourusername':
        print("=" * 50)
        print("WARNING: Using placeholder credentials!")
        print("=" * 50)
        print("\nPlease update the .env file with your MySQL credentials:")
        print("  - MYSQL_HOST=localhost")
        print("  - MYSQL_USER=your_actual_username")
        print("  - MYSQL_PASSWORD=your_actual_password")
        print("  - MYSQL_DATABASE=mydatabase")
        print("  - MYSQL_PORT=3306")
        print("\nLocation: python-excercises/.env")
        print("=" * 50)
    else:
        # First try to connect to the server
        server_ok = test_connection_without_database()
        
        if server_ok:
            # Then try to connect to the specific database
            print()
            test_connection()
        else:
            print("\nCould not connect to MySQL server.")
            print("Please make sure MySQL is installed and running.")
