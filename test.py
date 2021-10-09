# Import the required libraries
from tkinter import *
import pygame
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x500")

# Add a background image
bg = ImageTk.PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k00.PNG")

label = Label(win, image=bg)
label.place(x=0, y=0)

# Initialize mixer module in pygame
pygame.mixer.init()

# Define a function to play the music
def play_sound():
   pygame.mixer.music.load("F:\Python_projects\Final_project_GARD\click.mp3")
   pygame.mixer.music.play()

# Add a Button widget
b1 = Button(win, text="Play Music", command=play_sound)
b1.pack(pady=60)

win.mainloop()
