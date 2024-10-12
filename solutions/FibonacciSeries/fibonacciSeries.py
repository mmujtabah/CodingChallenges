# Fibonacci series generator
# This program takes a number as input and generates the Fibonacci series up to that number of terms.

# Initialize the first two terms of the Fibonacci series
first_term = 0
second_term = 1

# Get the number of terms from the user
num = int(input("Enter the number: "))

# Print the first term (0)
print(0, end=" ")

# Loop to calculate and print the next terms of the Fibonacci series
# The loop runs num-1 times because the first term (0) is already printed
for i in range(num - 1):
    # Calculate the next term as the sum of the previous two terms
    next_term = first_term + second_term
    # Print the next term
    print(next_term, end=" ")
    # Update the first and second terms for the next iteration
    first_term = second_term
    second_term = next_term
