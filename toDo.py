import sqlite3

class TaskManager:

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

    def show_tasks(self):
        try:
            cur = self.connection.cursor()
            cur.execute("""SELECT task, category FROM task""")
            result = cur.fetchall()

            for i, row in enumerate(result, start=1):
                print(str(i) + " - " + row[0] + " - " + row[1])
        except sqlite3.Error as e:
            print("An error occurred:", str(e))

    def add_task(self):
        print("add task")
        task = input("Enter the content of your task: ")
        category = input("Enter the category of your task (grow, work, relax, other): ")

        if task == "0":
            print("Back to menu")
        else:
            try:
                cur = self.connection.cursor()
                cur.execute("""INSERT INTO task(task, category) VALUES(?, ?)""", (task, category))
                self.connection.commit()
                print("Task added!")
            except sqlite3.Error as e:
                print("An error occurred:", str(e))

    def delete_task(self):
        try:
            cur = self.connection.cursor()
            cur.execute("""SELECT rowid, task, category FROM task""")
            result = cur.fetchall()

            for i, row in enumerate(result, start=1):
                print(str(row[0]) + " - " + row[1] + " - " + row[2])

            task_index = int(input("Enter the index of the task to be deleted: "))

            cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,))
            rows_deleted = cur.rowcount

            if rows_deleted != 0:
                print("Task deleted!")
            else:
                print("A task with this index does not exist")
        except (sqlite3.Error, ValueError) as e:
            print("An error occurred:", str(e))

    def edit_task(self):
        try:
            cur = self.connection.cursor()
            cur.execute("""SELECT rowid, task, category FROM task""")
            result = cur.fetchall()

            for i, row in enumerate(result, start=1):
                print(str(row[0]) + " - " + row[1] + " - " + row[2])

            task_index = int(input("Enter the index of the task to be edited: "))
            new_task_content = input("Enter the new content of your task: ")
            new_category = input("Enter the new category of your task (grow, work, relax, other): ")

            cur.execute("""UPDATE task SET task=?, category=? WHERE rowid=?""",
                        (new_task_content, new_category, task_index))
            rows_edited = cur.rowcount

            if rows_edited != 0:
                print("Task edited!")
            else:
                print("A task with this index does not exist")
        except (sqlite3.Error, ValueError) as e:
            print("An error occurred:", str(e))

task_manager = TaskManager("todo.db")

while True:
    print()
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Leave")

    user_choice = input("Select number: ")
    print()

    try:
        user_choice = int(user_choice)
        if user_choice == 1:
            task_manager.show_tasks()
        elif user_choice == 2:
            task_manager.add_task()
        elif user_choice == 3:
            task_manager.delete_task()
        elif user_choice == 4:
            task_manager.edit_task()
        elif user_choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please enter a number.")
