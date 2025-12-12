tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    print("Your Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            break

        else:
            print("Invalid choice")
