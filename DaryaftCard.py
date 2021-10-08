from tkinter import*
from tkinter import messagebox
import os
from PIL import Image, ImageTk

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
        self.root.iconphoto(self.root,PhotoImage(file="F:\Python_projects\Final_project_GARD\logo.png"))
        self.logo = PhotoImage(file="F:\Python_projects\Final_project_GARD\logo.png")
        self.lab = Label(self.root,image=self.logo,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-50, y=50)
        #--------------------------------------------------------------entry password
        self.text1=PhotoImage(file="F:\Python_projects\Final_project_GARD\end.png")
        self.lab = Label(self.root,image=self.text1,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-350, y=400)
        #-----------------------------------------------------------------Side Buttons
        self.left_button=PhotoImage(file="F:\Python_projects\Final_project_GARD\left_button.PNG")
        self.but1 = Button(self.root,image=self.left_button,height=130 , width=130)
        self.but1.pack()
        self.but1.place(x=0, y=100)

        self.but2 = Button(self.root,image=self.left_button,height=130 , width=130)
        self.but2.pack()
        self.but2.place(x=0, y=300)

        self.but3 = Button(self.root,image=self.left_button,height=130 , width=130)
        self.but3.pack()
        self.but3.place(x=0, y=500)

        self.but4 = Button(self.root,image=self.left_button,height=130 , width=130)
        self.but4.pack()
        self.but4.place(x=0, y=700)

        self.right_button=PhotoImage(file="F:\Python_projects\Final_project_GARD\Right_button.PNG")
        self.but5 = Button(self.root,image=self.right_button,height=130 , width=130)
        self.but5.pack()
        self.but5.place(x=self.width-130, y=100)

        self.but6 = Button(self.root,image=self.right_button,height=130 , width=130)
        self.but6.pack()
        self.but6.place(x=self.width-130, y=300)

        self.but7 = Button(self.root,image=self.right_button,height=130 , width=130)
        self.but7.pack()
        self.but7.place(x=self.width-130, y=500)

        self.but8 = Button(self.root,image=self.right_button,height=130 , width=130)
        self.but8.pack()
        self.but8.place(x=self.width-130, y=700)



    def ask_quit(self):
        if messagebox.askokcancel("quit","Do you want to quit?"):
            os._exit(1)

def main():
    screen=parsian_bank()
    screen.root.mainloop()
if __name__ == "__main__":main()
    
    





