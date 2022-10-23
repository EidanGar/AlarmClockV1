import datetime as dt
import time
import tkinter as tk


def update():
    time_remaining = alarm_time - dt.datetime.now()
    time_remaining = time_remaining + dt.timedelta(seconds=1)

    month_label.config(text=f"Time remaining: {time_remaining}")

    window.after(1000, update())
    if time_remaining == 0:
        month_label.config(text="Time to wake up!")


def set_alarm():
    if time_now > alarm_time:
        print(time_now)
        print(alarm_time)
        month_label.config(text="Inavlid Time")
    else:
        day_label.grid_remove()
        day_input.grid_remove()
        hour_label.grid_remove()
        hour_input.grid_remove()
        minute_label.grid_remove()
        minute_input.grid_remove()
        update()


window = tk.Tk()
window.title("Alarm Clock")

time_now = dt.datetime.now()
year = time_now.year
month = time_now.month

alarm_frame = tk.Frame(window)
alarm_frame.grid()

A = 0
xpad = 8
ypad = 5

month_label = tk.Label(alarm_frame, text=time_now.strftime("%B"), font=("Arial", 17))
month_label.grid(columnspan=2)

day_label = tk.Label(alarm_frame, text="Day:")
day_label.grid(row=2, column=A)
day_input = tk.Spinbox(
    alarm_frame,
    from_=time_now.day,
    to=31,
    font=("Arial", 15),
    width=3,
    bg="#375A7D",
    fg="white",
)
day_input.grid(row=3, column=A, padx=xpad, pady=ypad)

hour_label = tk.Label(alarm_frame, text="Hour:")
hour_label.grid(row=2, column=A + 1)
hour_input = tk.Spinbox(
    alarm_frame,
    from_=time_now.hour,
    to=23,
    font=("Arial", 15),
    width=3,
    bg="#375A7D",
    fg="white",
)
hour_input.grid(row=3, column=A + 1, padx=xpad, pady=ypad)

minute_label = tk.Label(alarm_frame, text="Minute:")
minute_label.grid(row=2, column=A + 2)
minute_input = tk.Spinbox(
    alarm_frame,
    from_=time_now.minute,
    to=59,
    font=("Arial", 15),
    width=3,
    bg="#375A7D",
    fg="white",
)
minute_input.grid(row=3, column=A + 2, padx=xpad, pady=ypad)

set_alarm_button = tk.Button(alarm_frame, text="Set Alarm", command=set_alarm)
set_alarm_button.grid(columnspan=2, pady=10)

alarm_time = dt.datetime(
    year,
    month,
    int(day_input.get()),
    int(hour_input.get()),
    int(minute_input.get()) + 1,
)

window.mainloop()
