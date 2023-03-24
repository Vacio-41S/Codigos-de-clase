from tkinter import *
import pygame, sys
from pygame.locals import*
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init() #Iniciamos modulo de pygame
def openFileSong():
    cancion = filedialog.askopenfilename() #Guardar el nombre o cancion que queremos reproducion
    print(cancion)
    pygame.mixer.music.load(cancion)



def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

def volumenUp():
    volumenLevel1 = pygame.mixer.music.get_volume() + 0.2
    print(volumenLevel1)
    pygame.mixer.music.set_volume(volumenLevel1)

def volumenDown():
    volumenLevel1 = pygame.mixer.music.get_volume() - 0.2
    print(volumenLevel1)
    pygame.mixer.music.set_volume(volumenLevel1)

raiz = Tk()
raiz.title("Reproductor MP3 - GUI")
raiz.iconbitmap("pips.ico")
raiz.geometry("1000x600")
raiz.resizable(0,0)

#CRear Frame
framePrincipal = Frame(raiz, bg="#4a4a4a")
framePrincipal.pack(fill="both", expand=1)

#Titulo Reproductor
titleReproductor = Label(framePrincipal, text="Reproductor MP3 - GUI", font=("Roboto", 20,"bold "),bg="#4a4a4a", fg="#fbfbfb" )
titleReproductor.place(relx=0.27, rely=0.45)

#Boton Open Song
botonOpenSong = Button(framePrincipal, text="Open Song",bg="#a5eea0",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=openFileSong)
botonOpenSong.place(relx=0.05, rely=0.6)

#Boton Play Song
botonPlaySong = Button(framePrincipal, text="Play",bg="#42ab49",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=playSong)
botonPlaySong.place(relx=0.2, rely=0.6)

#Stop Song
botonStopSong = Button(framePrincipal, text="Stop",bg="#e2504c",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=stopSong)
botonStopSong.place(relx=0.35, rely=0.6)

#Resume
botonResumeSong = Button(framePrincipal, text="Resume",bg="#ffc400",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=resumeSong)
botonResumeSong.place(relx=0.5, rely=0.6)

#Pause
botonPauseSong = Button(framePrincipal, text="Pause",bg="#550099",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=pauseSong)
botonPauseSong.place(relx=0.65, rely=0.6)

#Volumen+
botonVolumen1Song = Button(framePrincipal, text="Vol +",bg="#550",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=volumenUp)
botonVolumen1Song.place(relx=0.28, rely=0.7)

#Volumen-
botonVolumen0Song = Button(framePrincipal, text="Vol -",bg="#099",fg="#fbfbfb",font=("Roboto", 15, "bold"), width=10, height=1, command=volumenDown)
botonVolumen0Song.place(relx=0.43, rely=0.7)

#ImagenReproductor


raiz.mainloop()