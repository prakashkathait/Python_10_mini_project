# To_do List Program::::::::::::
to_do_list = []
def display_menu():
    print("\nTo-do List Menu:")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove a task")
    print("4.Mark task as complete")
    print("5.Exit")

#function to add a task 

def add_task():
    task = input("\n Enter the task you want to add:")
    to_do_list.append({"task":task,"completed":False})
    print(f'Task "{task}" added.')

#function to view the tasks
def view_task():
    if not to_do_list:
        print("\n Your to-do list is Empty")
    else:
        print("\nYour Task:")
        for index,task in enumerate(to_do_list,1):
            status = "✔" if task["completed"] else "❌"
            print(f"{index}.{task['task']}[{status}]")

#function to remove a task
def remove_task():
    view_task()
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        removed_task = to_do_list.pop(task_number - 1)
        print(f'Task "{removed_task["task"]}" removed.')
    except (IndexError,ValueError):
        print("Invalid task number.")

#function to mark a task as complete
def mark_complete():
    view_task()
    try:
        task_number = int(input("\nEnter the task number to mark as complete: "))
        to_do_list[task_number - 1]["completed"] = True
        print(f'Task "{to_do_list[task_number - 1]["task"]}" marked as complete.')
    except (IndexError,ValueError):
        print("Invalid task number.")

#main loop

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            print("Existing the To-Do List. Goodbye!!")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()


