from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mainWindow import Face_Recognization_System



class New_register:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#windFname=StringVar()

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()

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

        title_lbl=Label(bg_img,text=" Register Here",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=6)
        main_frame.place(x=250,y=80,width=800,height=400)

        Fname_label=Label(main_frame,text="First Name",font=("times new roman",13,"bold"))
        Fname_label.grid(row=0,column=0,padx=10,pady=8,sticky=W)

        Fname_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        Fname_entry.grid(row=0,column=1,padx=10,pady=8,sticky=W)
#=================================================================================
        Lname_label=Label(main_frame,text="Last Name",font=("times new roman",15,"bold"))
        Lname_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        Lname_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        Lname_entry.grid(row=0,column=3,padx=10,pady=8,sticky=W)
#=======================================================================

        con_label=Label(main_frame,text="Contact Number ",font=("times new roman",15,"bold"))
        con_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)

        con_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        con_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)

  #============================================================================    

        Email_label=Label(main_frame,text="Email",font=("times new roman",15,"bold"))
        Email_label.grid(row=1,column=2,padx=10,pady=8,sticky=W)

        Email_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_email,font=("times new roman",15,"bold"))
        Email_entry.grid(row=1,column=3,padx=10,pady=8,sticky=W)
#=================================================================================

        Sques_label=Label(main_frame,text="Security Question",font=("times new roman",15,"bold"))
        Sques_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        Sques_combo=ttk.Combobox(main_frame,textvariable=self.var_secQ,font=("times new roman",15,"bold"),state="randomly",width=20)
        Sques_combo["values"]=("Select","What Is Your First Pet Name","Which Is Your Fav Movie","The Name You Like The Most")
        Sques_combo.current(0)
        Sques_combo.grid(row=2,column=1,padx=2,pady=8,sticky=W)

#======================================================================================
        Sans_label=Label(main_frame,text="Security Answer",font=("times new roman",15,"bold"))
        Sans_label.grid(row=2,column=2,padx=10,pady=8,sticky=W)

        Sans_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_secA,font=("times new roman",15,"bold"))
        Sans_entry.grid(row=2,column=3,padx=10,pady=8,sticky=W)
        #=================================================================================


        Password_label=Label(main_frame,text="Password",font=("times new roman",15,"bold"))
        Password_label.grid(row=3,column=0,padx=10,pady=8,sticky=W)

        Password_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        Password_entry.grid(row=3,column=1,padx=10,pady=8,sticky=W)

#======================================================================================
        Cpass_label=Label(main_frame,text="Confirm Password",font=("times new roman",15,"bold"))
        Cpass_label.grid(row=3,column=2,padx=10,pady=8,sticky=W)

        Cpass_entry=ttk.Entry(main_frame,width=20,textvariable=self.var_cpass,font=("times new roman",15,"bold"))
        Cpass_entry.grid(row=3,column=3,padx=10,pady=8,sticky=W)


#===========================================================================
        Checkbtn=Checkbutton(main_frame,text="I Agree The Term And Conditions",font=("times new roman",15,"bold"),offvalue=0,onvalue=1)
        Checkbtn.place(x=250,y=500)

 #===========================================================================
        img1=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\login.jpg")
        img1=img1.resize((100,50),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg1=ImageTk.PhotoImage(img1)#storing image into variable
      
        login=Button(main_frame,image=self.photoimg1,command=self.register_data,)
        login.grid(row=4,column=0)

#===============================================================================
        img2=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\signup.png")
        img2=img2.resize((100,50),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img2)#storing image into variable
      
        signup=Button(main_frame,image=self.photoimg4)
        signup.grid(row=4,column=2)

    def register_data(self):
        try:
            if self.var_fname.get()=="" or self.var_email.get()==""or  self.var_secQ().get()=="select":
                messagebox.showerror("Error","All field are required")
            elif self.var_pass.get()!=self.var_cpass.get():
                messagebox.showerror("Error","Password and Confirm Password Must be same")
            else:
               conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
               my_cursor=conn.cursor()
               query=("select* from register where email=%s")
               value=(self.var_email)
               my_cursor.execute(query,value)
               row=my_cursor.fetchone()
               if row!=None:
                   messagebox.showerror("Error","user already exist, please try another email")
               else:
                   my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_fname.get(),
                                                                            self.var_lname.get(),
                                                                            self.var_contact.get(),
                                                                            self.var_email.get(),
                                                                            self.var_secQ.get(),
                                                                            self.var_secA.get(),
                                                                            self.var_pass.get()
                                                                            
                   ))
               conn.commit()
               conn.close()
               messagebox.showinfo("Succsessfully")

        except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def login(self):
        try:
            if self.txtuser.get==" " or self.txtpass.get()==" ":
                messagebox.showerror("Error","all field required")
            elif self.txtuser.get()=="HELLO" and self.txtpass.get()=="BYE":
                messagebox.showinfo("success","welcome to lookin ")
            else:
               conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from register where email=%s and pass=%s",(
                   
                self.var_email.get(),
                self.var_pass.get()
              
               ))

               row=my_cursor.fetchone()

               if row==None:
                   messagebox.showerror("Error","Invalid Username And Password")
               else:
                   open_main=messagebox.askyesno("yes no","Acsses Only admin")
                   if open_main>0:
                       self.new_window=Toplevel(self.new_window)
                       self.app=Face_Recognization_System(self.new_window)
                   else:
                       if not open_main:
                           return
               conn.commit()
               conn.close()
               
               

        except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=New_register(root)#making class object
    root.mainloop()#for end
