def calculate_average():
    print("Welcome to Average Calculator!")
    print("Enter numbers one by one. To finish, just press Enter without typing a number.")
    print("-------------------------------------------------------------")

    all_numbers = []

    while True:
        user_input = input("Enter number: ").strip()
        if user_input == "":
            break

        try:
            number = float(user_input)
            all_numbers.append(number)
        except ValueError:
            print("That's not a valid number! Please enter a valid number.")

    if all_numbers:
        total_sum = sum(all_numbers)
        count = len(all_numbers)
        average = total_sum / count
        print(f"The Average Value is: {average}")
    else:
        print("No numbers entered, so no average to calculate.")

calculate_average()
