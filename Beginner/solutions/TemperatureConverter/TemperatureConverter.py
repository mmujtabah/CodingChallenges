# Get the temperature unit from the user and convert it to uppercase for consistency
temp_unit = input("Convert from Celsius or Fahrenheit? Enter 'C' or 'F': ").upper()

# Check if the user wants to convert from Celsius to Fahrenheit
if temp_unit == 'C':
    # Prompt the user to enter the temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))
    # Convert Celsius to Fahrenheit using the formula
    ft = (celsius * 9/5) + 32
    # Display the converted temperature
    print(f"{celsius}°C is {ft}°F")

# Check if the user wants to convert from Fahrenheit to Celsius
elif temp_unit == 'F':
    # Prompt the user to enter the temperature in Fahrenheit
    ft = float(input("Enter temperature in Fahrenheit: "))
    # Convert Fahrenheit to Celsius using the formula
    celsius = (ft - 32) * 5/9
    # Display the converted temperature
    print(f"{ft}°F is {celsius}°C")

# Handle invalid input cases
else:
    print("Invalid input. Please enter 'C' or 'F'.")
