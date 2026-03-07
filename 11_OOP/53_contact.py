# 26_simple_contact.py - Simple class: Contact
# Florentino Baez - ITSE-1002

class Contact:
    """Class with several attributes."""
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def info(self):
        return f"{self.name} | {self.email} | {self.phone}"

# Short list of contacts
contacts = [
    Contact("John Doe", "john@email.com", "555-1234"),
    Contact("Jane Smith", "jane@email.com", "555-5678"),
]

# Usage
for c in contacts:
    print(c.info())
