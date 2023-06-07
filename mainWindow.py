from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from AdminWin import Admin
from TeacherWin import Teacher
from StudentWin import Student

class Face_Recognization_System:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title
       # self.root.wm.iconbitmap("icon.ico")

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
        #======================Admin=============================
        img4=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\adminnew.jfif")
        img4=img4.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img4)#storing image into variable
        #==================================
        admin=Button(bg_img,image=self.photoimg4,command=self.admin)
        admin.place(x=250,y=200,height=200,width=200)
        admin_1=Button(bg_img,text="Admin",command=self.admin,cursor="hand2",font=("times new roman",20,"bold"))
        admin_1.place(x=250,y=200,width=200,height=40)

        #=====================Teacher=====================
        img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\teachernew.png")
        img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg5=ImageTk.PhotoImage(img5)#storing image into variable
        # button=============================
        teacher=Button(bg_img,image=self.photoimg5,command=self.teacher)
        teacher.place(x=550,y=200,height=200,width=200)
        
        teacher_1=Button(bg_img,text="Teacher",command=self.teacher,cursor="hand2",font=("times new roman",20,"bold"))
        teacher_1.place(x=550,y=200,width=200,height=40)
        
        #========================student=====================
        img6=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\student.jpg")
        img6=img6.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg6=ImageTk.PhotoImage(img6)#storing image into variable
        # button=============================
        student=Button(bg_img,image=self.photoimg6,command=self.student)
        student.place(x=850,y=200,height=200,width=200)
        
        student_1=Button(bg_img,text="Student",command=self.student,cursor="hand2",font=("times new roman",20,"bold"))
        student_1.place(x=850,y=200,width=200,height=40)


    def admin(self):
        self.new_window=Toplevel(self.root)
        self.app=Admin(self.new_window)

    def teacher(self):
        self.new_window=Toplevel(self.root)
        self.app=Teacher(self.new_window)
    def student(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Face_Recognization_System(root)#making class object
    root.mainloop()#for end


