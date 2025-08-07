# Define a class to represent each task
class Task:
    def __init__(self, task_id, name, status="pending"):  # Constructor to initialize task info
        self.id = task_id                                 # Unique ID for each task
        self.name = name.strip()                          # Remove any extra spaces from name
        self.status = status                              # Task status: "pending" or "completed"

    def mark_complete(self):                              # Method to mark the task as completed
        self.status = "completed"

    def __str__(self):                                    # How the task will display when printed
        return f"[{self.status.upper()}] Task {self.id}: {self.name}"


# Define a manager class to handle multiple tasks
class TaskManager:
    def __init__(self):                                   # Constructor for TaskManager
        self.tasks = []                                   # Store list of Task objects
        self.task_count = 1                               # Start task IDs from 1

    def add_task(self, name):                             # Add a new task
        if not name.strip():                              # If task name is empty or just spaces
            print("❌ Task cannot be empty!")
            return
        task = Task(self.task_count, name)                # Create a new Task object
        self.tasks.append(task)                           # Add to the task list
        print(f"✅ Task added: {task.name}")               # Confirm to the user
        self.task_count += 1                              # Increment the ID for the next task

    def view_tasks(self):                                 # View all tasks
        if not self.tasks:                                # If no tasks exist
            print("No tasks yet! Add some tasks first.")
            return
        print(f"You have {len(self.tasks)} task(s):")     # Show task count
        for task in self.tasks:                           # Loop and display each task
            print(task)
        total_chars = sum(len(task.name) for task in self.tasks)  # Total characters in task names
        avg_len = total_chars / len(self.tasks)           # Average length of task names
        print(f"\nTotal characters: {total_chars}")
        print(f"Average task length: {avg_len:.1f} characters")

    def update_task_status(self, task_id):                # Mark a task as complete
        for task in self.tasks:                           # Look through all tasks
            if task.id == task_id:                        # If we find a matching ID
                task.mark_complete()                      # Call the method to mark it completed
                print(f"✅ Marked as complete: {task}")    # Confirm to the user
                return
        print("❌ Task ID not found.")                     # If ID is not found

    def show_status(self, filter_by="all"):               # Show tasks filtered by status
        if not self.tasks:                                # If task list is empty
            print("No tasks yet! Add some tasks first.")
            return

        print("\n--- Task Statuses ---")
        for task in self.tasks:
            if filter_by.lower() == "y" and task.status == "pending":   # Show pending only
                print(task)
            elif filter_by.lower() == "n" and task.status == "completed":  # Show completed only
                print(task)
            elif filter_by.lower() == "all":                             # Show all tasks
                print(task)


# === MAIN PROGRAM LOGIC ===
def run_task_manager():                                   # Entry point for the app
    print("=== Personal Task Manager ===")                 # Welcome message
    print("Welcome to your task manager!")

    manager = TaskManager()                               # Create a TaskManager instance

    while True:                                           # Main menu loop
        print("\n" + "=" * 30)
        print("What would you like to do?")
        print("1. Add a task")                            # Option 1: Add task
        print("2. View tasks")                            # Option 2: View all tasks
        print("3. Update task status")                    # Option 3: Mark task completed
        print("4. Show Status")                           # Option 4: Filter tasks by status
        print("5. Exit")                                  # Option 5: Exit program
        print("=" * 30)

        choice = input("Enter your choice: ").strip()     # Read user input

        if choice == "1":
            name = input("Enter your new task: ")         # Ask for task name
            manager.add_task(name)                        # Call method to add task

        elif choice == "2":
            manager.view_tasks()                          # Call method to view all tasks

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))  # Input task ID
                manager.update_task_status(task_id)        # Call method to mark it complete
            except ValueError:                             # Handle non-numeric input
                print("❌ Please enter a valid numeric ID.")

        elif choice == "4":
            filter_option = input("Show (Y) pending / (N) completed / (All): ").lower()  # Input filter
            if filter_option in ["y", "n", "all"]:
                manager.show_status(filter_option)         # Show filtered tasks
            else:
                print("❌ Invalid option. Choose Y, N, or All.")

        elif choice == "5":
            print("👋 Goodbye! Have a productive day!")    # Exit message
            break                                          # Exit the loop

        else:
            print("❌ Invalid choice. Please select a number from 1 to 5.")  # Handle bad input

    print("Program ended. Come back tomorrow for more features!")  # End message


# Run the main function if this file is executed
if __name__ == "__main__":
    run_task_manager()                                     # Start the task manager