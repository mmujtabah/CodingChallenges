# Take user input for the number
num = int(input("Enter the number: "))

# Assume the number is prime unless proven otherwise
is_prime = True

# Loop through all numbers from 2 to one less than the input number
# If any number divides the input number evenly, it's not prime
for i in range(2, num):
    if num % i == 0:  # If there's no remainder, num is divisible by i
        is_prime = False  # Mark the number as not prime
        break  # Exit the loop since we found a divisor

# Check if the number is 1, which is neither prime nor composite
if is_prime == False:
    print("Not Prime")  # If a divisor was found, the number is not prime
elif num == 1:
    print("1 is neither prime nor composite")  # Special case for 1
else:
    print("Prime")  # If no divisors were found, the number is prime
