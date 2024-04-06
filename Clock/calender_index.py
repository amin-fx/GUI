from tkinter import *
import calendar

root = Tk()
root.geometry("400x300")
root.title("Calender")
root.resizable(False, False)


def show():
    m = int(month.get())
    y = int(year.get())

    output = calendar.month(y, m)
    cal.insert(END, str(output))


def clear():
    cal.delete(1.0, END)


def exit():
    root.destroy()


title = Label(root, text="Simple Calender App", font=("Verdana", 18, "bold"))
title.place(x=40, y=10)

month_lbl = Label(root, text="Month", font=("Verdana", 10, "bold"))
month_lbl.place(x=70, y=80)

month = Spinbox(root, from_=1, to=12, width=5)
month.place(x=140, y=80)

year_lbl = Label(root, text="Year", font=("Verdana", 10, "bold"))
year_lbl.place(x=210, y=80)

year = Spinbox(root, from_=2020, to=2500, width=8)
year.place(x=260, y=80)

cal = Text(root, width=35, height=5, relief=RIDGE, borderwidth=2)
cal.place(x=70, y=110)

btn = Button(root, text="Show!", font=("Verdana", 10, "bold"), relief=RIDGE, borderwidth=2, bg="SkyBlue", command=show)
btn.place(x=140, y=200)

btn_clear = Button(root, text="Clear!", font=("Verdana", 10, "bold"), bg="lime", command=clear)
btn_clear.place(x=210, y=200)

btn_exit = Button(root, text="Exit!", font=("Verdana", 10, "bold"), bg="red", command=exit)
btn_exit.place(x=280, y=200)

root.mainloop()
