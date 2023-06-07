from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from studentDetailsTeacher import Student_Teacher
from contactToAdmin import Contact_To_Admin
from facerecognize import Face_recognize

from train import Train
import cv2
import numpy as np

#from facerecognize import Face_recognize

import os


class Teacher:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("Face Recognization System")#window title
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

        title_lbl=Label(bg_img,text="TEACHER",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)
        #view student  details button
        img4=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\images (1).png")
        img4=img4.resize((200,140),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img4)#storing image into variable
        #==================================
        b1=Button(bg_img,image=self.photoimg4,command=self.Student_Details,cursor="hand2")
        b1.place(x=100,y=200,height=200,width=200)
        b1_1=Button(bg_img,text="Student Record",cursor="hand2",font=("times new roman",20,"bold"))
        b1_1.place(x=100,y=200,width=200,height=40)

        #====================picture=====================
        img5=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\facer.jpg")
        img5=img5.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg5=ImageTk.PhotoImage(img5)#storing image into variable
        # button=============================
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=400,y=200,height=200,width=200)

        b2_1=Button(bg_img,text="Face Recognize",command=self.face_rr,cursor="hand2",font=("times new roman",20,"bold"))
        b2_1.place(x=400,y=200,width=200,height=40)
        
        #=================Train Data=====================
        img6=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\images.png")
        img6=img6.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg6=ImageTk.PhotoImage(img6)#storing image into variable
        # button=============================
        b3=Button(bg_img,image=self.photoimg6,command=self.train_classfier)
        b3.place(x=700,y=200,height=200,width=200)
        
        b3_1=Button(bg_img,text="Train Data",command=self.train_classfier,cursor="hand2",font=("times new roman",20,"bold"))
        b3_1.place(x=700,y=200,width=200,height=40)

#=============contact to admin=====================
        img7=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\picture.jpg")
        img7=img7.resize((200,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg7=ImageTk.PhotoImage(img7)#storing image into variable
        # button=============================
        b4=Button(bg_img,image=self.photoimg7,command=self.open_img)
        b4.place(x=1000,y=200,height=200,width=200)
        
        b4_1=Button(bg_img,text="Picture",command=self.open_img,cursor="hand2",font=("times new roman",20,"bold"))
        b4_1.place(x=1000,y=200,width=200,height=40)

    def train_classfier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path :
            img=Image.open(image).convert('L')#Gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("training image",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
#====================train the classsifier and save====================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        
    def Student_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Teacher(self.new_window)


    def face_rr(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognize(self.new_window)

    # def contactAdmin(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Contact_To_Admin(self.new_window)
  
    def open_img(self):
           os.startfile("data")


   

    
    def open_img(self):
        os.startfile("data")


if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Teacher(root)#making class object
    root.mainloop()#for end


