# MUSIC PLAYER

# importing modules

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
from pygame import mixer
import os
import winsound
import webbrowser

# creating window

spotify="https://www.spotify.com/in/"

while True:
    f=5000
    dr=1000

    root=Tk()

    root.title("ALPHA.OS MUSIC v1.0.1  Powered By ALPHA.OS")
    root.iconbitmap(r'icon.ico')
    root.configure(bg="#ffecd2")
    image=Image.open("newicon.png")
    photo2=ImageTk.PhotoImage(image)

    def quit():
        exit()

    l1=Label(root,image=photo2,bg="#ffecd2")
    l1.pack(pady=30)
    l2=Label(root, text="powered by", bg="#ffecd2", fg="black")
    l3=Label(root,text = "ALPHA.OS", font="Cambria 20", height=1,width=24, bg="#ffecd2", fg="black")
    l3.pack(side=BOTTOM)
    l2.pack(side=BOTTOM)
    winsound.Beep(f,dr)
    messagebox.showinfo("ALPHA.OS", "ALPHA.OS INITIATNG... YOU CAN NOW CLOSE THIS WINDOW")
    root.mainloop()

    break

window = Tk()
#
# messagebox.showinfo("ALPHA.OS","WELCOME TO ALPHA.OS MUSICPLAYER v1.0.1 LOADING...")
image = Image.open("music.png")
photo = ImageTk.PhotoImage(image)
image2 = Image.open("osicon.png")
photo2 = ImageTk.PhotoImage(image2)
window.title("ALPHA.OS MUSIC v1.0.1  Powered By ALPHA.OS")
window.iconbitmap(r'icon.ico')

# messagebox.showinfo("ALPHA.OS","FOLLOW THE ONSCREEN INSTRUCTIONS")
messagebox.showinfo("ALPHA.OS","choose your theme dark/light in the shell")

print("choose theme below light/dark")
q = input("enter your choice")

if q == "light":
    window.configure(bg='white')
    messagebox.showinfo("ALPHA.OS","THEME SETTED TO LIGHT")
    # messagebox.showwarning("ALPHA.OS","THEME WILL NO LONGER BE CHANGED. RESTART PLAYER TO CHANGE THEME")
    print("MOVE TO THE MAIN WINDOW NOW")

elif q == "dark":
    window.configure(bg="grey")
    messagebox.showinfo("ALPHA.OS","THEME SETTED TO DARK")
    # messagebox.showwarning("ALPHA.OS", "THEME WILL NO LONGER BE CHANGED. RESTART PLAYER TO CHANGE THEME")
    print("MOVE TO THE MAIN WINDOW NOW")

else:
    messagebox.showerror("ALPHA.OS","INVALID CHOICE...!")
    # messagebox.showwarning("ALPHA.OS", "THEME WILL NO LONGER BE CHANGED. RESTART PLAYER TO CHANGE THEME")
    print("STARTING PLAYER IN DEFAULT")

fr=3000
dr=100

# initiating pygame

pygame.mixer.init()

# functions of player

t=0
def vibe():
    global t
    t=t+1
    if t == 1:
        winsound.Beep(fr, dr)
        song_name = song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
        # messagebox.showinfo("success", "music is now playing")

n = 0
def start_stop():

    global n
    n = n + 1
    if n == 1:
        winsound.Beep(fr, dr)
        song_name = song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.pause()
        # messagebox.showinfo("success","music is now pause")

    elif (n % 2) == 0:
        winsound.Beep(fr, dr)
        pygame.mixer.music.play()
        # messagebox.showinfo("success", "music now playing")

    elif (n % 2) != 0:
        winsound.Beep(fr, dr)
        pygame.mixer.music.pause()
        # messagebox.showinfo("success", "music now paused")


def spotify():
    winsound.Beep(fr, dr)
    messagebox.showinfo("ALPHA.OS", "MOVING TO SPOTIFY")
    messagebox.showinfo("ALPHA.OS", "INPUT THE LOCATION OF INSTALLED SPOTIFY FILE IN THE SHELL")
    x=input("enter spotify location here - ")
    os.startfile(x)

def Exit():
    winsound.Beep(fr, dr)
    window.quit()

def installation():
    winsound.Beep(fr, dr)
    messagebox.showinfo("ALPHA.OS", "SPOTIFY WEB REDIRECTING")
    webbrowser.open("http:/spotify.com")

m=0
def next():

    global m
    m = m + 1
    if m == 1:
        winsound.Beep(fr, dr)
        song_name = song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
        # messagebox.showinfo("success","music is now playing")

    elif (n % 2) == 0:
        winsound.Beep(fr, dr)
        song_name = song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
        # messagebox.showinfo("success","music is now playing")

    elif (n % 2) != 0:
        winsound.Beep(fr, dr)
        song_name = song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
        # messagebox.showinfo("success","music is now playing")

# placements

if q=="light":

    f3 = Frame(window, bg="white")
    f3.pack(side=TOP)

    l1 = Label(f3, image=photo, bg="white")
    l1.pack(pady=3,side=TOP)

else:

    f3 = Frame(window, bg="grey")
    f3.pack(side=TOP)

    l1 = Label(f3, image=photo,bg="grey")
    l1.pack(pady=3,side=TOP)

if q == "light":

    f1 = Frame(window, bg="#FFFFFF")
    f1.pack(side=LEFT, anchor=SW, pady=5, padx=5)

    f2 = Frame(window, bg="#FFFFFF")
    f2.pack(side=BOTTOM, anchor=SE)

    l2 = Label(f2, text="ALPHA.OS MUSIC v1.0.1", font="sitka 30 bold", bg="white")
    l2.pack(pady=10,side=TOP)

    song_list = os.listdir()
    song_listbox = StringVar(window)
    song_listbox.set("SELECT SONGS")
    Menu = OptionMenu(f1, song_listbox, *song_list)
    Menu.pack()

    b1 = Button(f1, text="START VIBING", width=75, bg='black', fg='white',activebackground="white",activeforeground="black", font="candara", command=vibe)
    b1.pack(pady=3)

    b2 = Button(f1, text="OPEN SPOTIFY WEB", width=75, bg='black', fg='green',activebackground="white",activeforeground="black", font="candara", command=installation)
    b2.pack()

    b4 = Button(f1, text="OPEN SPOTIFY", width=75, bg='black',activebackground="white",activeforeground="black", fg='green', font="candara", command=spotify)
    b4.pack(pady=3)

    b3 = Button(f1, text="Play / Pause", width=75, bg='black', fg='white',activebackground="white",activeforeground="black", font="candara", command=start_stop)
    b3.pack()

    b5 = Button(f1, text="Next Song", width=75, bg='black', fg='white', font="candara",activebackground="white",activeforeground="black", command=next)
    b5.pack(pady=3)

    b6 = Button(f1, text="Exit ALPHA.os music", width=75, bg='black', fg='red',activebackground="white",activeforeground="black", font="candara", command=Exit)
    b6.pack()

    l3 = Label(f2, text="powered by", bg="white")

    l4 = Label(f2, text="ALPHA.OS", font="calibri 20", bg="white")
    l4.pack(side=BOTTOM)
    l3.pack(side=BOTTOM)

    l5 = Label(f2, image=photo2, bg="white")
    l5.pack(side=BOTTOM)

else:

    f1 = Frame(window, bg="grey")
    f1.pack(side=LEFT, anchor=SW, pady=5, padx=5)

    f2 = Frame(window, bg="grey")
    f2.pack(side=BOTTOM, anchor=SE)

    l2 = Label(f2, text="ALPHA.OS MUSIC v1.0.1", font="sitka 30 bold", bg="grey",fg="black")
    l2.pack(side=TOP)

    song_list = os.listdir()
    song_listbox = StringVar(window)
    song_listbox.set("SELECT SONGS")
    Menu = OptionMenu(f1, song_listbox, *song_list)
    Menu.pack()

    b1 = Button(f1, text="START VIBING", width=75, bg='black', fg='white',activebackground="cyan",activeforeground="black", font="candara", command=vibe)
    b1.pack(pady=3)

    b2 = Button(f1, text="INSTALL SPOTIFY", width=75, bg='black', fg='green',activebackground="cyan",activeforeground="black", font="candara", command=installation)
    b2.pack()

    b4 = Button(f1, text="OPEN SPOTIFY", width=75, bg='black', fg='green',activebackground="cyan",activeforeground="black", font="candara", command=spotify)
    b4.pack(pady=3)

    b3 = Button(f1, text="Play / Pause", width=75, bg='black', fg='white',activebackground="cyan",activeforeground="black", font="candara", command=start_stop)
    b3.pack()

    b5 = Button(f1, text="Next Song", width=75, bg='black', activebackground="cyan",activeforeground="black",fg='white', font="candara", command=next)
    b5.pack(pady=3)

    b6 = Button(f1, text="Exit Alpha.os music", width=75, activebackground="cyan",activeforeground="black",bg='black', fg='red', font="times", command=Exit)
    b6.pack()

    l3 = Label(f2, text="powered by", bg="grey", fg="black")

    l4 = Label(f2, text="ALPHA.OS", font="calibri 18", bg="grey", fg="black")
    l4.pack(side=BOTTOM)
    l3.pack(side=BOTTOM)

    l5 = Label(f2, image=photo2, bg="grey")
    l5.pack(side=BOTTOM)

# ending loop
window.mainloop()
