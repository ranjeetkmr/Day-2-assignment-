from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        
        #======BG IMAGE======
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="H:/bg-01.jpg")
       # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #==========Login Frame======
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)
        
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        
        desc=Label(Frame_login,text="Accountant employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
         
        Login_btn=Button(self.root,command=self.login_function,text="Login",bg="#d77337",fg="white",bd=0,font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
        
        forget_btn=Button(Frame_login,text="Forget Password?",fg="white",bg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="India" or self.txt_user.get()!="India":
            
            messagebox.showerror("Error","Invalid username/password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password:{self.txt_pass.get()}",parent=self.root)
            
root=Tk()
obj=Login(root)
root.mainloop()
