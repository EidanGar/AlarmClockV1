from time import *
from tkinter import *
from datetime import datetime
from datetime import *
import datetime
import time

def alarm_set():
    global day

    if int(hour_box.get()) < 0 or int(hour_box.get()) > 23:
        hour_box.config(bg="red")
        return

    if int(second_box.get()) < 0 or int(second_box.get()) > 59:
        second_box.config(bg="red")
        return

    if int(minute_box.get()) < 0 or int(minute_box.get()) > 59:
        minute_box.config(bg="red")
        return

    if day.get() not in option_list:
        days_menu.config(bg="red")
        return

    time_obj = time.localtime()
    current_weekday = strftime("%A", time_obj)

    if current_weekday == "Monday":
        current_weekday = 0
    elif current_weekday == "Tuesday":
        current_weekday = 1
    elif current_weekday == "Wednesday":
        current_weekday = 2
    elif current_weekday == "Thursday":
        current_weekday = 3
    elif current_weekday == "Friday":
        current_weekday = 4
    elif current_weekday == "Saturday":
        current_weekday = 5
    elif current_weekday == "Sunday":
        current_weekday = 6

    week_day = ""

    if day.get() == "Monday":
        week_day = 0
    elif day.get() == "Tuesday":
        week_day = 1
    elif day.get() == "Wednesday":
        week_day = 2
    elif day.get() == "Thursday":
        week_day = 3
    elif day.get() == "Friday":
        week_day = 4
    elif day.get() == "Saturday":
        week_day = 5
    elif day.get() == "Sunday":
        week_day = 6

    year = int(strftime("%Y"))
    month = int(strftime("%m"))
    current_date = int(strftime('%c').split()[2])
    hour = int(strftime("%H"))*10
    minute = int(strftime("%M"))*10
    seconds = int(strftime("%S"))*10

    current_time = (year, month, current_date, hour, minute, seconds, current_weekday)

    set_time = (year, month, 16, hour_box.get(), minute_box.get(), second_box.get(), week_day)

    days_box_label.grid_remove()
    days_menu.grid_remove()
    minute_label.grid_remove()
    minute_box.grid_remove()
    hour_label.grid_remove()
    hour_box.grid_remove()
    second_label.grid_remove()
    second_box.grid_remove()
    set_alarm.grid_remove()

    d = datetime.date(set_time[0], set_time[1], current_date)

    days_ahead = week_day - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_alarm = d + datetime.timedelta(days_ahead)
    days_remaining = d - next_alarm

    time_remaining.config(text=f"Time remaining: {abs(days_remaining.days)} days", font=("Arial", 20))
    time_remaining.grid()

    if current_time[0] == set_time[0]:
        if current_time[1] == set_time[1]:
            if current_time[3] == set_time[3]:
                if current_time[4] == set_time[4]:
                    if current_time[5] == set_time[5]:
                        if current_time[6] == set_time[6]:
                            time_remaining.config(text="It's time to wake up!", font=("Arial", 20))


# year - month - day - hour - min - sec - day of week -

def entry_disappear(): 
    global alarm_name

    alarm_label.config(text=alarm_name.get()[:10], font=("Arial", 20))
    alarm_label.grid(row=0, column=0, columnspan=2)
    
    alarm_name.grid_remove()

    submit_name.grid_remove()


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    date_string = strftime("%A, %B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()

# ------- TIMER ON TOP --------

time_frame = Frame(window, bg="black")
time_frame.grid()

day = StringVar()
day.set("Select day")

time_label = Label(time_frame, bg="black", fg="#00FF00", font=("Arial", 20))
time_label.grid(pady=5)

date_label = Label(time_frame, bg="black", fg="#00FF00", font=("Arial", 12))
date_label.grid(padx=10, pady=5)

# --------------------------------------------------

alarm_frame = Frame(window, highlightbackground = "black", 
                            highlightthickness = 2, bd=0)
alarm_frame.grid()

time_remaining = Label(alarm_frame)

alarm_name = Entry(alarm_frame, font=("Arial", 15), width=10)
alarm_name.grid(row=0, column=0, padx=2, pady=2)

submit_name = Button(alarm_frame, text="Submit", command=entry_disappear)
submit_name.grid(row=0, column=1)

alarm_label = Label(alarm_frame)

days_box_label = Label(alarm_frame, text="Day:", font=("Arial", 18))
days_box_label.grid(padx=2, pady=2, row=1, column=0)

option_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days_menu = OptionMenu(alarm_frame, day, *option_list)
days_menu.grid(padx=2, pady=2, row=1, column=1)

minute_label = Label(alarm_frame, text="Minutes:", font=("Arial", 18))
minute_label.grid(padx=2, pady=2, row=2, column=0)

minute_box = Spinbox(alarm_frame, from_=00, to=59, width=3, font=("Arial", 18))
minute_box.grid(padx=2, pady=2, row=2, column=1)

hour_label = Label(alarm_frame, text="Hour:", font=("Arial", 18))
hour_label.grid(padx=2, pady=2, row=3, column=0)

hour_box = Spinbox(alarm_frame, from_=00, to=23, width=3, font=("Arial", 18))
hour_box.grid(padx=2, pady=2, row=3, column=1)

second_label = Label(alarm_frame, text="Seconds:", font=("Arial", 18))
second_label.grid(padx=2, pady=2, row=4, column=0)

second_box = Spinbox(alarm_frame, from_=00, to=59, width=3, font=("Arial", 18))
second_box.grid(padx=2, pady=2, row=4, column=1)

set_alarm = Button(alarm_frame, text="Set Alarm", command=alarm_set)
set_alarm.grid(row=5, column=0,pady=10, columnspan=2)

update()

window.mainloop()