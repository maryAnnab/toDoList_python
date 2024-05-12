class TaskManager:
    def __init__(self, db_instance):
        self.db_instance = db_instance

    def show_tasks(self):
        try:
            cur = self.db_instance.connection.cursor()
            cur.execute("""SELECT task, category FROM task""")
            result = cur.fetchall()

            for i, (task, category) in enumerate(result, start=1):
                print(f"{i} - {task} - {category}")
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
                cur = self.db_instance.connection.cursor()
                cur.execute("""INSERT INTO task(task, category) VALUES(?, ?)""", (task, category))
                self.db_instance.connection.commit()
                print("Task added!")
            except sqlite3.Error as e:
                print("An error occurred:", str(e))

    def delete_task(self):
        try:
            cur = self.db_instance.connection.cursor()
            cur.execute("""SELECT rowid, task, category FROM task""")
            result = cur.fetchall()

            for row in result:
                print(f"{row[0]} - {row[1]} - {row[2]}")

            task_index = int(input("Enter the index of the task to be deleted: "))

            cur = self.db_instance.connection.cursor()
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
            cur = self.db_instance.connection.cursor()
            cur.execute("""SELECT rowid, task, category FROM task""")
            result = cur.fetchall()

            for row in result:
                print(f"{row[0]} - {row[1]} - {row[2]}")

            task_index = int(input("Enter the index of the task to be edited: "))
            new_task_content = input("Enter the new content of your task: ")
            new_category = input("Enter the new category of your task (grow, work, relax, other): ")

            cur = self.db_instance.connection.cursor()
            cur.execute("""UPDATE task SET task=?, category=? WHERE rowid=?""",
                        (new_task_content, new_category, task_index))
            rows_edited = cur.rowcount

            if rows_edited != 0:
                print("Task edited!")
            else:
                print("A task with this index does not exist")
        except (sqlite3.Error, ValueError) as e:
            print("An error occurred:", str(e))
