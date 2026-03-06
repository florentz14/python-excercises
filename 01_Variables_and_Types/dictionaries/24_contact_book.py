# -------------------------------------------------
# File Name: 24_contact_book.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Contact Book Application.
#              Creates a full CRUD contact manager backed by JSON
#              file storage. Features include adding, updating,
#              deleting, searching by name/phone/email, listing
#              contacts, and displaying statistics.
# -------------------------------------------------

"""
Exercise 8: Contact Book Application
This exercise creates a full-featured contact management system.
Demonstrates practical application of dictionaries with CRUD operations.
"""

import json
import os


class ContactBook:
    """
    A contact book manager using dictionaries.
    """
    
    def __init__(self, filename="contacts.json"):
        """
        Initialize contact book.
        
        Args:
            filename: JSON file to store contacts
        """
        self.filename = filename
        self.contacts = {}
        self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from JSON file."""
        # Construct full file path (hardcoded path - do not change)
        filepath = f"/home/claude/dictionary_exercises/{self.filename}"
        if os.path.exists(filepath):
            try:
                # Read and parse JSON file
                with open(filepath, 'r') as f:
                    self.contacts = json.load(f)
                print(f"✓ Loaded {len(self.contacts)} contacts from {self.filename}")
            except json.JSONDecodeError:
                # Handle corrupted JSON file
                print(f"⚠ Error reading {self.filename}, starting fresh")
                self.contacts = {}
        else:
            # File doesn't exist yet, start with empty dictionary
            print(f"No existing contact file found, starting fresh")
    
    def save_contacts(self):
        """Save contacts to JSON file."""
        # Construct full file path (hardcoded path - do not change)
        filepath = f"/home/claude/dictionary_exercises/{self.filename}"
        # Write contacts dictionary to JSON file with indentation
        with open(filepath, 'w') as f:
            json.dump(self.contacts, f, indent=2)
        print(f"✓ Saved {len(self.contacts)} contacts to {self.filename}")
    
    def add_contact(self, name, phone, email=None, address=None, notes=None):
        """
        Add a new contact.
        
        Args:
            name: Contact name (used as key)
            phone: Phone number
            email: Email address (optional)
            address: Physical address (optional)
            notes: Additional notes (optional)
        """
        # Check if contact already exists
        if name in self.contacts:
            print(f"⚠ Contact '{name}' already exists! Use update to modify.")
            return False
        
        # Create new contact entry in dictionary
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address,
            "notes": notes,
            "created": "2026-02-08"  # Could use datetime for dynamic date
        }
        
        print(f"✓ Added contact: {name}")
        self.save_contacts()
        return True
    
    def update_contact(self, name, **kwargs):
        """
        Update an existing contact.
        
        Args:
            name: Contact name
            **kwargs: Fields to update (phone, email, address, notes)
        """
        if name not in self.contacts:
            print(f"⚠ Contact '{name}' not found!")
            return False
        
        # Update only provided fields
        for key, value in kwargs.items():
            if key in ["phone", "email", "address", "notes"]:
                self.contacts[name][key] = value
        
        print(f"✓ Updated contact: {name}")
        self.save_contacts()
        return True
    
    def delete_contact(self, name):
        """
        Delete a contact.
        
        Args:
            name: Contact name to delete
        """
        if name not in self.contacts:
            print(f"⚠ Contact '{name}' not found!")
            return False
        
        del self.contacts[name]
        print(f"✓ Deleted contact: {name}")
        self.save_contacts()
        return True
    
    def search_contact(self, query):
        """
        Search for contacts by name, phone, or email.
        
        Args:
            query: Search query string
        
        Returns:
            Dictionary of matching contacts
        """
        # Convert query to lowercase for case-insensitive search
        query_lower = query.lower()
        results = {}
        
        # Iterate through all contacts and search in multiple fields
        for name, info in self.contacts.items():
            # Search in contact name
            if query_lower in name.lower():
                results[name] = info
                continue
            
            # Search in phone number (if exists)
            if info.get("phone") and query_lower in info["phone"].lower():
                results[name] = info
                continue
            
            # Search in email address (if exists)
            if info.get("email") and query_lower in info["email"].lower():
                results[name] = info
                continue
        
        return results
    
    def display_contact(self, name):
        """
        Display detailed information for a contact.
        
        Args:
            name: Contact name
        """
        if name not in self.contacts:
            print(f"⚠ Contact '{name}' not found!")
            return
        
        # Retrieve contact information and display formatted details
        contact = self.contacts[name]
        print(f"\n{'=' * 50}")
        print(f"Contact: {name}")
        print("=" * 50)
        # Use get() with default 'N/A' for optional fields
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
        
        # Sort contacts alphabetically
        for name in sorted(self.contacts.keys()):
            contact = self.contacts[name]
            phone = contact.get('phone', 'N/A')
            email = contact.get('email', 'N/A')
            print(f"{name:20} | {phone:15} | {email}")
        
        print("=" * 60)
    
    def get_statistics(self):
        """Display statistics about the contact book."""
        # Calculate total number of contacts
        total = len(self.contacts)
        # Count contacts with optional fields using generator expression
        with_email = sum(1 for c in self.contacts.values() if c.get('email'))
        with_address = sum(1 for c in self.contacts.values() if c.get('address'))
        with_notes = sum(1 for c in self.contacts.values() if c.get('notes'))
        
        print(f"\n{'=' * 50}")
        print("Contact Book Statistics")
        print("=" * 50)
        print(f"Total contacts:      {total}")
        print(f"With email:          {with_email} ({with_email/total*100:.1f}%)" if total > 0 else "N/A")
        print(f"With address:        {with_address} ({with_address/total*100:.1f}%)" if total > 0 else "N/A")
        print(f"With notes:          {with_notes} ({with_notes/total*100:.1f}%)" if total > 0 else "N/A")
        print("=" * 50)


def main():
    print("Exercise 8: Contact Book Application")
    print("=" * 60)
    
    # Initialize contact book with JSON file storage
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
    book.add_contact(
        "Bob Smith",
        phone="555-0102",
        email="bob.smith@company.com",
        address="456 Oak Ave, Los Angeles, CA"
    )
    book.add_contact(
        "Charlie Brown",
        phone="555-0103",
        notes="Met at conference"
    )
    book.add_contact(
        "Diana Prince",
        phone="555-0104",
        email="diana@example.com",
        address="789 Pine Rd, Seattle, WA",
        notes="Work colleague"
    )
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
    book.update_contact(
        "Bob Smith",
        phone="555-9999",
        notes="Updated phone number"
    )
    book.display_contact("Bob Smith")
    print()
    
    print("5. Searching Contacts:")
    print("-" * 60)
    # Search by name (case-insensitive)
    print("Search for 'alice':")
    results = book.search_contact("alice")
    for name in results:
        print(f"  Found: {name} - {results[name]['phone']}")
    
    # Search by phone number
    print("\nSearch for '555-0104':")
    results = book.search_contact("555-0104")
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
    print("Summary:")
    print("  - Built complete CRUD application with dictionaries")
    print("  - Implemented persistent storage with JSON")
    print("  - Added search and statistics features")
    print("  - Demonstrated real-world dictionary usage")
    print("  - Contact data saved to my_contacts.json")


if __name__ == "__main__":
    main()
