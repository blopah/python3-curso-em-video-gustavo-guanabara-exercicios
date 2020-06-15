from tkinter.filedialog import askdirectory

print('\nFaça um programa em Python que abra e reproduza o audio de um arquivo em mp3.\n')

import os
import pygame
from tkinter import *

root = Tk()
root.minsize(300, 300)

listofsong = []

index = 0

def directorychooser():

    directory = askdirectory()
    os.(directory)

    for files in os.listdir(directory):
        if files.endswith('.mp3'):
            listofsong.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsong[5])
    # pygame.mixer.music.play()

label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

nextbutton = Button(root, text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root, text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root, text = 'Stop Music')
stopbutton.pack()

directorychooser()


root.mainloop()