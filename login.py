from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from trend import *
import mysql.connector
from PIL import ImageTk,Image
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="pass",
  database="twitterDb"
)
class LoginClass():
    def __init__(self , master):
        self.master = master
         
        
        master.configure(background='white')
        master.geometry("700x600")        
        master.resizable(0, 0)
        #==============================VARIABLES======================================
        PRODUCT_ID = StringVar()
        PASSWORD = StringVar()
        res = StringVar()
        #==============================FRAMES=========================================

        Form = Frame(master,highlightbackground="black", highlightcolor="black", highlightthickness=2)
        Form.configure(bg="white")
        Form.pack(side=TOP, pady=20,padx=20)
        
        label = Label(Form,bg="white")
        label.grid(row=0)
        image = ImageTk.PhotoImage(Image.open("welcome.jpg"))
        label.config(image = image)
        label.image = image
   
        # lbl_id = Label(Form,bg="white",fg="black", text = "Login Window", font=('arial', 18))
        # lbl_id.grid(row=2)     
       
        

        lbl_id = Label(Form,bg="white",fg="black", text = "User Name", font=('arial', 14), bd=15)
        lbl_id.grid(row=3)

        self.input_id = Entry(Form,bg="white", textvariable=PRODUCT_ID, font=('arial', 14),bd=2)
        self.input_id.grid(row=4,padx=20)
        
        lbl_password = Label(Form,bg="white",fg="black", text = "Password", font=('arial', 14), bd=15)
        lbl_password.grid(row=5)
        
        self.password = Entry(Form,bg="white", textvariable=PASSWORD, show="*", font=('arial', 14),bd=2)
        self.password.grid(row=6)
        
        
        

        #==============================BUTTON WIDGETS=================================
        btn_login = Button(Form,bg="#5eabde",fg="white", text="Login", width=25, command=self.Login)
        btn_login.grid(row=7,pady=20)
        btn_clear = Button(Form,bg="#5eabde",fg="white", text="Reset", width=25, command=self.Reset)
        btn_clear.grid(row=8,pady=10)
        # background_label.image = background_image
     
    def onLoginSuccess(self):
        self.master.withdraw() 
        self.newWindow = Toplevel(self.master)        
        self.app = TrendClass(self.newWindow)
          
    #Fucntion to clear text
    def Reset(self):
        self.input_id.delete(0,END)
        self.input_id.insert(0,'')
        self.password.delete(0,END)
        self.password.insert(0,'')
        self.password.insert(0,'')
     
    #Fucntion to check Login 
    def Login(self):
        if self.password.get()=='' or self.input_id.get()=='':
            messagebox.showinfo('', 'All Fields Mandatory')                
        else:
             mycursor = mydb.cursor()
             mysql_query="""SELECT * FROM admindetails where uname=%s AND password=%s"""
             mycursor.execute(mysql_query, (self.input_id.get(),self.password.get(),))
             myresult = mycursor.fetchall()  
             cnt=0
             for row in myresult:
                 cnt=1 
             if cnt==0:
                messagebox.showinfo('Response', 'Invalid Credentials')
             else:
                self.onLoginSuccess()
                # messagebox.showinfo('Response', 'Login Successful')
