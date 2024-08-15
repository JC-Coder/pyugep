def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete a Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f'Task "{task}" added.')

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f'{index}. {task["task"]} - {status}')

def mark_task_done(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to mark as done: "))
    if 1 <= task_no <= len(tasks):
        tasks[task_no - 1]["done"] = True
        print(f'Task "{tasks[task_no - 1]["task"]}" marked as done.')
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to delete: "))
    if 1 <= task_no <= len(tasks):
        task = tasks.pop(task_no - 1)
        print(f'Task "{task["task"]}" deleted.')
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        choice = show_menu()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
