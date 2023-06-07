from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox

class Contact_To_Admin:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title
        #self.root.wm.iconbitmap("icon.ico")


#==========================================back groud image==================================
        img3=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\laptop.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg3=ImageTk.PhotoImage(img3)#storing image into variable

        bg_img=Label(self.root,image=self.photoimg3)#to set lebel
        bg_img.place(x=0,y=-5,width=1530,height=710)

        title_lbl=Label(bg_img,text="Contact TO Admin",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)
        van_lbl=Label(bg_img,text="abc123.alg@gmail.com",font=("times new roman",20,"bold"),fg="black")
        van_lbl.place(x=520,y=220)
        van_lbl=Label(bg_img,text="0123456789",font=("times new roman",20,"bold"),fg="black")
        van_lbl.place(x=520,y=270)
if __name__ == "__main__":
    root=Tk()
    app=Contact_To_Admin(root)
    root.mainloop()
 