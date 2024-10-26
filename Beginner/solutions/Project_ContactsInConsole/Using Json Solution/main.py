import json
import os

contactsFile = "contacts.json"
contactsJson = None

def load_contacts():
    global contactsJson
    with open(contactsFile,"r",encoding="UTF-8") as contactReader:
        contactsJson = json.load(contactReader)
    contactReader.close()
def refresh_contacts():
    print("Refreshing...")
    load_contacts()
    print("Refreshing Complete!")
    menu()

def create_Contact():
    name = input("Enter the name:")
    username = input("Enter the username:")
    contactExists = False
    for contact in contactsJson["contacts"]:
        if contact["username"] == username:
            print("Contact already exists.")
            contactExists = True
            break

    if contactExists == False:    
        email = input("Enter the email:")
        phoneNumber = input("Enter the phone number:")
        address = input("Enter the address:")
        template = {
            "name": name,
            "username": username,
            "email": email,
            "phoneNumber": phoneNumber,
            "address": address
        }
        contactsJson["contacts"].append(template)
        jsonFormat = json.dumps(contactsJson)
        with open(contactsFile,"w",encoding="UTF-8") as contactWriter:
            contactWriter.write(jsonFormat)
        contactWriter.close()
    else:
        print("Contact Already Exists.")
def edit_contact():
    global contactsJson
    username = input("Enter the username of the contact you want to edit: ")
    selectedContact = None
    isContactFound = False
    for contact in contactsJson["contacts"]:
        if contact["username"] == username:
            selectedContact = contact
            isContactFound = True
            break
    if isContactFound == False:
        print("No contact found with username '"+username+"'.")
    else:
        name = input("Enter the name:")
        usernameForStoring = input("Enter the username:")
        email = input("Enter the email:")
        phoneNumber = input("Enter the phone number:")
        address = input("Enter the address:")
        selectedContact["name"] = name
        selectedContact["username"] = usernameForStoring
        selectedContact["email"] = email
        selectedContact["phoneNumber"] = phoneNumber
        selectedContact["address"] = address

        print("Writing changes")
        jsonFormat = json.dumps(contactsJson)
        with open(contactsFile,"w",encoding="UTF-8") as contactWriter:
            contactWriter.write(jsonFormat)
        contactWriter.close()

def delete_contact():
    username = input("Enter the username of the contact you want to delete: ")
    selectedContact = None
    isContactFound = False
    for contact in contactsJson["contacts"]:
        if contact["username"] == username:
            selectedContact = contact
            isContactFound = True
            break
    if isContactFound == False:
        print("No contact found with username '"+username+"'.")
    else:
        confirmation = input(f"Do you want to delete the contact({contact['username']}) [y/N]: ")
        if confirmation.lower() == "y":
            contactsJson["contacts"].remove(selectedContact)
            jsonFormat = json.dumps(contactsJson)
            with open(contactsFile,"w",encoding="UTF-8") as contactWriter:
                contactWriter.write(jsonFormat)
            contactWriter.close()
        else:
            print("Delete operation cancelled!")
def printSeparator():
    print("####################################################")
def display_contacts():
    for contact in contactsJson["contacts"]:
        printSeparator()
        print(f"Name : {contact['name']}")
        print(f"Username : {contact['username']}")
        print(f"Email Address : {contact['email']}")
        print(f"Phone Number : {contact['phoneNumber']}")
        print(f"Address : {contact['address']}")
        printSeparator()


def clearScreen():
    input("Done?")
    os.system("clear")
    # use this for windows: os.system("cls")
def menu():
    print("Welcome to ContactsInConsole App! | Made by @alizaincodes")
    print("----------------------------------------------")
    print("Which operating you want to do?")
    print("1. Refresh Contacts")
    print("2. List Contacts")
    print("3. Create Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit the app")
    print("-----------------------------------------------")
    choice = int(input("Enter the choice number:"))
    if choice == 1:
        refresh_contacts()
        clearScreen()
    elif choice == 2:
        display_contacts()
        clearScreen()
    elif choice == 3:
        create_Contact()
        refresh_contacts()
        clearScreen()
    elif choice == 4:
        edit_contact()
        refresh_contacts()
        clearScreen()
    elif choice == 5:
        delete_contact()
        refresh_contacts()
        clearScreen()
    elif choice == 6:
        clearScreen()
        print("Thanks for using! Good Bye")
        exit()
    else:
        print("Invalid Choice Entered!")
    menu()

if __name__ == "__main__":
    print("Initializing...")
    load_contacts()
    menu()