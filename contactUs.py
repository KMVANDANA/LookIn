from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk


class Help_Desk:
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


        title_lbl=Label(bg_img,text="Contact Us",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)
        van_lbl=Label(bg_img,text="vandana125.alg@gmail.com",font=("times new roman",20,"bold"),fg="black")
        van_lbl.place(x=500,y=200)
        van_lbl=Label(bg_img,text="9080706050",font=("times new roman",20,"bold"),fg="black")
        van_lbl.place(x=500,y=240)

        vaish_lbl=Label(bg_img,text="vaish126.alg@gmail.com",font=("times new roman",20,"bold"),fg="black")
        vaish_lbl.place(x=500,y=280)
        vaish_lbl=Label(bg_img,text="1020304050",font=("times new roman",20,"bold"),fg="black")
        vaish_lbl.place(x=500,y=320)

        riya_lbl=Label(bg_img,text="riya126.alg@gmail.com",font=("times new roman",20,"bold"),fg="black")
        riya_lbl.place(x=500,y=320)
        riya_lbl=Label(bg_img,text="1020304050",font=("times new roman",20,"bold"),fg="black")
        riya_lbl.place(x=500,y=360)

        anmol_lbl=Label(bg_img,text="anmol127.alg@gmail.com",font=("times new roman",20,"bold"),fg="black")
        anmol_lbl.place(x=500,y=400)
        anmol_lbl=Label(bg_img,text="1020304050",font=("times new roman",20,"bold"),fg="black")
        anmol_lbl.place(x=500,y=440)

if __name__ == "__main__":
    root=Tk()
    app=Help_Desk(root)
    root.mainloop()
 