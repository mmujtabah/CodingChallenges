# Challenge "GetTheSpeedToReach"

Write a program which gets the distance of the user's destination and the time in which the user wants to reach there.
The program will use Distance-Speed-Time formula to get the speed for reaching the destination in time.

Formula: `S = vt` 
where:
- S is the distance
- v is the Speed/Velocity
- t is the time

The program should have two modes for measurement:
- `m/s Meter per second` : Distance and Time will be taken in meters and seconds respectively.
- `km/h Kilometer per hour` : Distance and Time will be taken in kilo meters and hours respectively.

Adjust the formula yourself to get the required speed/velocity which is needed to cover the distance in given time.

# Example Output 

For Meter per second: 

```bash
(base) kali@theWarMachine:~/Documents/CodingChallenges/solutions/GetTheSpeedToReach$ python3 GetTheSpeedToReach.py 
Welcome to GetTheSpeedToReach Challenge. Select mode for measurement:


         1) M/S Meter per second 
         2) KM/H Kilometer per hour

Enter the number of the item you want to choose: 1
Selected Meter per second. 

Enter distance from your destination(meters) :134
Enter time in you want to reach there(seconds) :60
You need 2.2 m/s speed to reach your destination.
```

For Kilometer per hour: 

```bash
(base) kali@theWarMachine:~/Documents/CodingChallenges/solutions/GetTheSpeedToReach$ python3 GetTheSpeedToReach.py 
Welcome to GetTheSpeedToReach Challenge. Select mode for measurement:


         1) M/S Meter per second 
         2) KM/H Kilometer per hour

Enter the number of the item you want to choose: 2
Selected Kilometer per hour.
Enter distance from your destination(kilometers) :12.5
Enter time in you want to reach there(hours) :1.3
You need 9.6 km/h speed to reach your destination.
```

For error message:
```
(base) kali@theWarMachine:~/Documents/CodingChallenges-Fork/CodingChallenges/solutions/GetTheSpeedToReach$ python3 GetTheSpeedToReach.py 
Welcome to GetTheSpeedToReach Challenge. Select mode for measurement:


         1) M/S Meter per second 
         2) KM/H Kilometer per hour

Enter the number of the item you want to choose: 3
WRONG CHOICE. EXITING... 
```