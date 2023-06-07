from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from Help import Ask_Me
from contactUs import Help_Desk
from viewAttendance import view_attendance


class Student:
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

        title_lbl=Label(bg_img,text="STUDENT",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)
        #======================view Attendance=============================
        img4=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\view.jpg")
        img4=img4.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img4)#storing image into variable
      
        b1=Button(bg_img,image=self.photoimg4,command=self.view_atten)
        b1.place(x=250,y=200,height=200,width=200)
        b1_1=Button(bg_img,text="View Attendance",cursor="hand2",command=self.view_atten,font=("times new roman",20,"bold"))
        b1_1.place(x=250,y=200,width=200,height=40)

        #=======================Contact us=====================
        img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\contact.jpg")
        img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg5=ImageTk.PhotoImage(img5)#storing image into variable
        # button=============================
        b2=Button(bg_img,image=self.photoimg5,command=self.HelpDesk)
        b2.place(x=550,y=200,height=200,width=200)
        
        b2_1=Button(bg_img,text="Contact Us",command=self.HelpDesk,cursor="hand2",font=("times new roman",20,"bold"))
        b2_1.place(x=550,y=200,width=200,height=40)
        
        #========================Help=====================
        img6=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\help.jpg")
        img6=img6.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg6=ImageTk.PhotoImage(img6)#storing image into variable
        # button=============================
        b3=Button(bg_img,image=self.photoimg6,command=self.Help)
        b3.place(x=850,y=200,height=200,width=200)
        
        b3_1=Button(bg_img,text="Help",command=self.Help,cursor="hand2",font=("times new roman",20,"bold"))
        b3_1.place(x=850,y=200,width=200,height=40)


    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Ask_Me(self.new_window)

    def HelpDesk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help_Desk(self.new_window)


    def  view_atten(self):
        self.new_window=Toplevel(self.root)
        self.app=view_attendance(self.new_window)



if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Student(root)#making class object
    root.mainloop()#for end


