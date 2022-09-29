from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from login import *
from PIL import ImageTk,Image
from tkinter import Label

class Welcome():
    def __init__(self,master):
        self.master = master
       
        #==============================FRAMES=========================================

        Form = Frame(master)
        Form.pack(side=TOP)        
        Form.configure(bg='white');        
        
        
        label = Label(Form,bg="black")
        label.grid(row=1)
        image = ImageTk.PhotoImage(Image.open("welcome.jpg"))
        label.config(image = image)
        label.image = image       


        #==============================BUTTON WIDGETS=================================
        btn_login = Button(Form,bg="#5eabde",fg="white", text="Proceed", width=25, command=self.onLoginButtonClick)
        btn_login.grid(row=4,column=0,pady=20)

    def onLoginButtonClick(self):
        self.master.withdraw() 
        self.newWindow = Toplevel(self.master)        
        self.app = LoginClass(self.newWindow)
        


mainFrame = Tk()
mainFrame.config(bg="white")
mainFrame.geometry("600x300")
mainFrame.resizable(0, 0)
mainFrame.title("Welcome Window")
cls = Welcome(mainFrame)

mainFrame.mainloop()
