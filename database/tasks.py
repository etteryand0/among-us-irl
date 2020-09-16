class Database:
    def spectate_tasks():
        import sqlite3
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        tasks = list(cursor.execute('SELECT * FROM tasks'))
        for task in tasks:
            print(task)
