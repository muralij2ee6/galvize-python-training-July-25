import os
from datetime import datetime

FILENAME = "notes.txt"


def create_notes_file():
    """Create a new notes file if it doesn't exist"""
    try:
        if not os.path.exists(FILENAME):
            with open(FILENAME, 'w') as file:
                file.write("=== My Notes ===\n")
                file.write(f"File created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            print(f"Successfully created {FILENAME}")
        else:
            print(f"{FILENAME} already exists. You can add notes to it.")
    except Exception as e:
        print(f"Error creating file: {e}")


def write_note_to_file():
    """Add a new note to the file with creation timestamp"""
    try:
        if not os.path.exists(FILENAME):
            print("Notes file doesn't exist. Please create it first.")
            return

        note = input("Enter your note (press Enter when done):\n")
        if not note.strip():
            print("Empty note not saved.")
            return

        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(FILENAME, 'a') as file:
            file.write(f"Note created at: {created_at}\n")
            file.write(f"Content: {note}\n")
            file.write("-" * 40 + "\n\n")  # Separator line
        print("Note successfully added with timestamp!")
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_notes_from_file():
    """Read and display all notes from the file with their creation times"""
    try:
        if not os.path.exists(FILENAME):
            print("No notes file found. Please create one first.")
            return

        with open(FILENAME, 'r') as file:
            print("\n=== YOUR NOTES ===")
            print(file.read())
    except Exception as e:
        print(f"Error reading file: {e}")


def clear_notes_file():
    """Clear all notes from the file (hidden option)"""
    try:
        if os.path.exists(FILENAME):
            confirm = input("Are you sure you want to clear all notes? (y/n): ").lower()
            if confirm == 'y':
                with open(FILENAME, 'w') as file:
                    file.write("=== My Notes ===\n")
                    file.write(f"File cleared: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                print("All notes have been cleared.")
    except Exception as e:
        print(f"Error clearing file: {e}")


def main():
    print("It is a party! 🎉")
    print("Welcome to the Enhanced Note Taker App!")

    while True:
        print("\nOptions:")
        print("1. Create a notes file")
        print("2. Write a new Note (with timestamp)")
        print("3. Read notes file (with creation times)")
        print("4. Exit")
        print("(Enter 'clear' to wipe all notes - hidden option)")

        choice = input("Please select an option (1-4): ").strip()

        if choice == "1":
            create_notes_file()
        elif choice == "2":
            write_note_to_file()
        elif choice == "3":
            read_notes_from_file()
        elif choice == "4":
            print("Goodbye!")
            break
        elif choice.lower() == "clear":
            clear_notes_file()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()