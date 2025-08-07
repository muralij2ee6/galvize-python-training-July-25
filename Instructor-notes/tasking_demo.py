# task_manager_day1_complete.py
print("=== Personal Task Manager ===")
print("Welcome to your task manager!")

# Variables for storing tasks (maximum 3 for now)
# task1 = ""
# task2 = ""
# task3 = ""
# next_id = 0

tasks = []
next_id = 1

# Simple interactive loop using basic concepts
while True:
    print("\n" + "="*30)
    print("What would you like to do?")
    print("1. Add a task")
    print("2. next_id tasks") 
    print("3. Exit")
    print("="*30)
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        print("\n--- Adding New Task ---")
        
        # Check which slot is available
        if next_id == 1:
            task_title = input("Enter your first task: ")
            if len(task_title) > 0:
                # create a new task dictionary
                task = {
                    "id": next_id,
                    "title": task_title.strip(),
                    "completed": False
                }
                tasks.append(task) # add to our list of tasks
                next_id = next_id + 1  # increment task ID
                print(f"✓ Task #{next_id-1} '{task_title}' added!")
            else:
                print("❌ Task cannot be empty!")
            
    elif choice == "2":
        print("\n--- Your Tasks ---")
        if next_id == 0:
            print("No tasks yet! Add some tasks first.")
        else:
            print(f"You have {next_id} task(s):")
            
            # if len(tasks) > 0:
            #     print(f"1. {task1}")
                
            # # Show some basic statistics
            # total_chars = len(task1) + len(task2) + len(task3)
            # print(f"\nTotal characters: {total_chars}")
            # if next_id > 0:
            #     average = total_chars / next_id
            #     print(f"Average task length: {average:.1f} characters")
                
    elif choice == "3":
        print("Goodbye! Have a productive day!")
        break
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Program ended. Tomorrow we'll learn lists to store unlimited tasks!")






# When we create a task, by default it will a "Pending" status. 

# To mark a task as complete, we can add a new option to our menu:
# 5. Mark task complete. 

# when we go to this option, we can ask the user to enter the task ID they want to mark as complete.
# given that all the tasks, are showing up with their ID's, we can easily find the task in our list of tasks and mark it as complete by setting the "completed" key to True.


# then when we view all tasks, we can show the status of each task as either "✓ Complete" or "Pending".

# Stretch - 
# Create a new option to view only completed tasks.
# Create another option to view only pending tasks.
# and in each of these options, we can use list comprehension to filter the tasks based on their status.
# 