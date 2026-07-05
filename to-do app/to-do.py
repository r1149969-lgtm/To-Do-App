

tasks = []

while True:

    print("\n===== To-Do App =====")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter your choise: ")

    if choice == "1":
       
       task = input("Enter a task: ")
       tasks.append(task)
       
    elif choice == "2":

        if len (tasks)==0:
            print("No task available.")
        else:
            print("\n Your Tasks: ")
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
        
    elif choice == "3":
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("\n Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1 }.{tasks[i]}")
            Delete = int(input ("Enter task number to delete :"))
        if Delete >= 1 & Delete <= len(tasks):
            removed=tasks.pop(Delete-1)
            print(f"{removed} deleted successfully!")
        else:
            print("Invalid task number.")
        
        
        

    elif choice == "4":
       
       print("Thank you! Goodbye.")
       break
else:
       
       print("Invalid choice.Try again.")   