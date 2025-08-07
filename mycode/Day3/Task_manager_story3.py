
# task_manager_day1_complete.py
print("=== Personal Task Manager ===")
print("Welcome to your task manager!")

# Variables for storing tasks (maximum 3 for now)
tasks= []
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
                task = {
                    "id": task_count + 1,
                    "title": new_task.strip(),
                    "Status": "Completed"
                }
                tasks.append(task)
                task_count += 1
                print(f"✓ Task {task['id']} saved: {task['title']}")
            else:
                print("❌ Task cannot be empty!")
                
        elif task_count == 1:
            new_task = input("Enter your another task: ")
            if len(new_task) > 0:
                task = {
                    "id": task_count + 1,
                    "title": new_task.strip(),
                    "Status": "Completed"
                }
                tasks.append(task)
                task_count += 1
                print(f"✓ Task {task['id']} saved: {task['title']}")
            else:
                print("❌ Task cannot be empty!")                
            
    elif choice == "2":
        print("\n--- Your Tasks ---")
        if task_count == 0:
            print("No tasks yet! Add some tasks first.")
        else:
            print(f"You have {task_count} task(s):")
            
            for task in tasks:
                print(f"{task['id']}. {task['title']}")
                print(f"Status: {task['Status']}")
                
            # Show some basic statistics
            total_chars = sum(len(task['title']) for task in tasks)
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