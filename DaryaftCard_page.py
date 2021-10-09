# -*- coding: UTF-8 -*-
from tkinter import*
from tkinter import messagebox
import os
import pygame

class parsian_bank:
    def __init__(self):

        self.root = Tk()
        #self.root.config(bg="#e6dce0")
        self.root.title("Parsian Bank")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        #self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.root.geometry("%dx%d" %(self.width,self.height))
        self.root.wm_state('zoomed')
        self.root.resizable(False, False)
        self.root.iconphoto(self.root,PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png"))
        self.logo = PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png")
        self.lab = Label(self.root,image=self.logo,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-50, y=50)
        pygame.mixer.init()
        #--------------------------------------------------------------Top message
        self.text1=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\mablagh.png")
        self.lab = Label(self.root,image=self.text1,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-140, y=230)
        #--------------------------------------------------------------choises
        self.lab = Label(self.root,text="100,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=self.width-250 , y=320)
        self.lab = Label(self.root,text="500,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=self.width-250 , y=450)
        self.lab = Label(self.root,text="1,200,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=self.width-250 , y=580)
        self.lab = Label(self.root,text="2,000,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=self.width-250 , y=720)
        
        self.lab = Label(self.root,text="300,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=100 , y=320)
        self.lab = Label(self.root,text="800,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=100 , y=450)
        self.lab = Label(self.root,text="1,500,000",borderwidth=10,font=("Helvetica", "25"))
        self.lab.pack()
        self.lab.place(x=100 , y=580)
        self.DaryaftCard=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\daryaft_card.PNG")
        self.lab = Label(self.root,image=self.DaryaftCard,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=100, y=720)
        #-----------------------------------------------------------------Side Buttons
        self.left_button=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\left_button.PNG")
        self.but1 = Button(self.root,image=self.left_button,height=90 , width=90)
        self.but1.pack()
        self.but1.place(x=0, y=300)
        self.but1.bind('<Button-1>', self.music)

        self.but2 = Button(self.root,image=self.left_button,height=90 , width=90)
        self.but2.pack()
        self.but2.place(x=0, y=430)
        self.but2.bind('<Button-1>', self.music)

        self.but3 = Button(self.root,image=self.left_button,height=90 , width=90)
        self.but3.pack()
        self.but3.place(x=0, y=560)
        self.but3.bind('<Button-1>', self.music)

        self.but4 = Button(self.root,image=self.left_button,height=90 , width=90)
        self.but4.pack()
        self.but4.bind('<Button-1>', self.music)
        self.but4.config(command=self.Daryaft_Card)
        self.but4.place(x=0, y=700)

        self.right_button=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\Right_button.PNG")
        self.but5 = Button(self.root,image=self.right_button,height=90 , width=90)
        self.but5.pack()
        self.but5.place(x=self.width-90, y=300)
        self.but5.bind('<Button-1>', self.music)

        self.but6 = Button(self.root,image=self.right_button,height=90 , width=90)
        self.but6.pack()
        self.but6.place(x=self.width-90, y=430)
        self.but6.bind('<Button-1>', self.music)

        self.but7 = Button(self.root,image=self.right_button,height=90 , width=90)
        self.but7.pack()
        self.but7.place(x=self.width-90, y=560)
        self.but7.bind('<Button-1>', self.music)

        self.but8 = Button(self.root,image=self.right_button,height=90 , width=90)
        self.but8.pack()
        self.but8.place(x=self.width-90, y=700)
        self.but8.bind('<Button-1>', self.music)



    def ask_quit(self):
        if messagebox.askokcancel("quit","Do you want to quit?"):
            os._exit(1)

    def music(self,event=None):
        pygame.mixer.music.load("F:\Python_projects\Final_project_GARD\click.mp3")
        pygame.mixer.music.play(loops=0)

    def Daryaft_Card(self):
        self.root.destroy()
        #new=DaryafCard_page()

def main():
    screen=parsian_bank()
    screen.root.mainloop()
if __name__ == "__main__":main()
    
    





