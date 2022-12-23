import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "../..", "data", "db.sqlite"))
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def read_sql(path):
    with open(path, "r") as file:
        sql = file.read()

    return sql

def connect():
    return connection

def table_exists(table):
    select_table = read_sql('src/db/sql/select_table.sql')
    cursor.execute(select_table, {'table': table})
    result = cursor.fetchone()

    return result

def drop_tables():
    drop_table = read_sql('src/db/sql/drop_table.sql')
    cursor.execute(drop_table)
    connection.commit()

def setup_database():
    if table_exists('high_scores'):
        return

    schema = read_sql('src/db/sql/schema.sql')        
    cursor.execute(schema)
    connection.commit()
