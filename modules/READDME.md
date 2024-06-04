# Modules

This directory contains Python modules that are used across the project for various functionalities.

## Description

- `db_connections.py`: This module contains functions for establishing connections to the MySQL database.
- `sql_operations.py`: This module contains functions for executing SQL operations such as creating tables and inserting data into the database.

## Usage

To use these modules in your project, follow these steps:

1. Import the necessary functions from the modules into your Python script or notebook.
2. Utilize the imported functions to establish database connections and execute SQL operations as needed.

Example:

```python
# Import functions from modules
from modules.db_connections import get_mysql_engine
from modules.sql_operations import execute_sql, CREATE_TABLE_TESTING_DATA_FOR_CSV_INSERTION

# Database connection
user = '<user>'
password = '<password>'
host = 'localhost'
port = 3306  # Change port number if necessary
database = '<database_name>'
engine = get_mysql_engine(user, password, host, port, database)

# Execute SQL script to create the Testing Data Table if it doesn't exist
execute_sql(engine, CREATE_TABLE_TESTING_DATA_FOR_CSV_INSERTION)
```
