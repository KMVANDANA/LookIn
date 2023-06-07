from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from studentDetailsAdmin import Student_Admin
from teacherDetails import Teacher_Admin

class Admin:
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

        title_lbl=Label(bg_img,text="ADMIN",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)
        #view student  details button
        img4=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\record.png")
        img4=img4.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img4)#storing image into variable
        #==================================
        b1=Button(bg_img,image=self.photoimg4,command=self.Student_Details,cursor="hand2")
        b1.place(x=700,y=200,height=200,width=200)

        b1_1=Button(bg_img,text="Student Details",command=self.Student_Details,cursor="hand2",font=("times new roman",20,"bold"))
        b1_1.place(x=700,y=200,width=200,height=40)

        #view teacher records=====================
        img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\record.png")
        img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg5=ImageTk.PhotoImage(img4)#storing image into variable
        # button=============================
        b1=Button(bg_img,image=self.photoimg5,command=self.Teacher_Details,cursor="hand2")
        b1.place(x=400,y=200,height=200,width=200)
        
        b1_1=Button(bg_img,text="Teacher record ",command=self.Teacher_Details,cursor="hand2",font=("times new roman",20,"bold"))
        b1_1.place(x=400,y=200,width=200,height=40)
        
        # # edit teacher details=====================
        # img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\images.png")
        # img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        # self.photoimg5=ImageTk.PhotoImage(img4)#storing image into variable
        # # button=============================
        # b1=Button(bg_img,image=self.photoimg5)
        # b1.place(x=700,y=200,height=200,width=200)
        
        # b1_1=Button(bg_img,text="Edit Teacher",cursor="hand2",font=("times new roman",20,"bold"))
        # b1_1.place(x=700,y=200,width=200,height=40)

#edit student details=====================
        # img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\images.png")
        # img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        # self.photoimg5=ImageTk.PhotoImage(img4)#storing image into variable
        # # button=============================
        # b1=Button(bg_img,image=self.photoimg5)
        # b1.place(x=1000,y=200,height=200,width=200)
        
        # b1_1=Button(bg_img,text="Edit Student ",cursor="hand2",font=("times new roman",20,"bold"))
        # b1_1.place(x=1000,y=200,width=200,height=40)

        #=======================function button=================
    def Student_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Admin(self.new_window)
    def Teacher_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Teacher_Admin(self.new_window)



if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Admin(root)#making class object
    root.mainloop()#for end


