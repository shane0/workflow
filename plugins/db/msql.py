#!/usr/bin/env python
"""pick a server database and run a query against it"""

# todo add sqlite postgres mongo
# this only works for domain auth
def execute_query(server, database, query):
    """Executes a SQL query using the provided server, database, and query.

    Args:
        server (str): The SQL Server server name.
        database (str): The SQL Server database name.
        query (str): The SQL query to execute.

    Returns:
        list: A list of tuples, where each tuple represents a row of results.
    """

    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows