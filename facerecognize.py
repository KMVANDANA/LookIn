from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np
#from train import Train
from studentDetailsTeacher import  Student_Teacher
from time import strftime
from datetime import datetime
import csv



class Face_recognize:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window
        #self.root.wm.iconbitmap("icon.ico")


        title_lbl=Label(self.root,text="Face Recognization",font=("times new roman",40,"bold"),bg="white",fg="red")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=60)

        
        img3=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\phone.jpg")
        #img3=img3.resize((1530,710),Image.ANTIALIAS)#antilias covert high level image into low level
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)#storing image into variable

        bg_img=Label(self.root,image=self.photoimg3)#to set lebel
        bg_img.place(x=0,y=55,width=1500,height=600)

        showAll_btn=Button(bg_img,text="Face Recognize",command=self.face_recog,cursor="hand2",width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.place(x=640,y=450,width=200,height=40)


        #======================attandence Mark======================
    # def mark_attandence(self,i,r,n,d):
    #     with open("mark.csv","r+",new="\n") as f:
    #         my_dataList=f.readlines()
    #         name_list=[]
    #         for line in my_dataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         if((i not in name_list) and (i not in name_list) and(i not in name_list) and (i not in name_list) ) :
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")    
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")



        


    def face_recog(self):
        try: 
           
            def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):#boundry draaw
            
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                print("hello yes")
                coord=[]
                print("hello no")
                for(x,y,w,h) in features:
                    print("cccccccczzzzzz")
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    print("helloooooooo")
                    confidence=int((100*(1-predict/300)))
                    print("yesssssssssssssssss")

                    conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select stu_name from teacherstudent where stu_id"+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select rollno from teacherstudent where stu_id"+str(id))
                    r=my_cursor.fetchone()
                    r="+".join(r)

                    my_cursor.execute("select dep from teacherstudent where stu_id"+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)

                    my_cursor.execute("select stu_id from teacherstudent where stu_id"+str(id))
                    i=my_cursor.fetchone()
                    i="+".join(i)


                    if confidence>40:
                        print("aaaa")
                        cv2.putText(img,f"stu_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),thickness=3)
                        cv2.putText(img,f"rollno:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),thickness=3)
                        cv2.putText(img,f"stu_name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),thickness=3)  
                        cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),thickness=3)        
                        # #self.mark_attandence(i,r,n,d)
                    else:
                        print("bbbbbbbb")
                        cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3,0,0,0)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,y]

                return coord
            
            def recongnize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
                

            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recongnize(img,clf,faceCascade)
                cv2.imshow("Welcome To Look In",img)

                # if cv2.waitkey(1)==13:
                #     break
            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


            

        


if __name__ == '__main__':#main
 
    root=Tk()#calling root
    obj=Face_recognize(root)#making class object
    root.mainloop()#for end
