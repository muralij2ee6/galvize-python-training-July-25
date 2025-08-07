print("=== Personal Task Manager v3.0 ===")
from datetime import datetime
class Task:
    """Represents a single task with ID, title, and completion status."""

    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title.strip()
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """Return a formatted string representation of the task."""
        status = "✓ Complete" if self.completed else "○ Pending"
        return f"{self.id:<4} {status:<12} {self.title}, {self.created_at}"


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Add a new task with the given title."""
        task = Task(self.next_id, title)
        self.tasks.append(task)
        print(f"✓ Task #{self.next_id} '{title}' added!, at '{task.created_at }'")
        self.next_id += 1

    def list_tasks(self, filter_status=None):
        """List tasks based on filter: all, pending, or completed."""
        if filter_status == "pending":
            filtered = [t for t in self.tasks if not t.completed]
        elif filter_status == "completed":
            filtered = [t for t in self.tasks if t.completed]
        else:
            filtered = self.tasks

        header = {
            None: "--- All Tasks ---",
            "pending": "--- Pending Tasks ---",
            "completed": "--- Completed Tasks ---"
        }[filter_status]

        print("\n" + header)
        if not filtered:
            print("No tasks found!")
        else:
            print(f"{'ID':<4} {'Status':<12} {'Title'} {'Created At'}")
            print("-" * 40)
            for task in filtered:
                print(task)

    def mark_complete(self, task_id):
        """Mark a specific task complete by its ID."""
        for task in self.tasks:
            if task.id == task_id and not task.completed:
                task.mark_complete()
                print(f"✓ Task #{task_id} '{task.title}' marked complete!")
                return
        print(f"❌ Task #{task_id} not found or already completed!")

    def summary(self):
        """Print a summary of total, completed, and pending tasks."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        pending = total - completed
        print(f"\nSummary: {total} total, {completed} completed, {pending} pending")


def main():
    manager = TaskManager()

    while True:
        print("\n" + "="*50)
        print("TASK MANAGER MENU")
        print("="*50)
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Mark task complete")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            if title.strip():
                manager.add_task(title)
            else:
                print("❌ Task title cannot be empty!")
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks("pending")
        elif choice == "4":
            manager.list_tasks("completed")
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.mark_complete(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if choice != "6":
            manager.summary()


if __name__ == "__main__":
    main()