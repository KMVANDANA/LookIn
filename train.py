from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np
import csv

class Train:
        def __init__(self,root):#calling constructor(root(window name))
            self.root=root#intialize root
            self.root.geometry("1430x690+0+0")#width and height(starting point)
            self.root.title("face recognization System")#window
            #self.root.wm.iconbitmap("icon.ico")

        #===================================first image=========================================
            img=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\alface.jpg")
            img=img.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
            self.photoimg=ImageTk.PhotoImage(img)#storing image into variable

            first_lbl=Label(self.root,image=self.photoimg)#to set lebel
            first_lbl.place(x=0,y=0,width=500,height=200)
    #=======================================second image======================================

            img1=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\header.webp")
            img1=img1.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
            self.photoimg1=ImageTk.PhotoImage(img1)#storing image into variable

            first_lbl=Label(self.root,image=self.photoimg1)#to set lebel
            first_lbl.place(x=500,y=0,width=500,height=200)
    #===================================third image===========================================

            img2=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\verticalImage2.jpg")
            img2=img2.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
            self.photoimg2=ImageTk.PhotoImage(img2)#storing image into variable

            first_lbl=Label(self.root,image=self.photoimg2)#to set lebel
            first_lbl.place(x=1000,y=0,width=500,height=200)

            title_lbl=Label(self.root,text="Train Data",font=("times new roman",40,"bold"),bg="white",fg="navy blue")#LABLE ON BG IMAGE
            title_lbl.place(x=0,y=0,width=1300,height=45)

        
            trn_btn=Button(self.root,text="TRAIN DATA",command=self.train_classfier,width=30,font=("times new roman",16,"bold"),bg="navy blue",fg="white")
            trn_btn.place(x=0,y=150,width=1330,height=60)


        def train_classfier(self):
            try:
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
                clf.write("classfier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("result","Training database completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    

    
if __name__ == '__main__':#main
 
    root=Tk()#calling root
    obj=Train(root)#making class object
    root.mainloop()#for end