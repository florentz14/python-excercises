# -------------------------------------------------
# File Name: 56_contact_book.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Contact Book - full CRUD with JSON storage.
# -------------------------------------------------

"""
Exercise: Contact Book Application (OOP)
Full-featured contact management system using the ContactBook class.
"""

import json
import os


class ContactBook:
    """
    A contact book manager using dictionaries.
    """

    def __init__(self, filename="contacts.json"):
        """Initialize contact book. Uses script directory for file storage."""
        self.filename = filename
        self.contacts = {}
        # Store file in script directory for portability
        self.filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON file."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    self.contacts = json.load(f)
                print(f"[OK] Loaded {len(self.contacts)} contacts from {self.filename}")
            except json.JSONDecodeError:
                print(f"[!] Error reading {self.filename}, starting fresh")
                self.contacts = {}
        else:
            print("No existing contact file found, starting fresh")

    def save_contacts(self):
        """Save contacts to JSON file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, indent=2)
        print(f"✓ Saved {len(self.contacts)} contacts to {self.filename}")

    def add_contact(self, name, phone, email=None, address=None, notes=None):
        """Add a new contact."""
        if name in self.contacts:
            print(f"[!] Contact '{name}' already exists! Use update to modify.")
            return False

        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address,
            "notes": notes,
            "created": "2026-02-08"
        }

        print(f"[OK] Added contact: {name}")
        self.save_contacts()
        return True

    def update_contact(self, name, **kwargs):
        """Update an existing contact."""
        if name not in self.contacts:
            print(f"⚠ Contact '{name}' not found!")
            return False

        for key, value in kwargs.items():
            if key in ["phone", "email", "address", "notes"]:
                self.contacts[name][key] = value

        print(f"[OK] Updated contact: {name}")
        self.save_contacts()
        return True

    def delete_contact(self, name):
        """Delete a contact."""
        if name not in self.contacts:
            print(f"⚠ Contact '{name}' not found!")
            return False

        del self.contacts[name]
        print(f"[OK] Deleted contact: {name}")
        self.save_contacts()
        return True

    def search_contact(self, query):
        """Search for contacts by name, phone, or email."""
        query_lower = query.lower()
        results = {}

        for name, info in self.contacts.items():
            if query_lower in name.lower():
                results[name] = info
                continue
            if info.get("phone") and query_lower in info["phone"].lower():
                results[name] = info
                continue
            if info.get("email") and query_lower in info["email"].lower():
                results[name] = info
                continue

        return results

    def display_contact(self, name):
        """Display detailed information for a contact."""
        if name not in self.contacts:
            print(f"⚠ Contact '{name}' not found!")
            return

        contact = self.contacts[name]
        print(f"\n{'=' * 50}")
        print(f"Contact: {name}")
        print("=" * 50)
        print(f"Phone:   {contact.get('phone', 'N/A')}")
        print(f"Email:   {contact.get('email', 'N/A')}")
        print(f"Address: {contact.get('address', 'N/A')}")
        print(f"Notes:   {contact.get('notes', 'N/A')}")
        print("=" * 50)

    def list_all_contacts(self):
        """Display all contacts in a formatted list."""
        if not self.contacts:
            print("No contacts in the book.")
            return

        print(f"\n{'=' * 60}")
        print(f"All Contacts ({len(self.contacts)} total)")
        print("=" * 60)

        for name in sorted(self.contacts.keys()):
            contact = self.contacts[name]
            phone = contact.get("phone", "N/A")
            email = contact.get("email", "N/A")
            print(f"{name:20} | {phone:15} | {email}")

        print("=" * 60)

    def get_statistics(self):
        """Display statistics about the contact book."""
        total = len(self.contacts)
        with_email = sum(1 for c in self.contacts.values() if c.get("email"))
        with_address = sum(1 for c in self.contacts.values() if c.get("address"))
        with_notes = sum(1 for c in self.contacts.values() if c.get("notes"))

        print(f"\n{'=' * 50}")
        print("Contact Book Statistics")
        print("=" * 50)
        print(f"Total contacts:      {total}")
        if total > 0:
            print(f"With email:          {with_email} ({with_email/total*100:.1f}%)")
            print(f"With address:        {with_address} ({with_address/total*100:.1f}%)")
            print(f"With notes:          {with_notes} ({with_notes/total*100:.1f}%)")
        else:
            print("With email:          N/A")
            print("With address:        N/A")
            print("With notes:          N/A")
        print("=" * 50)


def main():
    print("Contact Book Application (OOP)")
    print("=" * 60)

    book = ContactBook("my_contacts.json")
    print()

    print("1. Adding Contacts:")
    print("-" * 60)
    book.add_contact(
        "Alice Johnson",
        phone="555-0101",
        email="alice@email.com",
        address="123 Main St, San Francisco, CA",
        notes="College friend"
    )
    book.add_contact("Bob Smith", phone="555-0102", email="bob.smith@company.com")
    book.add_contact("Charlie Brown", phone="555-0103", notes="Met at conference")
    book.add_contact("Diana Prince", phone="555-0104", email="diana@example.com")
    print()

    print("2. Listing All Contacts:")
    print("-" * 60)
    book.list_all_contacts()
    print()

    print("3. Viewing Contact Details:")
    print("-" * 60)
    book.display_contact("Alice Johnson")
    print()

    print("4. Updating a Contact:")
    print("-" * 60)
    book.update_contact("Bob Smith", phone="555-9999", notes="Updated phone")
    book.display_contact("Bob Smith")
    print()

    print("5. Searching Contacts:")
    print("-" * 60)
    results = book.search_contact("alice")
    for name in results:
        print(f"  Found: {name} - {results[name]['phone']}")
    print()

    print("6. Contact Book Statistics:")
    print("-" * 60)
    book.get_statistics()
    print()

    print("7. Deleting a Contact:")
    print("-" * 60)
    book.delete_contact("Charlie Brown")
    book.list_all_contacts()

    print("\n" + "=" * 60)
    print("Summary: ContactBook class - CRUD, JSON persistence, search")


if __name__ == "__main__":
    main()
