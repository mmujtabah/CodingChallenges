import os

CONTACTS_DIR = "contacts"
SPLITTER = "<||>"

os.makedirs(CONTACTS_DIR, exist_ok=True)

def get_contact_filepath(name):
    return os.path.join(CONTACTS_DIR, f"{name}.consolecontact")

def create_contact():
    name = input("Enter contact name: ").strip()
    if os.path.exists(get_contact_filepath(name)):
        print("Contact with this name already exists!")
        return
    
    username = input("Enter username: ").strip()
    email = input("Enter email address: ").strip()
    phone = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()
    
    contact_data = f"{name}{SPLITTER}{username}{SPLITTER}{email}{SPLITTER}{phone}{SPLITTER}{address}"
    with open(get_contact_filepath(name), "w") as file:
        file.write(contact_data)
    
    print("Contact created successfully!")

def view_contacts():
    contacts = os.listdir(CONTACTS_DIR)
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContacts List:")
    for contact_file in contacts:
        if contact_file.endswith(".consolecontact"):
            with open(os.path.join(CONTACTS_DIR, contact_file), "r") as file:
                data = file.read().split(SPLITTER)
                print(f"Name: {data[0]}, Username: {data[1]}, Email: {data[2]}, Phone: {data[3]}, Address: {data[4]}")
    print()

def edit_contact():
    name = input("Enter the name of the contact to edit: ").strip()
    filepath = get_contact_filepath(name)
    if not os.path.exists(filepath):
        print("Contact not found.")
        return
    
    with open(filepath, "r") as file:
        data = file.read().split(SPLITTER)
    
    print(f"Current Information - Name: {data[0]}, Username: {data[1]}, Email: {data[2]}, Phone: {data[3]}, Address: {data[4]}")
    
    username = input("Enter new username (leave blank to keep current): ").strip() or data[1]
    email = input("Enter new email (leave blank to keep current): ").strip() or data[2]
    phone = input("Enter new phone (leave blank to keep current): ").strip() or data[3]
    address = input("Enter new address (leave blank to keep current): ").strip() or data[4]
    
    updated_data = f"{name}{SPLITTER}{username}{SPLITTER}{email}{SPLITTER}{phone}{SPLITTER}{address}"
    with open(filepath, "w") as file:
        file.write(updated_data)
    
    print("Contact updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    filepath = get_contact_filepath(name)
    if os.path.exists(filepath):
        os.remove(filepath)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def clear_contacts():
    for contact_file in os.listdir(CONTACTS_DIR):
        if contact_file.endswith(".consolecontact"):
            os.remove(os.path.join(CONTACTS_DIR, contact_file))
    print("All contacts have been deleted.")

def main():
    while True:
        print("\n--- ContactsInConsole ---")
        print("1. Create Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Clear All Contacts")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            create_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            clear_contacts()
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
