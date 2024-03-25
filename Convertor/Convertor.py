# Import essential modules
from tkinter import *

# Define a window
root = Tk()
root.title("Temperature convertor")
root.minsize(500, 300)
root.configure(padx=50, pady=50)

lbl = Label(root, text="Convert from Fahrenheit to Celsius", font=("Arial", 25, 'bold'))
lbl.grid(column=2, row=0)
lbl.config(pady=10)

input = Entry(root)
input.grid(row=2, column=2)

answer_lbl = Label(root, text="", font=("Arial", 10, 'bold'))
answer_lbl.grid(column=2, row=4)


# Temperature convertor formula = 5 * (f-32) / 9 Or c*9/5 + 32
def temp_convertor():
    temp = float(input.get())
    temp_c = 5 * (temp - 32) / 9
    answer_lbl["text"] = f"Temperature in celcius : {str(int(temp_c))}"
    input.delete(0, END)


btn = Button(root, text="Convert", command=temp_convertor)
btn.grid(row=2, column=3, padx=10)
# Running window
root.mainloop()
