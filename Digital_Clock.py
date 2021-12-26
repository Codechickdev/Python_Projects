from tkinter import *
import time

app = Tk()

app.geometry('420x100')
app.title("Digital Clock")
app.resizable(0, 0)

label = Label(app, font=("Boulder", 68, 'bold'), fg="Green", bg="Black", bd=25)
label.grid(row=0, column=0)
label.pack()

def digital_clock():
    live_time = time.strftime("%H:%M:%S")
    label.config(text=live_time)
    label.after(200, digital_clock)

digital_clock()
app.mainloop()