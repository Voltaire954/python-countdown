# import time #BUILT IN PYTHON MODULE FOR TIME RELATED FUNCTIONS

# my_time= int(input("Enter the time in seconds: "))
# """
#     STORING THE INPUT FROM THE USER INTO THE MY_TIME VARIABLE, AFTER TYPE CHANGING INTO A INTEGER
# """
# for x in range (my_time,0,-1):#FOR LOOP THAT, LOOPS FROM 0 TO THE MY_TIME VARIABLE THE NEGATIVE 1. IS TO INCLUDE THE VARIABLE IN THE COUNTDOWN. WITHOUT IT THE LOOP WOULD START 1 BEFORE THE COUNTDOWN.
#     seconds = x % 60#MATH FOR SECONDS
#     minutes = int (x/60) %60 #MATH FOR MINUTES
#     hours = int(x / 3600)# MATH FOR HOURS
#     print(f"{hours:02} {minutes:02} {seconds:02}")# PRINTING THE COUNTDOWN
#     time.sleep(1)# GIVES A SECOND BEFORE THE NEXT PRINT

# print("TIMES UP!")# TIMES UP IS PRINTED WHEN COUNTDOWN IS DONE.
import time  # Built-in Python module for time-related functions, like sleep()

# Ask the user to enter the countdown time in seconds
my_time = int(input("Enter the time in seconds: "))
"""
Convert the user's input from a string to an integer and store it in 'my_time'.
This represents the total number of seconds for the countdown.
"""

# Loop from 'my_time' down to 1
for x in range(my_time, 0, -1):
    # Calculate hours, minutes, and seconds
    seconds = x % 60                   # Seconds remaining after removing full minutes
    minutes = (x // 60) % 60           # Minutes remaining after removing full hours
    hours = x // 3600                   # Total hours

    # Print the countdown in HH:MM:SS format with leading zeros
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    # Wait for 1 second before the next iteration
    time.sleep(1)

# Print final message when the countdown is complete
print("TIMES UP!")
