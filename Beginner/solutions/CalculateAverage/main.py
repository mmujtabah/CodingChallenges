numbers = []

print("Welcome to Average Calculator!")
print("Enter a blank string to stop giving numbers and calculate the average.")
print("-------------------------------------------------------------")
while True: 
    number = input(f"Enter number:")
    if number.replace(" ","") == "":
        break
    cleaned_string = ""
    for char in list(number):
        if char.isnumeric():
            cleaned_string += char
    if cleaned_string.replace(" ","") == "":
        break
    numbers.append(int(cleaned_string))

lenOfNumbers = len(numbers)
sumOfAllNumbers = sum(numbers)

average = sumOfAllNumbers / lenOfNumbers

print(f"The Average Value is: {average}")
