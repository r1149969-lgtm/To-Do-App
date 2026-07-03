tasks=[]

def add_task():
    task = input("Enter a task:")
    tasks.append(task)
    print("Task added successfully!")
    
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def delete_task():
    if len(tasks) == 0:
        print("No task available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
    delete = int(input("Enter task number to delete:"))
    if delete >= 1 and delete <= len(tasks):
        removed = tasks.pop(delete - 1)
        print(f"{removed} deleted successfully!")
    else:
        print("Invalid task number.") 




while True:

    print("\n===== To-Do App =====")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter your choise: ")
    if choice == "1":
       add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task() 
    elif choice == "4":
       print("Thank you! Goodbye.")
       break
else:
       
       print("Invalid choice.Try again.")   