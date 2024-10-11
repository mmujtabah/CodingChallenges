# Challenge : "SimpleAlarm"

Write a program which displays "Time is over" after the given amount of time.

This time is given in both seconds and minutes so your program should support both.

The timer program should also update the current timer such that it shows the remaining seconds.

# Example Output
```bash
(base) kali@theWarMachine:~/Documents/CodingChallenges/solutions/SimpleAlarm$ python3 SimpleAlarm.py 
Please choose a unit for timer: 
         1) Seconds
         2) Minutes
Enter the choice number : 1
Enter the time in seconds(do not use decimals): 25
Remaining Time : 25 seconds.
Remaining Time : 24 seconds.
Remaining Time : 23 seconds.
Remaining Time : 22 seconds.
Remaining Time : 21 seconds.
Remaining Time : 20 seconds.
Remaining Time : 19 seconds.
Remaining Time : 18 seconds.
Remaining Time : 17 seconds.
Remaining Time : 16 seconds.
Remaining Time : 15 seconds.
Remaining Time : 14 seconds.
Remaining Time : 13 seconds.
Remaining Time : 12 seconds.
Remaining Time : 11 seconds.
Remaining Time : 10 seconds.
Remaining Time : 9 seconds.
Remaining Time : 8 seconds.
Remaining Time : 7 seconds.
Remaining Time : 6 seconds.
Remaining Time : 5 seconds.
Remaining Time : 4 seconds.
Remaining Time : 3 seconds.
Remaining Time : 2 seconds.
Remaining Time : 1 seconds.
Time is over.
```

# Hints
- For **Javascript** Users, use `setInterval()` function to set a regular execution. And then use clear `clearInterval()` to clear that execution.
- For **Python** Users, use `time` module to use `sleep` function.
