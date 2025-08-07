# task_manager_day1_complete.py
print("=== Personal Task Manager ===")
print("Welcome to your task manager!")

# Variables for storing tasks (maximum 3 for now)
task1 = ""
task2 = ""
task3 = ""
task_count = 0

# Simple interactive loop using basic concepts
while True:
    print("\n" + "="*30)
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks") 
    print("3. Exit")
    print("="*30)
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        print("\n--- Adding New Task ---")
        
        # Check which slot is available
        if task_count == 0:
            new_task = input("Enter your first task: ")
            if len(new_task) > 0:
                task1 = new_task.strip()
                task_count = task_count + 1
                print(f"✓ Task 1 saved: {task1}")
            else:
                print("❌ Task cannot be empty!")
                
        elif task_count == 1:
            new_task = input("Enter your second task: ")
            if len(new_task) > 0:
                task2 = new_task.strip()
                task_count = task_count + 1
                print(f"✓ Task 2 saved: {task2}")
            else:
                print("❌ Task cannot be empty!")
                
        elif task_count == 2:
            new_task = input("Enter your third task: ")
            if len(new_task) > 0:
                task3 = new_task.strip()
                task_count = task_count + 1
                print(f"✓ Task 3 saved: {task3}")
            else:
                print("❌ Task cannot be empty!")
        else:
            print("❌ Maximum 3 tasks allowed for now!")
            print("Tomorrow we'll learn how to store unlimited tasks!")
            
    elif choice == "2":
        print("\n--- Your Tasks ---")
        if task_count == 0:
            print("No tasks yet! Add some tasks first.")
        else:
            print(f"You have {task_count} task(s):")
            
            if len(task1) > 0:
                print(f"1. {task1}")
            if len(task2) > 0:
                print(f"2. {task2}")
            if len(task3) > 0:
                print(f"3. {task3}")
                
            # Show some basic statistics
            total_chars = len(task1) + len(task2) + len(task3)
            print(f"\nTotal characters: {total_chars}")
            if task_count > 0:
                average = total_chars / task_count
                print(f"Average task length: {average:.1f} characters")
                
    elif choice == "3":
        print("Goodbye! Have a productive day!")
        break
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Program ended. Tomorrow we'll learn lists to store unlimited tasks!")