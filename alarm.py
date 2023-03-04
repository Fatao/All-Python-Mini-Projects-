import datetime
import time
import winsound

# get the time for the alarm
alarm_time = input("Enter the time for the alarm in HH:MM:SS format: ")

# convert the alarm time to datetime object
alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")

# loop until the current time matches the alarm time
while True:
    # get the current time
    current_time = datetime.datetime.now().time()

    # if the current time matches the alarm time, play the alarm sound and break the loop
    if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute and current_time.second == alarm_time.second:
        print("Time to wake up!")
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)  # play the alarm sound asynchronously
        break

    # wait for 1 second before checking the time again
    time.sleep(1)
