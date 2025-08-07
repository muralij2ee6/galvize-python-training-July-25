# task_manager_day1_complete.py
print("=== Personal Task Manager ===")
print("Welcome to your task manager!")

# Variables for storing tasks (maximum 3 for now)
tasks = []
task_count = 0
priority_options ={
    "1": "High",
    "2": "Medium",
    "3": "Low"
}

def get_menu_choice():
    valid_choices = ["1", "2", "3", "4"]
    print("\n" + "=" * 30)
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Change the status of a task")
    print("4. Exit")
    print("=" * 30)
    return input("Enter your choice (1, 2, 3 or 4): ")
# Simple interactive loop using basic concepts
while True:
    print("\n" + "=" * 30)
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Change the status of a task")
    print("4. Exit")
    print("=" * 30)

    choice = input("Enter your choice (1, 2, 3 or 4): ")

    if choice == "1":
        print("\n--- Adding New Task ---")

        # Check which slot is available
        if task_count == 0:
            new_task = input("Enter your first task: ")
            if len(new_task) > 0:
                task = {
                    "id": task_count + 1,
                    "title": new_task.strip(),
                    "Status": "Pending"
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
                    "Status": "Pending"
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
            status_choice = input("Enter status to view (Pending/Completed): ").strip()
            if status_choice in ["Pending", "Completed"]:
                filtered_tasks = [task for task in tasks if task['Status'] == status_choice]
                if filtered_tasks:
                    print(f"\n{status_choice} Tasks:")
                    for task in filtered_tasks:
                        print(f"{task['id']}. {task['title']}")
                else:
                    print(f"No {status_choice.lower()} tasks found.")
            else:
                print("Invalid status! Please enter 'Pending' or 'Completed'.")

                # Print all tasks with status (if still needed)
            print("\nAll Tasks with Status:")
            print("\n".join([f"{task['id']}. {task['title']} (Status: {task['Status']})" for task in tasks]))

            # Show some basic statistics
            total_chars = sum(len(task['title']) for task in tasks)
            print(f"\nTotal characters: {total_chars}")
            if task_count > 0:
                average = total_chars / task_count
                print(f"Average task length: {average:.1f} characters")
    elif choice == "3":
        print("\n--- Changing Task Status by Task ID---")
        if task_count == 0:
            print("No tasks to update! Add some tasks first.")
        else:
            task_id = int(input("Enter the task ID to change its status: "))
            if 1 <= task_id <= task_count:
                new_status = input("Enter new status (Pending/Completed): ").strip()
                if new_status in ["Pending", "Completed"]:
                    tasks[task_id - 1]["Status"] = new_status
                    print(f"✓ Task {task_id} Task Name: {task['title']} status updated to {new_status}.")
                else:
                    print("❌ Invalid status! Please enter 'Pending' or 'Completed'.")
            else:
                print("❌ Invalid task ID!")

    elif choice == "4":
        print("Goodbye! Have a productive day!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Program ended. Tomorrow we'll learn lists to store unlimited tasks!")
