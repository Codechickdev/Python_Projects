from datetime import datetime
from tkinter import messagebox

alarm_time = input("Enter the alarm time:HH:MM:SS : ")

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_min == current_min):
                if(alarm_sec == current_second):
                    messagebox.showinfo("Wake up, Time's up")
                    break