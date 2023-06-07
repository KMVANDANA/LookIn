from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk

class Face_Recognization_System:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title

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
        #for student button
        img4=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\student.jpg")
        img4=img4.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img4)#storing image into variable
        #student button
        b1=Button(bg_img,image=self.photoimg4)
        b1.place(x=100,y=100,height=200,width=200)
        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",20,"bold"))
        b1_1.place(x=100,y=100,width=200,height=40)

        #detect face
        img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\images.png")
        img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg5=ImageTk.PhotoImage(img4)#storing image into variable
        #detect  button
        b1=Button(bg_img,image=self.photoimg5)
        b1.place(x=400,y=100,height=200,width=200)
        
        b1_1=Button(bg_img,text="face detactor",cursor="hand2",font=("times new roman",20,"bold"))
        b1_1.place(x=400,y=100,width=200,height=40)
        #=

if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Face_Recognization_System(root)#making class object
    root.mainloop()#for end


