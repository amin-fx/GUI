# Import essential modules
from tkinter import *
from tkinter import messagebox

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
convertor_options = OptionMenu(root, option_text, *["Fahrenheit to celsius", "Kg to other weights"])
convertor_options.grid(row=2, column=3)

answer_lbl = Label(root, text="", font=("Arial", 10, 'bold'))
answer_lbl.grid(column=2, row=4)


# Temperature convertor formula = 5 * (f-32) / 9 Or c*9/5 + 32
def convertor():
    try:
        if option_text.get() == "Fahrenheit to celsius":
            temp = float(input.get())
            temp_c = 5 * (temp - 32) / 9
            answer_lbl["text"] = f"Temperature in celcius : {str(int(temp_c))}"
            input.delete(0, END)

        elif option_text.get() == "Kg to other weights":
            answer_lbl["text"] = ""
            kg_weight = float(input.get())
            gram_weight = kg_weight * 1000
            tone_weight = kg_weight/1000
            pound_weight = kg_weight * 2.2046
            ounce_weight = kg_weight * 35.274
            gram_lbl = Label(root, text="Gram")
            tone_lbl = Label(root, text="Tone")
            pound_lbl = Label(root, text="Pound")
            ounce_lbl = Label(root, text="Ounce")
            gram_lbl.grid(column=1, row=5)
            tone_lbl.grid(column=2, row=5)
            pound_lbl.grid(column=3, row=5)
            ounce_lbl.grid(column=4, row=5)
            gram_txt = Text(root, width=30, height=5)
            tone_txt = Text(root, width=30, height=5)
            pound_txt = Text(root, width=30, height=5)
            ounce_txt = Text(root, width=30, height=5)
            gram_txt.insert(END, str(gram_weight))
            tone_txt.insert(END, str(tone_weight))
            pound_txt.insert(END, str(pound_weight))
            ounce_txt.insert(END, str(ounce_weight))
            gram_txt.grid(column=1, row=6)
            tone_txt.grid(column=2, row=6)
            pound_txt.grid(column=3, row=6)
            ounce_txt.grid(column=4, row=6)
            input.delete(0, END)

        else:
            answer_lbl["text"] = "Invalid option"

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid value")


btn = Button(root, text="Convert", command=convertor, bg="skyblue", fg="white")
btn.grid(row=2, column=4, padx=10)
# Running window
root.mainloop()
