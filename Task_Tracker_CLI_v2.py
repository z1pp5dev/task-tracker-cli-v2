#Layer 1 - Imports
import json


#Layer 2 - Constants and Paths
Data_File = "tasks.json"


#Layer 3 - Safe File I/O
try:
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    if not isinstance(tasks, list):
        tasks = []
        
except FileNotFoundError:
    tasks = []
    with open('tasks.json', 'w') as newtodo:
        json.dump(tasks, newtodo, indent=4)
    print(f"Tasks File does not exist! creating '{Data_File}' now.")

#Layer 4 - Core Logic Engine
while True:
    try:
      menu = int(input("Please enter one of the following options: 1. View Tasks, 2. Add New Task, 3. Complete Task, 4. Remove Task, 5. Save and Exit: "))
    except ValueError:
        print("Invalid Selection! Please enter a number for selection")
        continue
    #View Tasks Logic
    if menu == 1:
        print("\n----- PENDING TASKS -----")
        pending_count = 0
        for index, t in enumerate(tasks, start=1):
            if not t["completed"]:
                print(f"{index}. {t['task']}")
                pending_count += 1
        if pending_count == 0:
            print("No pending tasks!")

        print("\n----- COMPLETED TASKS -----")
        completed_count = 0
        for index, t in enumerate(tasks, start=1):
            if t["completed"]:
                print(f"{index}. {t["task"]} [Completed]")
                completed_count += 1
        if completed_count == 0:
            print("No completed tasks yet.")

                        #Add Task Logic
    elif menu == 2:
        new_task = input("Please enter the task you would like to add: ").strip()
        if new_task:
            tasks.append({"task": new_task, "completed": False})
            print(f"Successfully added '{new_task}' to your to-do list")

    elif menu == 3:
        print("\n----- PENDING TASKS -----")
        #Filter or list pending tasks
        pending_tasks = [t for t in tasks if not t['completed']]

        if not pending_tasks:
            print("No pending tasks to mark complete!")
        else:
            for index, t in enumerate(pending_tasks, start=1):
                print(f"{index}. {t['task']}")
            try:
                task_num = int(input("\nEnter the number of the task to mark complete: "))
                if 1 <= task_num <= len(pending_tasks):
                    #Find the exact task in the task list
                    target_task = pending_tasks[task_num -1]
                    target_task["completed"] = True
                    print(f"Successfully marked '{target_task}' as completed! ")
                else:
                    print('Invalid task number')
            except ValueError:
                print("Please enter a valid number.")
                

    #Remove Task Logic
    elif menu == 4:
        rm_task = input("Please enter the task you wish to delete: ")
        if rm_task in tasks:
            tasks.remove(rm_task)
            print(f"Successfully removed '{rm_task}' from your to-do list")
    
    #Layer 5 - Persistence and Clean Exit
    #Save and Exit Logic
    elif menu == 5:
        with open('tasks.json', 'w') as f:
            json.dump(tasks,f, indent=4)
        print(f"Tasks saved successfully to '{Data_File}'! ")
        break
    
    else:
        print("Please provide a valid selection. (1, 2, 3, or 4) ")

