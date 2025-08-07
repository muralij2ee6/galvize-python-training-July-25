class Task:
    """Represents a single task with ID, title, and completion status"""

    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def mark_complete(self):
        """Mark the task as completed"""
        self.completed = True

    def update_title(self, new_title):
        """Update the task title"""
        self.title = new_title.strip()

    def __str__(self):
        """String representation of the task"""
        status = "Completed" if self.completed else "Pending"
        return f"{self.id}. {self.title} (Status: {status})"


class TaskManager:
    """Manages a collection of tasks with enhanced operations"""

    def __init__(self):
        self.tasks = []
        self.task_count = 1  # Starting ID

    def add_task(self, title):
        """Add a new task to the manager"""
        if not title.strip():
            return None, "❌ Task cannot be empty!"

        new_task = Task(self.task_count, title.strip())
        self.tasks.append(new_task)
        self.task_count += 1
        return new_task, f"✓ Task {new_task.id} saved: {new_task.__str__()}"

    def delete_task(self, task_id):
        """Delete a task by its ID"""
        if not self.tasks:
            return False, "📭 No tasks to delete! Add some tasks first."

        try:
            task_id = int(task_id)
        except ValueError:
            return False, "❌ Invalid task ID! Please enter a number."

        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                deleted_task = self.tasks.pop(i)
                return True, f"🗑️ Task {deleted_task.id} '{deleted_task.title}' deleted successfully."

        return False, "❌ Task ID not found!"

    def edit_task(self, task_id, new_title):
        """Edit a task's title by its ID"""
        if not self.tasks:
            return False, "📭 No tasks to edit! Add some tasks first."

        try:
            task_id = int(task_id)
        except ValueError:
            return False, "❌ Invalid task ID! Please enter a number."

        if not new_title.strip():
            return False, "❌ Task title cannot be empty!"

        for task in self.tasks:
            if task.id == task_id:
                old_title = task.title
                task.update_title(new_title)
                return True, f"✏️ Task {task.id} updated: '{old_title}' → '{task.title}'"

        return False, "❌ Task ID not found!"

    def list_tasks(self, status_filter=None):
        """
        List all tasks, optionally filtered by status
        Returns: (filtered_tasks, total_tasks, message)
        """
        if not self.tasks:
            return [], 0, "📭 No tasks yet! Add some tasks first."

        if status_filter:
            if status_filter not in ["Pending", "Completed"]:
                return [], len(self.tasks), "❌ Invalid status! Please enter 'Pending' or 'Completed'."

            filtered = [
                task for task in self.tasks
                if task.completed == (status_filter == "Completed")
            ]

            if not filtered:
                return [], len(self.tasks), f"📭 No {status_filter.lower()} tasks found."

            return filtered, len(self.tasks), f"📋 {status_filter} Tasks:"

        return self.tasks.copy(), len(self.tasks), "📋 All Tasks:"

    def mark_task_status(self, task_id, new_status):
        """Change a task's status by its ID"""
        if not self.tasks:
            return False, "📭 No tasks to update! Add some tasks first."

        try:
            task_id = int(task_id)
        except ValueError:
            return False, "❌ Invalid task ID! Please enter a number."

        for task in self.tasks:
            if task.id == task_id:
                if new_status.lower() == "completed":
                    task.mark_complete()
                    return True, f"✓ Task {task.id} '{task.title}' status updated to Completed."
                elif new_status.lower() == "pending":
                    task.completed = False
                    return True, f"✓ Task {task.id} '{task.title}' status updated to Pending."
                else:
                    return False, "❌ Invalid status! Please enter 'Pending' or 'Completed'."

        return False, "❌ Task ID not found!"

    def summary(self):
        """Generate a summary of task statistics"""
        completed = sum(1 for task in self.tasks if task.completed)
        pending = len(self.tasks) - completed
        total_chars = sum(len(task.title) for task in self.tasks)
        avg_length = total_chars / len(self.tasks) if self.tasks else 0

        return {
            "total": len(self.tasks),
            "completed": completed,
            "pending": pending,
            "total_chars": total_chars,
            "avg_length": avg_length,
            "message": "📊 Task Summary:"
        }


def display_menu():
    """Display the main menu with emojis"""
    print("\n" + "=" * 30)
    print("📋 What would you like to do?")
    print("1️⃣. Add a task")
    print("2️⃣. View tasks")
    print("3️⃣. Change task status")
    print("4️⃣. Edit task")
    print("5️⃣. Delete task")
    print("6️⃣. View summary")
    print("7️⃣. Exit")
    print("=" * 30)


def get_task_id_input(prompt):
    """Helper function to get valid task ID input"""
    while True:
        task_id = input(prompt).strip()
        if task_id.isdigit():
            return int(task_id)
        print("❌ Invalid task ID! Please enter a number.")


def main():
    """Main application function"""
    print("=== 🚀 Enhanced Task Manager ===")
    print("🎉 Welcome to your task manager!")

    manager = TaskManager()

    while True:
        display_menu()
        choice = input("⌨️ Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- ✏️ Adding New Task ---")
            title = input("📝 Enter your task: ")
            task, message = manager.add_task(title)
            print(message)

        elif choice == "2":
            print("\n--- 📋 Your Tasks ---")
            status_choice = input("🔍 Filter by status (Pending/Completed) or leave blank: ").strip().capitalize()

            tasks, total, message = manager.list_tasks(status_choice if status_choice else None)
            print(message)

            if tasks:
                for task in tasks:
                    print(task)

                if not status_choice:
                    stats = manager.summary()
                    print(f"\n📝 Total characters: {stats['total_chars']}")
                    if stats['total'] > 0:
                        print(f"📏 Average task length: {stats['avg_length']:.1f} characters")

        elif choice == "3":
            print("\n--- 🔄 Changing Task Status ---")
            task_id = get_task_id_input("#️⃣ Enter the task ID: ")
            new_status = input("🔄 Enter new status (Pending/Completed): ").strip()
            success, message = manager.mark_task_status(task_id, new_status)
            print(message)

        elif choice == "4":
            print("\n--- ✏️ Editing Task ---")
            task_id = get_task_id_input("#️⃣ Enter the task ID to edit: ")
            new_title = input("📝 Enter new task title: ")
            success, message = manager.edit_task(task_id, new_title)
            print(message)

        elif choice == "5":
            print("\n--- 🗑️ Deleting Task ---")
            task_id = get_task_id_input("#️⃣ Enter the task ID to delete: ")
            success, message = manager.delete_task(task_id)
            print(message)

        elif choice == "6":
            print("\n--- 📊 Task Summary ---")
            stats = manager.summary()
            print(stats["message"])
            print(f"📌 Total tasks: {stats['total']}")
            print(f"✅ Completed: {stats['completed']}")
            print(f"⏳ Pending: {stats['pending']}")
            print(f"📝 Total characters: {stats['total_chars']}")
            if stats['total'] > 0:
                print(f"📏 Average task length: {stats['avg_length']:.1f} characters")

        elif choice == "7":
            print("\n🎉 Goodbye! Have a productive day! 🎉")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")

    print("🛑 Program ended.")


if __name__ == "__main__":
    main()