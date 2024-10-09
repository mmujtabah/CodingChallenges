import os,time 
# os module for interacting with CLI
# time module for interacting with time(for frames fps)

text = "Hello World!" # Text we want to show
while True: # Infinite Execution of Program
    for i in range(-1,len(text)): # Loops through each letter of text
        print(text[:i+1]) 
        # Gets the position of current letter and increases it by one and then prints the letters of text to index.
        time.sleep(0.2)
        # Stops execution for 0.2 Seconds. If removed, the animation will be too fast to be seen.
        os.system("clear")
        # Clears the Terminal/Console each time. So next frame should be rendered with only one text.