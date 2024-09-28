import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts, name, phone, email):
    """Add a new contact to the contact book."""
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def remove_contact(contacts, name):
    """Remove a contact from the contact book."""
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' removed.")
    else:
        print(f"Contact '{name}' not found.")

def view_contacts(contacts):
    """View all contacts in the contact book."""
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact Book:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        print()

if __name__ == "__main__":
    contacts = load_contacts()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to remove: ")
            remove_contact(contacts, name)
        elif choice == '3':
            view_contacts(contacts)
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option, please try again.")
