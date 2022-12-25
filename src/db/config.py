import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "../..", "data", "db.sqlite"))
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


def read_sql(path):
    """Reads an SQL file.

    Args:
        path: A string representing the path to the SQL file.

    Returns:
        sting: A string representing the SQL.
    """
    with open(path, "r", encoding="utf-8") as file:
        sql = file.read()

    return sql


def connect():
    """Returns a connection to the sqlite database.

    Returns:
        connection: A connection to the database.
    """
    return connection


def table_exists(table):
    """Checks if a table exists in the database.

    Args:
        table: A string representing the table name.

    Returns:
        boolean: Returns True if the table exists.
    """
    select_table = read_sql('src/db/sql/select_table.sql')
    cursor.execute(select_table, {'table': table})
    result = cursor.fetchone()

    return result


def drop_tables():
    """Drops all tables in the database.
    """
    drop_table = read_sql('src/db/sql/drop_table.sql')
    cursor.execute(drop_table)
    connection.commit()


def setup_database():
    """Sets up the database."""
    if table_exists('high_scores'):
        return

    schema = read_sql('src/db/sql/schema.sql')
    cursor.execute(schema)
    connection.commit()
