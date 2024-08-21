# Adding a task
def add_task(tasks):
    task = input("Enter the task :").strip()
    if task:
        tasks.append(task)
        print('Task added successfully.')
    else:
        print("Task was empty.")

# Viewing a task 
def view_tasks(tasks):
    if not tasks:
        print("List is empty.")
    else:
        print("\n To-Do list:")
        for id, task in enumerate(tasks , 1):
            print(f'{id}.{task}')

# removing a task
def remove_task(tasks):
    if not tasks:
        print("The list is empty.")

    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <len(tasks):
            removed_task = tasks.pop(task_number)
            print("Task removed successfully.")
        else: 
            print("NO task to remove.")
            return
    except ValueError:
        print("Enter a vlaid number.")

#Priting the option menu to the user
def display_menu():
    print("Please select from the below choices: ")
    print("Enter 1 to add a task ")
    print("Enter 2 to remove a task")
    print("Enter 3 to view all tasks")
    print("Enter 4 to exit")

# An empty list for tasks 
tasks =[]
print("Welcome to the Online To-Do App")

while True:
    #calling the display method 
    display_menu()

    # Taking user's choice
    choice = input("Choose an option (1-4):")
    if choice =="1":
        # Calling the add task method
        add_task(tasks)
    elif choice =="2":
        # Calling the remove task method
        remove_task(tasks)
    elif choice =="3":
        # Calling view tasks task method
        view_tasks(tasks)
    elif choice=="4":
        print("Thanks for using the To-Do App")
        # exiting the function
        break
    else:
        print("Invalid choice.")