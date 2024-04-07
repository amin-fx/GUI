from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.title("Text editor")
# root.geometry("520x380")
# root.resizable(False, False)
root.rowconfigure(0, weight=1, minsize=800)
root.columnconfigure(1, weight=1, minsize=800)


def open_file():
    file_path = askopenfilename(filetypes=[('Text files', '*.txt'),  ("Docx files", "*.docx"), ("All Files", "*.*")])

    if not file_path:
        return

    txt_edit.delete(1.0, END)

    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
        txt_edit.insert(END, input_text)
    root.title(f"Text edited - {file_path}")


def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Docx files", "*.docx")
        ,("All Files", "*.*")])

    if not file_path:
        return

    with open(file_path, "w") as output_file:
        output_txt = txt_edit.get(1.0, END)
        output_file.write(output_txt)
    root.title(f"Text edited - {file_path}")


txt_edit = Text(root)
fr_buttons = Frame(root, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save as", command=save_file)

btn_open.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky=EW, padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky=NS)
txt_edit.grid(row=0, column=1, sticky=NSEW)

root.mainloop()
