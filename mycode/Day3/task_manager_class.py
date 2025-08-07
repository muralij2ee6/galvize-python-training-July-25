class Task:
    def __init__(self, task_id, title, status="Pending"):
        self.id = task_id
        self.title = title
        self.status = status

    def __str__(self):
        return f"{self.id}. {self.title} (Status: {self.status})"

    def update_status(self, new_status):
        if new_status in ["Pending", "Completed"]:
            self.status = new_status
            return True
        return False


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not title.strip():
            return False

        new_task = Task(self.next_id, title.strip())
        self.tasks.append(new_task)
        self.next_id += 1
        return new_task

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def get_all_tasks(self):
        return self.tasks.copy()

    def get_task_stats(self):
        total_chars = sum(len(task.title) for task in self.tasks)
        avg_length = total_chars / len(self.tasks) if self.tasks else 0
        return total_chars, avg_length


def display_menu():
    print("\n" + "=" * 30)
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Change the status of a task")
    print("4. Exit")
    print("=" * 30)


def handle_add_task(task_manager):
    print("\n--- Adding New Task ---")
    title = input("Enter your task: ")
    task = task_manager.add_task(title)
    if task:
        print(f"✓ Task {task.id} saved: {task.title}")
    else:
        print("❌ Task cannot be empty!")


def handle_view_tasks(task_manager):
    print("\n--- Your Tasks ---")
    if not task_manager.tasks:
        print("No tasks yet! Add some tasks first.")
        return

    status_choice = input("Enter status to view (Pending/Completed) or press Enter to see all: ").strip().capitalize()

    if status_choice in ["Pending", "Completed"]:
        tasks = task_manager.get_tasks_by_status(status_choice)
        if tasks:
            print(f"\n{status_choice} Tasks:")
            for task in tasks:
                print(task)
        else:
            print(f"No {status_choice.lower()} tasks found.")
    elif status_choice == "":
        print("\nAll Tasks:")
        for task in task_manager.get_all_tasks():
            print(task)
    else:
        print("Invalid status! Please enter 'Pending' or 'Completed'.")

    # Show statistics
    total_chars, avg_length = task_manager.get_task_stats()
    print(f"\nTotal characters: {total_chars}")
    if task_manager.tasks:
        print(f"Average task length: {avg_length:.1f} characters")


def handle_change_status(task_manager):
    print("\n--- Changing Task Status by Task ID ---")
    if not task_manager.tasks:
        print("No tasks to update! Add some tasks first.")
        return

    try:
        task_id = int(input("Enter the task ID to change its status: "))
        task = task_manager.get_task_by_id(task_id)
        if not task:
            print("❌ Invalid task ID!")
            return

        new_status = input("Enter new status (Pending/Completed): ").strip().capitalize()
        if task.update_status(new_status):
            print(f"✓ Task {task.id} '{task.title}' status updated to {new_status}.")
        else:
            print("❌ Invalid status! Please enter 'Pending' or 'Completed'.")
    except ValueError:
        print("❌ Please enter a valid task ID (number).")


def main():
    print("=== Personal Task Manager ===")
    print("Welcome to your task manager!")

    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            handle_add_task(task_manager)
        elif choice == "2":
            handle_view_tasks(task_manager)
        elif choice == "3":
            handle_change_status(task_manager)
        elif choice == "4":
            print("Goodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("Program ended. Tomorrow we'll learn lists to store unlimited tasks!")


if __name__ == "__main__":
    main()