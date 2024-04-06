from tkinter import Label, Tk
import time

root = Tk()
root.title("Digital clock")
root.geometry("420x150")
root.resizable(False, False)

text_font = ("Arial", 68, "bold")
background = "#f2e750"
foreground = "#363529"
border_width = 25

lbl = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width)
lbl.grid(row=0, column=1)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    lbl.config(text=time_live)
    lbl.after(1000, digital_clock) # 1000 ms = 1 s


digital_clock()
root.mainloop()
