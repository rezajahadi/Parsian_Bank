from tkinter import*
from tkinter import messagebox
import os
import pygame
import time

class parsian_bank:
    def __init__(self):

        self.root = Tk()
        self.s=0
        #self.root.config(bg="#e6dce0")
        self.root.title("Parsian Bank")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.root.geometry("%dx%d" %(self.width,self.height))
        self.root.wm_state('zoomed')
        self.root.resizable(False, False)
        pygame.mixer.init()
        #--------------------------------------------------------------icon settings
        self.root.iconphoto(self.root,PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png"))
        self.logo = PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png")
        self.lab = Label(self.root,image=self.logo,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-50, y=50)
        #--------------------------------------------------------------Password Entry
        self.text1=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\password.png")
        self.lab = Label(self.root,image=self.text1,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-200, y=400)
        self.e1=Entry(self.root, width=10, font=('arial',30))
        self.e1.pack()
        self.e1.place(x=(self.width/2)-100, y=550)
        self.e1.config(show='*')

        self.b=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\keyboard.PNG")
        self.keyboard = Button(self.root,image=self.b,height=50 , width=85 ,command=self.key)
        self.keyboard.pack()
        self.keyboard.place(x=(self.width/2)+140, y=545)

        self.text2=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\password1.png")
        self.lab = Label(self.root,image=self.text2,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-130, y=620)

        self.text3=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\password2.png")
        self.lab = Label(self.root,image=self.text3,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-189, y=680)
        #-----------------------------------------------------------------buttom texts
        self.DaryaftCard=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\daryaft_card.PNG")
        self.lab = Label(self.root,image=self.DaryaftCard,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=150, y=720)

        self.english_language=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\english_language.PNG")
        self.lab = Label(self.root,image=self.english_language,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=self.width-330, y=720)
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
        #--------------------------------------------------------------keyboard
        self.r=Toplevel(self.root)
        self.r.geometry("270x240+%d+50" %(self.width/2-120))

        self.key1=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k1.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key1, command=lambda:self.e1.insert(100,'1'))
        self.b2.pack()
        self.b2.place(x=0,y=0)
        self.b2.bind('<Button-1>', self.music)

        self.key2=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k2.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key2, command=lambda:self.e1.insert(100,'2'))
        self.b2.pack()
        self.b2.place(x=60,y=0)
        self.b2.bind('<Button-1>', self.music)

        self.key3=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k3.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key3, command=lambda:self.e1.insert(100,'3'))
        self.b2.pack()
        self.b2.place(x=120,y=0)
        self.b2.bind('<Button-1>', self.music)

        self.key4=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\cancel.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key4)
        self.b2.pack()
        self.b2.place(x=210,y=0)
        self.b2.bind('<Button-1>', self.music)

        self.key5=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k4.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key5, command=lambda:self.e1.insert(100,'4'))
        self.b2.pack()
        self.b2.place(x=0,y=60)
        self.b2.bind('<Button-1>', self.music)

        self.key6=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k5.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key6, command=lambda:self.e1.insert(100,'5'))
        self.b2.pack()
        self.b2.place(x=60,y=60)
        self.b2.bind('<Button-1>', self.music)

        self.key7=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k6.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key7, command=lambda:self.e1.insert(100,'6'))
        self.b2.pack()
        self.b2.place(x=120,y=60)
        self.b2.bind('<Button-1>', self.music)

        self.key8=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\correct.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key8, command=self.DeleteCharacter)
        self.b2.pack()
        self.b2.place(x=210,y=60)
        self.b2.bind('<Button-1>', self.music)

        self.key9=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k7.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key9, command=lambda:self.e1.insert(100,'7'))
        self.b2.pack()
        self.b2.place(x=0,y=120)
        self.b2.bind('<Button-1>', self.music)

        self.key10=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k8.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key10, command=lambda:self.e1.insert(100,'8'))
        self.b2.pack()
        self.b2.place(x=60,y=120)
        self.b2.bind('<Button-1>', self.music)

        self.key11=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k9.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key11, command=lambda:self.e1.insert(100,'9'))
        self.b2.pack()
        self.b2.place(x=120,y=120)
        self.b2.bind('<Button-1>', self.music)

        self.key12=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\empty.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key12)
        self.b2.pack()
        self.b2.place(x=210,y=120)
        self.b2.bind('<Button-1>', self.music)

        self.key13=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k00.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key13, command=lambda:self.e1.insert(100,'00'))
        self.b2.pack()
        self.b2.place(x=0,y=180)
        self.b2.bind('<Button-1>', self.music)

        self.key14=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k0.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key14, command=lambda:self.e1.insert(100,'0'))
        self.b2.pack()
        self.b2.place(x=60,y=180)
        self.b2.bind('<Button-1>', self.music)

        self.key15=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\k000.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key15, command=lambda:self.e1.insert(100,'000'))
        self.b2.pack()
        self.b2.place(x=120,y=180)
        self.b2.bind('<Button-1>', self.music)

        self.key16=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\ok.PNG")
        self.b2=Button(self.r, height=50, width=50, image=self.key16, command=self.CheckPassword)
        self.b2.pack()
        self.b2.place(x=210,y=180)
        self.b2.bind('<Button-1>', self.music)

        
        self.root.after(15000,self.Daryaft_Card)
        self.r.protocol("WM_DELETE_WINDOW", self.close)
        self.r.withdraw()



    def ask_quit(self):
        if messagebox.askokcancel("Quit","Do you realy want to quit?!"):
            os._exit(1)  

    def Daryaft_Card(self):
        self.root.destroy()
        new=DaryafCard_page()  

    def key(self):
        if(self.s==0): 
            self.r.update()
            self.r.deiconify()
            self.s=1

    def close(self):
        self.r.withdraw()
        self.s=0

    def CheckPassword(self):
        s1=self.e1.get()
        if(s1=="1234"):
            self.root.destroy()
            new = operation_page()
        else:
            print("No")

    def DeleteCharacter(self):
        #self.e1.delete(0,END)
        a = len(self.e1.get())
        self.e1.delete(a-1)

    def music(self,event=None):
        pygame.mixer.music.load("F:\Python_projects\Final_project_GARD\click.mp3")
        pygame.mixer.music.play(loops=0)


class DaryafCard_page:
    def __init__(self):

        self.root = Tk()
        #self.root.config(bg="#e6dce0")
        self.root.title("Parsian Bank")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.root.geometry("%dx%d" %(self.width,self.height))
        self.root.wm_state('zoomed')
        self.root.resizable(False, False)
        self.root.iconphoto(self.root,PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png"))
        self.logo = PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png")
        self.lab = Label(self.root,image=self.logo,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-50, y=50)
        #--------------------------------------------------------------entry password
        self.text1=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\end.png")
        self.lab = Label(self.root,image=self.text1,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-350, y=400)
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

        self.root.after(15000,self.root.withdraw)

        self.root.mainloop()
    def music(self,event=None):
        pygame.mixer.music.load("F:\Python_projects\Final_project_GARD\click.mp3")
        pygame.mixer.music.play(loops=0)

    def ask_quit(self):
        if messagebox.askokcancel("Quit","Do you realy want to quit?!"):
            os._exit(1)

class operation_page:
    def __init__(self):

        self.root = Tk()
        #self.root.config(bg="#e6dce0")
        self.root.title("Parsian Bank")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.root.geometry("%dx%d" %(self.width,self.height))
        self.root.wm_state('zoomed')
        self.root.resizable(False, False)
        self.root.iconphoto(self.root,PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png"))
        self.logo = PhotoImage(file="F:\Python_projects\Final_project_GARD\images\logo.png")
        self.lab = Label(self.root,image=self.logo,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-50, y=50)
        #--------------------------------------------------------------Top message
        self.text1=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\operations.png")
        self.lab = Label(self.root,image=self.text1,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=(self.width/2)-250, y=200)
        #--------------------------------------------------------------choices
        self.d=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\daryaft_vajh.PNG")
        self.lab = Label(self.root,image=self.d,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=self.width-290 , y=300)
        self.s=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\SoartHesab.PNG")
        self.lab = Label(self.root,image=self.s,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=self.width-280 , y=430)
        self.enteghal=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\enteghal_vajh.PNG")
        self.lab = Label(self.root,image=self.enteghal,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=self.width-370 , y=560)
        self.ramz=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\pass_operation.PNG")
        self.lab = Label(self.root,image=self.ramz,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=100 , y=320)
        self.pardakht=PhotoImage(file="F:\Python_projects\Final_project_GARD\images\pardakht_ghabz.PNG")
        self.lab = Label(self.root,image=self.pardakht,borderwidth=10)
        self.lab.pack()
        self.lab.place(x=100 , y=430)
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
        self.but5.config(command=self.Daryaft_vajh)

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

        self.root.after(15000,self.Daryaft_Card)

        self.root.mainloop()
    def Daryaft_Card(self):
        self.root.destroy()
        new=DaryafCard_page()

    def music(self,event=None):
        pygame.mixer.music.load("F:\Python_projects\Final_project_GARD\click.mp3")
        pygame.mixer.music.play(loops=0)

    def ask_quit(self):
        if messagebox.askokcancel("Quit","Do you realy want to quit?!"):
            os._exit(1)

    def Daryaft_vajh(self):
        self.root.destroy()
        new=DaryaftVajh_page()

class DaryaftVajh_page:
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
        #pygame.mixer.init()
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
        new=DaryafCard_page()

        


def main():
    screen=parsian_bank()
    screen.root.mainloop()
if __name__ == "__main__":main()
    
    





