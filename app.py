from todo_db import TodoDB
from task_manager import TaskManager

db = TodoDB("todo.db")
task_manager = TaskManager(db)

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