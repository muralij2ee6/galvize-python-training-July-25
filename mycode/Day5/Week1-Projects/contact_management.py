import re
import json
from datetime import datetime
from typing import List, Dict, Optional


class Contact:
    def __init__(self, name: str, phone: str, email: str, notes: str = "", category: str = "Other"):
        self.name = name
        self.phone = phone
        self.email = email
        self.notes = notes
        self.category = category
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def validate(self) -> bool:
        """Validate email and phone format"""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        phone_regex = r'^\+?[0-9]{10,15}$'
        return (re.match(email_regex, self.email) is not None and
                re.match(phone_regex, self.phone) is not None)

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email}\n"
                f"Category: {self.category}\n"
                f"Notes: {self.notes}\n"
                f"Last Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')}")

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'notes': self.notes,
            'category': self.category,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class ContactManager:
    def __init__(self):
        self.contacts: List[Contact] = []
        self.categories = ["Family", "Work", "Friends", "Other"]
        self.load_contacts()

    def add_contact(self, contact: Contact) -> str:
        """Add a new contact with duplicate detection"""
        if not contact.validate():
            return "Invalid email or phone format"

        if self._is_duplicate(contact):
            return "Duplicate contact detected"

        self.contacts.append(contact)
        self.save_contacts()
        return "Contact added successfully"

    def _is_duplicate(self, new_contact: Contact) -> bool:
        """Check for duplicate contacts by email or phone"""
        for contact in self.contacts:
            if (contact.email.lower() == new_contact.email.lower() or
                    contact.phone == new_contact.phone):
                return True
        return False

    def search_contacts(self, search_term: str) -> List[Contact]:
        """Search contacts by name, phone, or email (case-insensitive)"""
        if not search_term:
            return []

        search_term = search_term.lower()
        results = []

        for contact in self.contacts:
            if (search_term in contact.name.lower() or
                    search_term in contact.phone or
                    search_term in contact.email.lower() or
                    search_term in contact.notes.lower() or
                    search_term in contact.category.lower()):
                results.append(contact)

        return results

    def edit_contact(self, old_email: str, **kwargs) -> str:
        """Edit existing contact"""
        for contact in self.contacts:
            if contact.email.lower() == old_email.lower():
                contact.update(**kwargs)
                self.save_contacts()
                return "Contact updated successfully"
        return "Contact not found"

    def delete_contact(self, email: str) -> str:
        """Delete contact by email"""
        for i, contact in enumerate(self.contacts):
            if contact.email.lower() == email.lower():
                del self.contacts[i]
                self.save_contacts()
                return "Contact deleted successfully"
        return "Contact not found"

    def get_contacts_by_category(self, category: str) -> List[Contact]:
        """Get contacts grouped by category"""
        return [contact for contact in self.contacts
                if contact.category.lower() == category.lower()]

    def export_to_file(self, filename: str = "contacts.txt") -> str:
        """Export contacts to text file"""
        try:
            with open(filename, 'w') as f:
                for contact in self.contacts:
                    f.write(f"{str(contact)}\n\n")
            return f"Contacts exported to {filename}"
        except Exception as e:
            return f"Export failed: {str(e)}"

    def save_contacts(self):
        """Save contacts to JSON file"""
        with open('contacts.json', 'w') as f:
            json.dump([contact.to_dict() for contact in self.contacts], f, indent=2)

    def load_contacts(self):
        """Load contacts from JSON file"""
        try:
            with open('contacts.json', 'r') as f:
                data = json.load(f)
                self.contacts = [
                    Contact(
                        name=item['name'],
                        phone=item['phone'],
                        email=item['email'],
                        notes=item['notes'],
                        category=item['category']
                    ) for item in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []

    def display_all_contacts(self) -> str:
        """Display all contacts formatted"""
        if not self.contacts:
            return "No contacts found"

        output = []
        for category in self.categories:
            category_contacts = self.get_contacts_by_category(category)
            if category_contacts:
                output.append(f"\n=== {category.upper()} ===")
                for contact in category_contacts:
                    output.append(str(contact))
        return "\n".join(output)


def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\nAdd New Contact")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            notes = input("Notes: ")
            print("Categories:", ", ".join(manager.categories))
            category = input("Category: ")

            contact = Contact(name, phone, email, notes, category)
            result = manager.add_contact(contact)
            print(result)

        elif choice == "2":
            search_term = input("\nEnter search term: ").strip()
            if not search_term:
                print("Please enter a search term")
                continue

            results = manager.search_contacts(search_term)
            if not results:
                print("\nNo contacts found matching your search")
            else:
                print(f"\nFound {len(results)} contacts:")
                for contact in results:
                    print("\n" + str(contact))

        elif choice == "3":
            email = input("\nEnter email of contact to edit: ")
            print("Leave field blank to keep current value")
            name = input(f"New Name: ")
            phone = input(f"New Phone: ")
            new_email = input(f"New Email: ")
            notes = input(f"New Notes: ")
            category = input(f"New Category: ")

            updates = {}
            if name: updates['name'] = name
            if phone: updates['phone'] = phone
            if new_email: updates['email'] = new_email
            if notes: updates['notes'] = notes
            if category: updates['category'] = category

            result = manager.edit_contact(email, **updates)
            print(result)

        elif choice == "4":
            email = input("\nEnter email of contact to delete: ")
            result = manager.delete_contact(email)
            print(result)

        elif choice == "5":
            print("\nAll Contacts:")
            print(manager.display_all_contacts())

        elif choice == "6":
            filename = input("\nEnter filename to export (default: contacts.txt): ") or "contacts.txt"
            result = manager.export_to_file(filename)
            print(result)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()