import os # Importing OS for file reading

contacts = [] # Blank storage array for contacts

SPLITTER = "<%CONTACT_(Splitter)_CONSOLE%>"

def load_contacts() -> None:
    global contacts
    contacts = []
    allThingsInDirectory = os.listdir("Contacts")  
    allcontactfiles = []
    for object in allThingsInDirectory:
        thefullpath = os.path.join("Contacts/"+object)
        if os.path.isfile(thefullpath) and object.endswith(".consolecontact"):
            allcontactfiles.append(object)
    for contactfile in allcontactfiles:
        thepath = os.path.join("Contacts/"+contactfile)
        with open(thepath,"r",encoding="utf-8") as contactfilereader:
            rawData = str(contactfilereader.read())
        contactfilereader.close()
        splittedData = rawData.split(SPLITTER)
        contactTemplate = {
            "name" : splittedData[0],
            "username" : splittedData[1],
            "email" : splittedData[2],
            "phoneNumber" : splittedData[3],
            "address" : splittedData[4],
            "filePath":thepath
        }
        contacts.append(contactTemplate)

def refresh_contacts():
    print("------------------------")
    print("Refreshing Contact List...")
    load_contacts()
    
def display_contacts():
    for contact in contacts:
        print("---------------------------------------------------------------")
        print(f"Name : {contact['name']} ")
        print(f"Username : {contact['username']} ")
        print(f"Email : {contact['email']} ")
        print(f"Phone Number : {contact['phoneNumber']} ")
        print(f"Address : {contact['address']} ")
        print(f"File Path : {contact['filePath']} ")

def delete_contact():
    username = input("Enter the username of the contact you want to delete:")
    isContactFound = False
    for contact in contacts:
        if contact["username"] == username:
            isContactFound = True
            confirmation = input(f"Do you want to delete the contact({contact['filePath']}) [y/N]: ")
            if confirmation.lower() == "y":
                os.remove(contact['filePath'])
            else:
                print("Contact Delete Cancelled!")
                break
    if isContactFound == False:
        print(f"No Contact Found with given username : {username}")

def edit_contact():
    username = input("Enter the username of the contact you want to edit:")
    isContactFound = False
    for contact in contacts:
        if contact["username"] == username:
            isContactFound = True
            name = input(f"Enter the name({contact['name']}):")
            username = input(f"Enter the username({contact['username']}):")
            email = input(f"Enter the email({contact['email']}):")
            phoneNumber = input(f"Enter the phone number({contact['phoneNumber']}):")
            address = input(f"Enter the address({contact['address']}):")
            dataToWrite = name + SPLITTER + username + SPLITTER + email + SPLITTER + phoneNumber + SPLITTER + address
            generatedPath = os.path.join("Contacts/" + f"{username}.consolecontact")
            os.remove(contact["filePath"])
            with open(generatedPath,"w",encoding="utf-8") as contactwriter:
                contactwriter.write(dataToWrite)
            contactwriter.close()
            print(f"Contact '{username}' has been edited successfully at this path '{generatedPath}'.")
    if isContactFound == False:
        print(f"No Contact Found with given username : {username}")

    
def createContact():
    name = input("Enter the name:")
    username = input("Enter the username:")
    email = input("Enter the email:")
    phoneNumber = input("Enter the phone number:")
    address = input("Enter the address:")
    dataToWrite = name + SPLITTER + username + SPLITTER + email + SPLITTER + phoneNumber + SPLITTER + address
    generatedPath = os.path.join("Contacts/" + f"{username}.consolecontact")
    if os.path.exists(generatedPath):
        print(f"A Contact already exists there with file name : {generatedPath}")
    else:
        with open(generatedPath,"w",encoding="utf-8") as contactwriter:
            contactwriter.write(dataToWrite)
        contactwriter.close()
        print(f"Contact '{username}' has been saved successfully at this path '{generatedPath}'.")

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
        createContact()
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