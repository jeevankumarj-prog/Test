# Database Connectivity Checker

A Python program to check connectivity to multiple database systems.

## Supported Databases

- MySQL
- PostgreSQL
- SQLite
- MSSQL (SQL Server)
- MongoDB

## Installation

### Prerequisites
- Python 3.6 or higher

### Install Required Libraries

```bash
# For MySQL
pip install mysql-connector-python

# For PostgreSQL
pip install psycopg2-binary

# For MSSQL
pip install pyodbc

# For MongoDB
pip install pymongo

# Or install all at once
pip install mysql-connector-python psycopg2-binary pyodbc pymongo
```

## Usage

### Method 1: Direct Execution (Default Credentials)

Edit the `db_connectivity_checker.py` file and update the database credentials in the `configs` dictionary:

```python
configs: Dict[str, Dict] = {
    "MySQL": {
        "type": "mysql",
        "host": "localhost",
        "user": "root",
        "password": "your_password",
        "database": "testdb",
        "port": 3306
    },
    # ... other databases
}
```

Then run:

```bash
python db_connectivity_checker.py
```

### Method 2: Quick Test with Custom Values

You can modify the credentials directly in the script or create a wrapper script:

```python
from db_connectivity_checker import check_mysql_connection, check_postgresql_connection

# Test MySQL
success, message = check_mysql_connection(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)
print(f"MySQL: {message}")

# Test PostgreSQL
success, message = check_postgresql_connection(
    host="localhost",
    user="postgres",
    password="your_password",
    database="testdb"
)
print(f"PostgreSQL: {message}")
```

### Method 3: Using Configuration File

Modify `db_config.json` with your database credentials:

```json
{
  "mysql": {
    "enabled": true,
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "your_password",
    "database": "testdb"
  }
}
```

## Output Example

```
============================================================
Database Connectivity Checker
============================================================
Timestamp: 2025-12-29 10:30:45

[MySQL] ✓ SUCCESS
  Message: MySQL connection successful

[PostgreSQL] ✗ FAILED
  Message: PostgreSQL connection failed: could not connect to server

[SQLite] ✓ SUCCESS
  Message: SQLite connection successful

[MongoDB] ✗ FAILED
  Message: pymongo not installed. Run: pip install pymongo

============================================================
Summary:
Passed: 2/4
============================================================
```

## Features

- **Multi-Database Support**: Check connectivity for MySQL, PostgreSQL, SQLite, MSSQL, and MongoDB
- **Error Handling**: Graceful error messages for connection failures
- **Detailed Reporting**: Clear success/failure status with diagnostic messages
- **Dependency Detection**: Alerts if required Python libraries are not installed
- **Summary Report**: Shows passed/failed count at the end

## Troubleshooting

### MySQL Connection Issues
- Ensure MySQL server is running
- Verify credentials (host, user, password, database)
- Check firewall settings if connecting remotely

### PostgreSQL Connection Issues
- Ensure PostgreSQL server is running
- Verify pg_hba.conf allows your connection
- Check password authentication method

### SQLite Connection Issues
- Ensure the database file exists or can be created
- Check file permissions in the directory

### MSSQL Connection Issues
- Ensure SQL Server is running
- Install ODBC Driver 17 for SQL Server
- Check SQL Server authentication settings

### MongoDB Connection Issues
- Ensure MongoDB server is running
- Verify host and port are correct
- Check authentication if required

## License

This script is provided as-is for testing purposes.
