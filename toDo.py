import sqlite3

connection = sqlite3.connect("todo.db")


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text, category text)""")
    except:
        pass


def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT task, category FROM task""")
    result = cur.fetchall()

    for i, row in enumerate(result, start=1):
        print(str(i) + " - " + row[0] + " - " + row[1])


def add_task(connection):
    print("add task")
    task = input("Enter the content of your task: ")
    category = input("Enter the category of your task (learning, working, freeTime): ")

    if task == "0":
        print("Back to menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task, category) VALUES(?, ?)""", (task, category))
        connection.commit()
        print("Task added!")


def delete_task(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task, category FROM task""")
    result = cur.fetchall()

    for i, row in enumerate(result, start=1):
        print(str(row[0]) + " - " + row[1] + " - " + row[2])

    task_index = int(input("Enter the index of the task to be deleted: "))

    cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,))
    rows_deleted = cur.rowcount
    connection.commit()

    if rows_deleted != 0:
        print("Task deleted!")
    else:
        print("A task with this index does not exist")


def edit_task(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task, category FROM task""")
    result = cur.fetchall()

    for i, row in enumerate(result, start=1):
        print(str(row[0]) + " - " + row[1] + " - " + row[2])

    task_index = int(input("Enter the index of the task to be edited: "))
    new_task_content = input("Enter the new content of your task: ")
    new_category = input("Enter the new category of your task (learning, working, freeTime): ")

    cur.execute("""UPDATE task SET task=?, category=? WHERE rowid=?""", (new_task_content, new_category, task_index))
    rows_edited = cur.rowcount
    connection.commit()

    if rows_edited != 0:
        print("Task edited!")
    else:
        print("A task with this index does not exist")


create_table(connection)

while True:
    print()
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Leave")

    user_choice = int(input("Select number: "))
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        edit_task(connection)

    if user_choice == 5:
        break

connection.close()
