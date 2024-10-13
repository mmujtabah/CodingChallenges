# Solution for Challenge "SimpleAlarm"

import time # Imports time module 

print("Please choose a unit for timer: ") # Asks user for choice of measurement
print("\t 1) Seconds")
print("\t 2) Minutes")

choice = int(input("Enter the choice number : ")) # Gets the choice number given by user.
# Uses int to convert it into integer format.

time_in_seconds = 0 # Blank variable initalization

if choice == 1: # If user choose seconds
    time_in_seconds = int(input("Enter the time in seconds(do not use decimals): "))
elif choice == 2: # If user choose minutes
    time_in_seconds = int(input("Enter the time in minutes(do not use decimals): ")) * 60
    # Multiplied it by 60 as 1 minute = 60 seconds
    # So it will be converted into seconds for our use.
else:
    print("WRONG CHOICE\n Exiting...")
    # Exits the program if wrong number is entered.
    exit()

for i in range(time_in_seconds): # Takes a range to given seconds
    print(f"Remaining Time : {time_in_seconds-i} seconds.")
    # time_in_seconds is the time given. "i" is the current time.
    # Time remaining will be total time - current time
    time.sleep(1) # Stops program execution for one second
    # Or adds a delay of 1 second to program.

print("Time is over.") # Displays message that time is over.