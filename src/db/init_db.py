from db.connection import connect


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS high_scores;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE high_scores (
            id INTEGER PRIMARY KEY,
            level INTEGER,
            name TEXT,
            score INTEGER
        );
    ''')

    connection.commit()


def init_db():
    connection = connect()

    drop_tables(connection)
    create_tables(connection)
