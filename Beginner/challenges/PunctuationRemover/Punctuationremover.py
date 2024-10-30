def remove_punctuation():
    print("Welcome to Punctuation Remover.")
    user_input = input("Enter a string: ")
    
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_string = ""

    for char in user_input:
        if char not in punctuation_marks:
            cleaned_string += char

    print("String without punctuation:", cleaned_string)

remove_punctuation()
