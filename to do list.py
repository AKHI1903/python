
tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Enter a valid number!")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
