from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Ask_Me:
    def __init__ (self,root):
        self.root=root
        self.root.title("CHATBOX")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.entry_func)
        #self.root.wm.iconbitmap("icon.ico")
  #==========================================back groud image==================================
        img3=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\code.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg3=ImageTk.PhotoImage(img3)#storing image into variable

        bg_img=Label(self.root,image=self.photoimg3)#to set lebel
        bg_img.place(x=0,y=0,width=1530,height=710)

        # title_lbl=Label(bg_img,text="FACE RECOGNIZATION ATTENDANCE SYSTEM",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        # title_lbl.place(x=0,y=0,width=1300,height=45)


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open('images.png')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='ASK  ME',font=('arial',30,'bold'),fg='navy blue',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=10,relief=RAISED,font=('areal',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bg='white',width=730)
        btn_frame.pack()

        lable1=Label(btn_frame,text='Type Something',font=('arial',16,'bold'),fg='navy blue',bg='white')
        lable1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="send",command=self.send,font=('arial',17,'bold'),width=8,bg='navy blue')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='gray')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.lable2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
        self.lable2.grid(row=1,column=1,padx=5,sticky=W)



        #=======================conversation function===========================
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def entry_func(self,event):
        self.send.invoke()
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)

        if(self.entry.get()==''):
            self.msg='Please Enter Somthing'
            self.lable2.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.lable2.config(text=self.msg,fg='red')
        if(self.entry.get()=='hi'):
            self.text.insert(END,' '+'\t\t\t\t\tBot:hello ')
            self.text.insert(END,'\n'+'Bot:who are you ')
        elif(self.entry.get()=='help me'):
            self.text.insert(END,''+'\t\t\t\t\tBot:yeah sure')
        elif(self.entry.get()=='tell me about this application'):
            self.text.insert(END,'\n\n\t\t\t\t\n'+'\t\tBot:this appication built for taking attandence by using face')
        elif(self.entry.get()=='why this better than other'):
            self.text.insert(END,'\n\n\t\t\t\t\n'+'\t\t\t\t\tBot:it help you in proxy problem .')
        else:
             self.text.insert(END,'\n\n\t\t\t\t\n'+'\t\t\t\t\tBot:sorry i didnt get it')

            
        



         

if __name__ =='__main__':
    root=Tk()
    obj=Ask_Me(root)
    root.mainloop()




