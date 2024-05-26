import sqlite3

def initialize_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id TEXT PRIMARY KEY,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_data():
    id = input("Введите ID: ")
    try:
        status = int(input("Выберите статус: 1-standart, 2-premium "))
        if status == 1:
            status1 = 'standart'
        elif status == 2:
            status1 = 'premium'
    except:
        pass

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (id, status) VALUES (?, ?)', (id, status1))
    conn.commit()
    conn.close()


def delete_data():
    id = input("Введите ID строки, которую вы хотите удалить: ")
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM data WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update_status():
    id = input("Введите ID строки, статус которой нужно изменить: ")
    try:
        new_status = int(input("Выберите статус: 1-standart, 2-premium "))
        if new_status == 1:
            status = 'standart'
        elif new_status == 2:
            status = 'premium'
    except:
        pass
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE data SET status = ? WHERE id = ?', (status, id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    try:
        action = int(input('Что хотите сделать? 1-добавить аккаунт, 2-удалить аккаунт, 3-обновить статус аккаунта  '))
        if action == 1:
            add_data()
        elif action == 2:
            delete_data()
        elif action == 3:
            update_status()
    except:
        pass

