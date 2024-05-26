import sqlite3


def get_data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    table_name = 'data'
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    columns = [description[0] for description in cursor.description]

    connection.close()
    return columns, rows
