import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time Counter")

hour = StringVar()
minute = StringVar()
seconds = StringVar()

hour.set("00")
minute.set("00")
seconds.set("00")

hour_entry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hour_entry.place(x=80, y=20)

minute_entry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minute_entry.place(x=130, y=20)

seconds_entry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=seconds)
seconds_entry.place(x=180, y=20)

def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(seconds.get())
    except:
        print("Please input the right value: ")
    
    while temp >- 1:
        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        seconds.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up ")
        
        temp -= 1

btn = Button(root, text="Set Time Countdown", bd='5', command=submit)
btn.place(x=70, y=120)

root.mainloop()