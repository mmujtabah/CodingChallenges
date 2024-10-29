# We can also use `string` module but we have to make everything from scratch.

print("Welcome to Punctuation Remover.")

string = input("Enter a string: ")

cleanedString = ""

for character in string:
    if (character.isalpha()) or (character.isdigit()) or (character.isspace()):
        # Explanation
        # isalpha() checks if the character is a letter.
        # isdigit() checks if it is a digit.
        # isspace() checks if it is whitespace.
        
        cleanedString += character

print(cleanedString)