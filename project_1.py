with open("my_file.txt") as file:
    task = file.readlines() 
    print(task)

while True:
    print("\nOptions: ")
    print("1. add tasks? ")
    print("2. remove task? ")
    print("3. view task? ")
    print("4. exit")
#made my prints corresponding to each option to my todo list
    choice = input("choose options 1-4: ")
#gave my choice its variable
    if choice == "1":
        a = input("enter task: ")
        task.append(a)
#if statements for my option 1 
    elif choice == "2":
        task_number = int(input("enter task choice to remove: "))
        del task[task_number - 1]
#else if option for my option 2 going more into depth with more steps of deleting a task from to do list
    elif choice == '3':
        if not task:
            print("No tasks available.")
        else:
            print("Current tasks:")
            for index, task in enumerate(task, start=1):
                print(f"{index}. {task}")
    elif choice == "4":
        with open("my_file.txt", "w") as file:
            task = file.writelines(task) 
        break
        #else if option for viewing your tasks
        # #else option to see if youre typing the proper options  
else:
    print("type a proper option and try again")
    #end of the code hallelujah