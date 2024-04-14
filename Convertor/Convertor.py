# Import essential modules
from tkinter import *
from tkinter import messagebox
# import cx_Freeze

# Define a window
root = Tk()
root.title("Convertor")
root.minsize(500, 300)
root.configure(padx=50, pady=50)

lbl = Label(root, text="Welcome to Convertor", font=("Arial", 25, 'bold'))
lbl.grid(column=2, row=0)
lbl.config(pady=10)

input = Entry(root)
input.grid(row=2, column=2)

option_text = StringVar()
option_text.set("Select an option")
convertor_options = OptionMenu(root, option_text, *["Fahrenheit to celsius", "Kg to other weights", "Feet to meter"])
convertor_options.grid(row=2, column=3)

answer_lbl = Label(root, text="", font=("Arial", 10, 'bold'))
answer_lbl.grid(column=2, row=4)

counter = 0


# Temperature convertor formula = 5 * (f-32) / 9 Or c*9/5 + 32
def convertor():
    global counter

    try:
        if counter == 0:
            global gram_lbl, tone_lbl, pound_lbl, ounce_lbl
            gram_lbl = Label(root, text="Gram")
            tone_lbl = Label(root, text="Tone")
            pound_lbl = Label(root, text="Pound")
            ounce_lbl = Label(root, text="Ounce")

            global gram_txt, tone_txt, pound_txt, ounce_txt
            gram_txt = Text(root, width=30, height=5)
            tone_txt = Text(root, width=30, height=5)
            pound_txt = Text(root, width=30, height=5)
            ounce_txt = Text(root, width=30, height=5)
            # print(f" counter = {counter} in main ")

        if option_text.get() == "Fahrenheit to celsius":
            temp = float(input.get())
            temp_c = 5 * (temp - 32) / 9
            answer_lbl["text"] = f"Temperature in celcius : {str(int(temp_c))}"
            input.delete(0, END)
            gram_lbl.destroy()
            gram_txt.destroy()
            tone_lbl.destroy()
            tone_txt.destroy()
            pound_lbl.destroy()
            pound_txt.destroy()
            ounce_lbl.destroy()
            ounce_txt.destroy()

            counter = 0
            # print(f" counter = {counter} in C -> F ")

        elif option_text.get() == "Feet to meter":
            feet_input = float(input.get())
            meter = (feet_input * 0.3084)
            answer_lbl["text"] = f"Height in meter : {str(meter)}"
            input.delete(0, END)
            gram_lbl.destroy()
            gram_txt.destroy()
            tone_lbl.destroy()
            tone_txt.destroy()
            pound_lbl.destroy()
            pound_txt.destroy()
            ounce_lbl.destroy()
            ounce_txt.destroy()

            counter = 0

        elif option_text.get() == "Kg to other weights":
            kg_weight = float(input.get())
            answer_lbl["text"] = f"Converting {kg_weight} KG :"
            gram_weight = kg_weight * 1000
            tone_weight = kg_weight/1000
            pound_weight = kg_weight * 2.2046
            ounce_weight = kg_weight * 35.274
            gram_lbl.grid(column=1, row=5)
            tone_lbl.grid(column=2, row=5)
            pound_lbl.grid(column=3, row=5)
            ounce_lbl.grid(column=4, row=5)
            gram_txt.delete(1.0, END)
            gram_txt.insert(END, str(gram_weight))
            gram_txt.config(state=DISABLED)
            tone_txt.delete(1.0, END)
            tone_txt.insert(END, str(tone_weight))
            tone_txt.config(state=DISABLED)
            pound_txt.delete(1.0, END)
            pound_txt.insert(END, str(pound_weight))
            pound_txt.config(state=DISABLED)
            ounce_txt.delete(1.0, END)
            ounce_txt.insert(END, str(ounce_weight))
            ounce_txt.config(state=DISABLED)
            gram_txt.grid(column=1, row=6)
            tone_txt.grid(column=2, row=6)
            pound_txt.grid(column=3, row=6)
            ounce_txt.grid(column=4, row=6)
            input.delete(0, END)
            counter += 1
            # print(f" counter = {counter} in KG ")

        else:
            answer_lbl["text"] = "Invalid option"

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid value")


btn = Button(root, text="Convert", command=convertor, bg="skyblue", fg="white")
btn.grid(row=2, column=4, padx=10)
# Running window
root.mainloop()
