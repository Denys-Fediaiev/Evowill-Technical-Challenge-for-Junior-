import sqlite3


class ActivityManager:
    def __init__(self):
        self.conn = sqlite3.connect('activities.sqlite')
        self.create_table()

    def close(self):
        self.conn.close()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY,
                activity TEXT
            )
        ''')
        self.conn.commit()

    def add_activity(self, activity):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO activities (activity) VALUES (?)', (activity,))
        self.conn.commit()

    def get_last_activities(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM activities ORDER BY id DESC')
        return cursor.fetchall()

