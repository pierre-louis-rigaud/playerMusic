import os
import time
import pygame
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Music Player")
root.geometry("535x600+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()            

def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.queue(Playlist.get(ACTIVE))
    mixer.music.play()
#     return mixer.music.play()
    

lower_frame = Frame(root , bg = "#FFFFFF", width = 535 , height = 180 )
lower_frame.place ( x = 0 , y = 400)



image_icon = PhotoImage(file="images/night-city-logo.png")
root.iconphoto(False, image_icon)


frameCnt = 40
frames = [PhotoImage(file='images/lake.gif',format = 'gif -index %i' %(i), width=530, height=395) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)




ButtonPlay = PhotoImage(file="images/start2.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=20, y=410)  #x=215, y=487

ButtonUnpause = PhotoImage(file="images/play.png")
Button(root, image=ButtonUnpause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=130, y=410) #x=20, y=487

ButtonPause = PhotoImage(file="images/pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.pause).place(x=215, y=410) #x=300, y=487

ButtonStop = PhotoImage(file="images/stop.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.stop).place(x=300, y=410) #x=130, y=487

def increase_volume():
    current_volume = mixer.music.get_volume()
    new_volume = min(1.0, current_volume + 0.2)
    mixer.music.set_volume(new_volume)

def decrease_volume():
    current_volume = mixer.music.get_volume()
    new_volume = max(0.0, current_volume - 0.1)
    mixer.music.set_volume(new_volume)

ButtonVolumeUp = PhotoImage(file="images/volumeUP.png")
Button(root, image=ButtonVolumeUp, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=increase_volume).place(x=385, y=410) 

ButtonVolumeDown = PhotoImage(file="images/volumeDOWN.png")
Button(root, image=ButtonVolumeDown, bg="#FFFFFF", bd=0, height = 60, width =60,
       command= decrease_volume).place(x=470, y=410) 


      
Menu = PhotoImage(file="images/menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=505, width=535, height=100)



Button(root, text="Browse Music", width=68, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=475)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)


root.mainloop()