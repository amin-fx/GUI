from tkinter import *
import os
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background="#0f1a2b")
root.resizable(width=False, height=False)

mixer.init()


def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                play_list.insert(END, song)


def play_music():
    music_name = play_list.get(ACTIVE)
    mixer.music.load(music_name)
    mixer.music.play()


img_icon = PhotoImage(file="pic/logo.png")
root.iconphoto(False, img_icon)

top = PhotoImage(file="pic/top.png")
Label(root, image=top, background="#0f1a2b").pack()

logo = PhotoImage(file="pic/logo.png")
Label(root, image=logo, background="#0f1a2b").place(x=70, y=115)

btn_play = PhotoImage(file="pic/play.png")
Button(root, image=btn_play, background="#0f1a2b", bd=0, command=play_music).place(x=100, y=400)

btn_stop = PhotoImage(file="pic/stop.png")
Button(root, image=btn_stop, background="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

btn_resume = PhotoImage(file="pic/resume.png")
Button(root, image=btn_resume, background="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

btn_pause = PhotoImage(file="pic/pause.png")
Button(root, image=btn_pause, background="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200, y=500)

menu = PhotoImage(file="pic/menu.png")
Label(root, image=menu, background="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=330, y=350, width=560, height=200)

Button(root, text="Open folder", width=15, height=2, font=("Arial", 10, "bold"), fg="black", bg="#21b3de"
       , command=add_music).place(x=330, y=300)

scroll = Scrollbar(frame_music)
play_list = Listbox(frame_music, width=100, font=("Verdana", 10, "bold"), bg="#000000", fg="white"
                    , selectbackground="lightblue", cursor="hand2", border=0, yscrollcommand=scroll.set)

scroll.config(command=play_list.yview)
scroll.pack(side=RIGHT, fill=Y)
play_list.pack(side=LEFT, fill=BOTH)
root.mainloop()
