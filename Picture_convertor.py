from tkinter import *
from tkinter import filedialog
from PIL import Image # pip install PIL-Tools

root = Tk()
root.title("Image Convertor")
can = Canvas(root, width=300, height=250, bg='purple', relief='raised')
can.pack()

lbl = Label(root, text='Image Converter', bg='purple', fg='White', font=('Arial', 20, 'bold'))
can.create_window(150, 60, window=lbl)


def get_png():
    global img
    import_file_path = filedialog.askopenfilename()
    img = Image.open(import_file_path)


browse_png = Button(root, text='Browse .png file', command=get_png, bg="royalblue", fg="white", font=('Arial', 12, "bold"))
can.create_window(150, 130, window=browse_png)


def convert():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    img.save(export_file_path)


save_btn = Button(root, text='Convert PNG to JPG', command=convert, bg="royalblue", fg="white",font=('Arial', 12, "bold"))
can.create_window(150, 170, window=save_btn)

root.mainloop()
