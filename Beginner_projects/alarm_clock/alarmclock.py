from datetime import datetime
from playsound import playsound
alarm_time = input("please enter time in format HH:MM:SS  :  ")

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
print("setting up alarm")
print(alarm_hour,alarm_min,alarm_sec)

while True:
    time_now = datetime.now()
    current_hour = time_now.strftime("%I")
    current_min = time_now.strftime("%M")
    current_sec = time_now.strftime("%S")
    if (alarm_hour == current_hour):
        if (alarm_min == current_min):
            if (alarm_sec == current_sec):
                print('its alarm time')
                playsound("audio.mp3")
                break


