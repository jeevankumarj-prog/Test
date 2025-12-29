import sys
import time
from typing import Dict, Tuple
from datetime import datetime

def check_mysql_connection(host: str, user: str, password: str, database: str, port: int = 3306) -> Tuple[bool, str]:
    """Check MySQL database connectivity"""
    try:
        import mysql.connector
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            auth_plugin='mysql_native_password'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        connection.close()
        return True, "MySQL connection successful"
    except ImportError:
        return False, "mysql-connector-python not installed. Run: pip install mysql-connector-python"
    except Exception as e:
        return False, f"MySQL connection failed: {str(e)}"

def check_postgresql_connection(host: str, user: str, password: str, database: str, port: int = 5432) -> Tuple[bool, str]:
    """Check PostgreSQL database connectivity"""
    try:
        import psycopg2
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        connection.close()
        return True, "PostgreSQL connection successful"
    except ImportError:
        return False, "psycopg2 not installed. Run: pip install psycopg2-binary"
    except Exception as e:
        return False, f"PostgreSQL connection failed: {str(e)}"

def check_sqlite_connection(db_path: str) -> Tuple[bool, str]:
    """Check SQLite database connectivity"""
    try:
        import sqlite3
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        connection.close()
        return True, "SQLite connection successful"
    except Exception as e:
        return False, f"SQLite connection failed: {str(e)}"

def check_mssql_connection(host: str, user: str, password: str, database: str, port: int = 1433) -> Tuple[bool, str]:
    """Check MSSQL database connectivity"""
    try:
        import pyodbc
        connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={host},{port};Database={database};UID={user};PWD={password}'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        connection.close()
        return True, "MSSQL connection successful"
    except ImportError:
        return False, "pyodbc not installed. Run: pip install pyodbc"
    except Exception as e:
        return False, f"MSSQL connection failed: {str(e)}"

def check_mongodb_connection(host: str, port: int = 27017, username: str = None, password: str = None) -> Tuple[bool, str]:
    """Check MongoDB database connectivity"""
    try:
        from pymongo import MongoClient
        if username and password:
            uri = f"mongodb://{username}:{password}@{host}:{port}/"
        else:
            uri = f"mongodb://{host}:{port}/"
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        client.close()
        return True, "MongoDB connection successful"
    except ImportError:
        return False, "pymongo not installed. Run: pip install pymongo"
    except Exception as e:
        return False, f"MongoDB connection failed: {str(e)}"

def print_header():
    """Print header information"""
    print("\n" + "="*60)
    print("Database Connectivity Checker")
    print("="*60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def print_result(db_type: str, success: bool, message: str):
    """Print formatted result"""
    status = "✓ SUCCESS" if success else "✗ FAILED"
    print(f"[{db_type}] {status}")
    print(f"  Message: {message}\n")

def main():
    print_header()
    
    # Example configurations - modify these as needed
    configs: Dict[str, Dict] = {
        "MySQL": {
            "type": "mysql",
            "host": "localhost",
            "user": "root",
            "password": "your_password",
            "database": "testdb",
            "port": 3306
        },
        "PostgreSQL": {
            "type": "postgresql",
            "host": "localhost",
            "user": "postgres",
            "password": "your_password",
            "database": "testdb",
            "port": 5432
        },
        "SQLite": {
            "type": "sqlite",
            "db_path": "test.db"
        },
        "MSSQL": {
            "type": "mssql",
            "host": "localhost",
            "user": "sa",
            "password": "your_password",
            "database": "testdb",
            "port": 1433
        },
        "MongoDB": {
            "type": "mongodb",
            "host": "localhost",
            "port": 27017,
            "username": None,
            "password": None
        }
    }
    
    results = []
    
    # Check each database
    for db_name, config in configs.items():
        success = False
        message = ""
        
        try:
            if config["type"] == "mysql":
                success, message = check_mysql_connection(
                    config["host"], config["user"], config["password"], 
                    config["database"], config["port"]
                )
            elif config["type"] == "postgresql":
                success, message = check_postgresql_connection(
                    config["host"], config["user"], config["password"], 
                    config["database"], config["port"]
                )
            elif config["type"] == "sqlite":
                success, message = check_sqlite_connection(config["db_path"])
            elif config["type"] == "mssql":
                success, message = check_mssql_connection(
                    config["host"], config["user"], config["password"], 
                    config["database"], config["port"]
                )
            elif config["type"] == "mongodb":
                success, message = check_mongodb_connection(
                    config["host"], config["port"],
                    config.get("username"), config.get("password")
                )
        except Exception as e:
            success = False
            message = str(e)
        
        print_result(db_name, success, message)
        results.append((db_name, success))
    
    # Print summary
    print("="*60)
    print("Summary:")
    passed = sum(1 for _, success in results if success)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    print("="*60 + "\n")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
