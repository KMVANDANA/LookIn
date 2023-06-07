from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
from mainWindow import Face_Recognization_System
from register import New_register
import mysql.connector
from mainWindow import Face_Recognization_System



class Login_page:
    
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title
        #self.root.wm.iconbitmap("icon.ico")


       

#===================================first image=========================================
        img=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\alface.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg=ImageTk.PhotoImage(img)#storing image into variable

        first_lbl=Label(self.root,image=self.photoimg)#to set lebel
        first_lbl.place(x=0,y=-40,width=500,height=200)
#=======================================second image======================================

        img1=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\header.webp")
        img1=img1.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg1=ImageTk.PhotoImage(img1)#storing image into variable

        first_lbl=Label(self.root,image=self.photoimg1)#to set lebel
        first_lbl.place(x=500,y=-40,width=500,height=200)
#===================================third image===========================================

        img2=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\verticalImage2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg2=ImageTk.PhotoImage(img2)#storing image into variable

        first_lbl=Label(self.root,image=self.photoimg2)#to set lebel
        first_lbl.place(x=1000,y=-40,width=500,height=200)

#==========================================back groud image==================================
        img3=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\code.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg3=ImageTk.PhotoImage(img3)#storing image into variable

        bg_img=Label(self.root,image=self.photoimg3)#to set lebel
        bg_img.place(x=0,y=90,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNIZATION ATTENDANCE SYSTEM",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)

        frame=Frame(self.root,bg="black")
        frame.place(x=450,y=160,width=340,height=480)

        img1=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\alface.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg.place(x=570,y=180,width=100,height=100)


        get_str=Label(frame,text="LogIn",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=130,y=140)
        #==========username==============
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=180)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=210,width=270)
        #======================password=============
        #==========username==============
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=250)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=280,width=270)
        
#=================login button================
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="navy blue")
        loginbtn.place(x=110,y=340,width=120,height=35)

#======================registration button===============
        Rbtn=Button(frame,text="New Registration",command=self.newR,font=("times new roman",10,"bold"),fg="white",bg="black",borderwidth=0)
        Rbtn.place(x=30,y=390,width=100,height=40)

#=========================forget password=============
        Fbtn=Button(frame,text="Forgot Password",command=self.Forget_pass,font=("times new roman",10,"bold"),fg="white",bg="black",borderwidth=0)
        Fbtn.place(x=200,y=390,width=100,height=40)


   
#===============function ===============
    def login(self):
     
        if self.txtuser.get()=="" or self.txtpass.get()=="":
          
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="HELLO" and self.txtpass.get()=="BYE":
         
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognization_System(self.new_window)     
            
        else:
         
         messagebox.showerror("invalid: "," invalid user")
         
    def newR(self):
        self.new_window=Toplevel(self.root)
        self.app=New_register(self.new_window)

    def Forget_pass(self):
        if self.txtuser.get=="":
            messagebox.showerror("Error","Please enter the e-mail address to reset password")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            
        if row==None:
            messagebox.showerror("My Error","Please enter the valid user name")

        else:
            conn.close()
            self.root2=Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("340x450+610+170")
      

   


if __name__ == "__main__":
    root=Tk()
    app=Login_page(root)
    root.mainloop()
 