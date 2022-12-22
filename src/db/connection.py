import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "../..", "data", "db.sqlite"))
connection.row_factory = sqlite3.Row


def connect():
    return connection