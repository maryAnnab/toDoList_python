import sqlite3

connection = sqlite3.connect("todo.db")

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass

def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT task FROM task""")
    result = cur.fetchall()

    for row in result:
        print(row[0])



def add_task(connection):
    print("add task")
    task = input("Enter the content of your task: ")
    if task == "0":
       print("Back to menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", {task,})
        print("Task added!")


def delete_task():
    # task_index = int(input("Enter the index of the task to be deleted: "))
    #
    # if task_index < 0 or task_index > len(tasks) - 1:
    #     print("A task with this index does not exist")
    #     return
    #
    # tasks.pop(task_index)
    print("Task deleted!")

create_table(connection)

while True:
    print()
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Leave")

    user_choice = int(input("Select number: "))
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        break

