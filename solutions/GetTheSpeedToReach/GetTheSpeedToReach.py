# Solution for Challenge "GetTheSpeedToReach"

print("Welcome to GetTheSpeedToReach Challenge. Select mode for measurement:\n\n")
print("\t 1) M/S Meter per second \n \t 2) KM/H Kilometer per hour\n")

choice = int(input("Enter the number of the item you want to choose: "))
# Takes choice as integer
 
# Initalized blank variables
distance = 0
time = 0
speed = 0
output_unit = ""

if(choice == 1): # Choice for m/s
    print("Selected Meter per second. \n")
    output_unit = "m/s"
    distance = float(input("Enter distance from your destination(meters) :"))
    time = float(input("Enter time in you want to reach there(seconds) :"))    
elif(choice == 2): # Choice for km/h
    print("Selected Kilometer per hour.")
    output_unit = "km/h"
    distance = float(input("Enter distance from your destination(kilometers) :"))
    time = float(input("Enter time in you want to reach there(hours) :"))    
else: # Error message
    print("WRONG CHOICE. EXITING... ")
    exit()

# S = vt
# v = S/t After arranging

speed = distance/time # formula

print(f"You need {speed:.1f} {output_unit} speed to reach your destination.")

# Added :.1f to the speed so it will only show 1 decimal digit.
