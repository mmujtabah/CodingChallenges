# Challenge(Project) Details : ContactsInConsole

Create a project that is an console based application.
It has ability to:
- Create Contacts
- View Contacts
- Edit Contacts
- Delete Contacts

It is a basic project. 

## RESTRICTIONS:
- You cannot use any kind of database.
- You have only two options:
  - Use JSON to manage the Contacts
  - Use Files to manage the Contacts

# Example Output 


https://github.com/user-attachments/assets/cbbbe44f-5f39-4427-a999-79c1e78c5096




# Hints
- Make a directory named `contacts` in the project main folder.
- Then make contacts with a file having a unique extension such as `.consolecontact`. So that other files do not conflict with it.
- Make a struction of a file such that you can split the data in meaningful information.
  ```
  Ali Zain<SPLITTER>alizaincodes<SPLITTER>alizain.dev@proton.me<SPLITTER>+92 3084319725<SPLITTER>New York
  ```
  When you will split using "<SPLITTER>" you can get: 
  ```
  ["Ali Zain","alizaincodes","alizain.dev@proton.me","+92 3084319725","New York"]
  ```
  Which you can use in turn: 
  ```
  ["Name","Username","Email","Phone Number","Address"]
  ```
- Make such a splitter that it works even the words have those letters splitter have.
  Such that if the user has `<SPLITTER>` in his name or anything. It will result in broken reading of contact.
