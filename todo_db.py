import sqlite3

class TodoDB:
    def __init__(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name)
            self.create_table()
        except sqlite3.Error as e:
            print("An error occurred while connecting to the database:", str(e))

    def __del__(self):
        self.save_changes()
        self.connection.close()

    def create_table(self):
        try:
            cur = self.connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS task(task text, category text)""")
        except sqlite3.Error as e:
            print("An error occurred:", str(e))

    def save_changes(self):
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred while saving changes:", str(e))
