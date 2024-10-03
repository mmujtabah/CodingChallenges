# Solution of Challenge "PalindromeString"

thestring = input("Enter a string to check if it is Palindrome or not: ")

if thestring[::-1] == thestring:
    print("Palindrome")
else:
    print("Not Palindrome")

# Explanation

# thestring[::-1] is used to reverse the string.
# [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
# Then we have used basic if statement to check whether both strings are equal.
