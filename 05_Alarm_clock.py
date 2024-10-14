# Concepts: Datetime module, Loops
#Description: Create a basic alarm clock that takes the current time 
#and alerts the user when a specific time is reached.

from datetime import datetime
import time

def alarm_clock(alarm_time):
    print(f'Setting alarm for {alarm_time}')

    while True:
        #Getting current time 
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current time:",current_time)

        #check alarm time equals to current time 
        if current_time == alarm_time:
            print("Wake Up!! Time to get up!")
            break

        #sleep for 1 second before checking again 
        time.sleep(1)

if __name__== "__main__":
    #set the alarm time in HH:MM:SS format
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")

    #call the alarm clock function 
    alarm_clock(alarm_time)


