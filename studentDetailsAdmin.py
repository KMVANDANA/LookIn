from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv

class Student_Admin:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1530x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title
       # self.root.wm.iconbitmap("icon.ico")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_division=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_address=StringVar()
        self.var_teachername=StringVar()
        
        img3=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\code.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg3=ImageTk.PhotoImage(img3)#storing image into variable

        bg_img=Label(self.root,image=self.photoimg3)#to set lebel
        bg_img.place(x=0,y=-5,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1400,height=45)

        #========================MAIN FRAME================================
        main_frame=Frame(bg_img,bd=6)
        main_frame.place(x=0,y=50,width=1350,height=610)

        #=====================left side lable=========
        left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,bg="white")
        left_frame.place(x=10,y=50,width=1000,height=500)

        #=====================right frame==================
       
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,bg="white")
        right_frame.place(x=700,y=50,width=550,height=500)

        #======================current course information===============

        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=30,width=920,height=120)

        #------------------DEPARTMENT-------------------

        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")

        dep_lable.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("select department","Btech","Bpharma","MCA","MBA","Msc","Bsc")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        #
        #-----------------------YEAR---------------------------------

        year_lable=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="randomly",width=20)
        year_combo["values"]=("select","2023-2024","2022-2023","2021-2020")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)

        #--------------------------------COURSE--------------------------

        course_lable=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="randomly",width=20)
        course_combo["values"]=("select","EC","CS","civil","AI AND ML")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=6,sticky=W)

        #=---------------------semester----------------------------

        sem_lable=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_lable.grid(row=1,column=2,padx=10)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="randomly",width=20)
        sem_combo["values"]=("select","I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=6,sticky=W)

    #---------------------CLASS STUDENT INFORMATION--------------------

        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=160,width=920,height=320)      

          #-------------------Student Id-------------------
        studentId_label=Label(class_student_frame,text="StudentId",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=6,sticky=W)


       #------------------------------student Name-------------------------------

        studentId_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=2,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_name,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=3,padx=10,pady=6,sticky=W)

     #--------------------------Class Division------------------------
        studentId_label=Label(class_student_frame,text="Class Division",font=("times new roman",13,"bold"))
        studentId_label.grid(row=1,column=0,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_division,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=1,padx=10,sticky=W)
    
    #-----------------------------Roll Number----------------------
        studentId_label=Label(class_student_frame,text="Roll Number",font=("times new roman",13,"bold"))
        studentId_label.grid(row=1,column=2,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=3,padx=10,pady=6,sticky=W)

    #-----------------------------Gender------------------------

        studentId_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"))
        studentId_label.grid(row=2,column=0,padx=10,pady=6,sticky=W)

        gen_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="randomly",width=20)
        gen_combo["values"]=("select","male","female")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=2,pady=6,sticky=W)

         #----------------DOB--------------------------------------
        studentId_label=Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"))
        studentId_label.grid(row=2,column=2,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=2,column=3,padx=10,pady=6,sticky=W)

        #-------------------Email----------------------------------
        studentId_label=Label(class_student_frame,text="Email",font=("times new roman",13,"bold"))
        studentId_label.grid(row=3,column=0,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=3,column=1,padx=10,pady=6,sticky=W)

        #------------------------phone number------------------------
        studentId_label=Label(class_student_frame,text="Phone Number",font=("times new roman",13,"bold"))
        studentId_label.grid(row=3,column=2,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=3,column=3,padx=10,pady=6,sticky=W)

        #-------------------------------Address----------------------
        studentId_label=Label(class_student_frame,text="Address",font=("times new roman",13,"bold"))
        studentId_label.grid(row=4,column=0,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=4,column=1,padx=10,pady=6,sticky=W)

        #------------------------------Teacher Name------------------
        studentId_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",13,"bold"))
        studentId_label.grid(row=4,column=2,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_teachername,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=4,column=3,padx=10,pady=6,sticky=W)


        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=220,width=920,height=35)

        #===========button with the help of button=========

    #===========================save====================
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        #==========================update=================
        update_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        #==================delete=======================
        delete_btn=Button(btn_frame,text="Delete",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        #=====================reset====================
        reset_btn=Button(btn_frame,text="Reset",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        

#======================================RIGHT FRAME==============================
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,bg="white")
        right_frame.place(x=700,y=50,width=550,height=500)

        #-----------------------------searching system------------------------
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=0,width=530,height=80)

        #=============================search by====================

        search_label=Label(search_frame,text="Search By :",font=("times new roman",13,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="randomly",width=10)
        search_combo["values"]=("select","StudentId","Student Name","Roll Number","Class Division")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=6,sticky=W)

        search_btn=Button(search_frame,text="Search",width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=2,padx=3)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=3)

        showAll_btn=Button(search_frame,text="ShowAll",width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)
     #==========================table frame
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=80,width=530,height=400)
    #===========================scroll bar======================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.adminstudent_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Gender","DOB","Division","Stu_id","Stu_name","Rollno.","E-mail","Phone","Address","Teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.adminstudent_table.xview)
        scroll_y.config(command=self.adminstudent_table.yview)

        self.adminstudent_table.heading("Department",text="Department")
        self.adminstudent_table.heading("Course",text="Course")
        self.adminstudent_table.heading("Year",text="Year")
        self.adminstudent_table.heading("Semester",text="Semester")
        self.adminstudent_table.heading("Gender",text="Gender")
        self.adminstudent_table.heading("DOB",text="DOB")
        self.adminstudent_table.heading("Division",text="Division")
        self.adminstudent_table.heading("Stu_id",text="Stu_id")
        self.adminstudent_table.heading("Stu_name",text="Stu_name")
        self.adminstudent_table.heading("Rollno.",text="Roll_number")
        self.adminstudent_table.heading("E-mail",text="E-mail")
        self.adminstudent_table.heading("Phone",text="Phone")
        self.adminstudent_table.heading("Address",text="Address")
        self.adminstudent_table.heading("Teacher",text="Teacher")

        self.adminstudent_table["show"]="headings"
        self.adminstudent_table.pack(fill=BOTH,expand=1)

        #-------------------To set width-----------------
        self.adminstudent_table.column("Department",width=100)
        self.adminstudent_table.column("Course",width=100)
        self.adminstudent_table.column("Year",width=100)
        self.adminstudent_table.column("Semester",width=100)
        self.adminstudent_table.column("Stu_id",width=100)
        self.adminstudent_table.column("Stu_name",width=100)
        self.adminstudent_table.column("Division",width=100)
        self.adminstudent_table.column("Rollno.",width=100)
        self.adminstudent_table.column("Gender",width=100)
        self.adminstudent_table.column("DOB",width=100)
        self.adminstudent_table.column("E-mail",width=100)
        self.adminstudent_table.column("Phone",width=100)
        self.adminstudent_table.column("Address",width=100)
        self.adminstudent_table.column("Teacher",width=100)
        
        self.adminstudent_table.pack(fill=BOTH,expand=1)
        self.adminstudent_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
         if self.var_dep.get()=="Select Department" or self.var_stu_id.get()=='' or self.var_stu_name.get()=='':
               messagebox.showerror("Error","All field Are required",parent=self.root)
         else:
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into adminstudent values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                  
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_division.get(),
                                                                                                                self.var_stu_id.get(),
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_roll_no.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phoneno.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teachername.get(),
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                    ))
               
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success ","student details has been added successfully",parent=self.root)                                                                                               
             except Exception as es:
                messagebox.showerror("Error",f"(Due To:{str(es)}",parent=self.root)
    
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from adminstudent")
         data2=my_cursor.fetchall()

         if len(data2)!=0:
             self.adminstudent_table.delete(*self.adminstudent_table.get_children())
             for i in data2:
                 self.adminstudent_table.insert("",END,values=i)
             conn.commit()
         conn.close()    

    #=======================get cursor======================
    def get_cursor(self,event=""):
        cursor_focus=self.adminstudent_table.focus()
        content=self.adminstudent_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_gender.set(data[4]),
        self.var_dob.set(data[5]),
        self.var_division.set(data[6]),
        self.var_stu_id.set(data[7]),
        self.var_stu_name.set(data[8]),
        self.var_roll_no.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phoneno.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teachername.set(data[13]),
        self.var_radio1.set(data[14])
             
    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_stu_id.get()=='' or self.var_stu_name.get()=='':
            messagebox.showerror("Error","All field Are required",parent=self.root)

         else:
             try:
                Update=messagebox.askyesno("Update","Do you Want To Update",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update teacherstudent set dep=%s,course=%s,year=%s,semester=%s,gender=%s,dob=%s,division=%s,stu_name=%s,rollno=%s,email=%s,phoneno=%s,address=%s,teachername=%s,photosample=%s where stu_id=%s",(
                                                                                                                  
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_division.get(),
                                                                                                              
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_roll_no.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phoneno.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teachername.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_stu_id.get()
                                                                                                               
                                                                                                                
                                                                                                                
                                                                                                                    ))
                     
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","Student Details update successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
             except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
      
 #====================================delete==================
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student id must required",parant=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","do you want to delete student",parent=self.root)
                if delete>0:
                    
                     conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
                     my_cursor=conn.cursor()
                     sql="delete from teacherstudent where stu_id=%s"
                     val=(self.var_stu_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def reset_data(self):
       
        self.var_dep.set("select department")
        self.var_course.set("select "),
        self.var_year.set("select"),
        self.var_semester.set("select "),
        self.var_gender.set("select"),
        self.var_dob.set(""),
        self.var_division.set("select "),
        self.var_stu_id.set(""),
        self.var_stu_name.set(""),
        self.var_roll_no.set(""),
        self.var_email.set(""),
        self.var_phoneno.set(""),
        self.var_address.set(""),
        self.var_teachername.set(""),
        self.var_radio1.set("")                                                                          
#================================Generate data set or take photo sample===============
    def gen_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_id.get()=='' or self.var_stu_name.get()=='':
            messagebox.showerror("Error","All field Are required",parent=self.root)

        else:
            try:
                 
              conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
              my_cursor=conn.cursor()
              my_cursor.execute("select *from teacherstudent")
              myresult=my_cursor.fetchall()
              id=0
              for x in myresult:
                id+=1
                my_cursor.execute("update teacherstudent set dep=%s,course=%s,year=%s,semester=%s,gender=%s,dob=%s,division=%s,stu_name=%s,rollno=%s,email=%s,phoneno=%s,address=%s,teachername=%s where stu_id=%s",(
                                                                                                                  
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_division.get(),
                                                                                                              
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_roll_no.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phoneno.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teachername.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_stu_id.get()==+1
                                                                                                               
                                                                                                                
                                                                                                                
                                                                                                                    ))
              
              
              
              conn.commit()
              self.fetch_data()
              self.reset_data()
              conn.close()
#===========================Load Predefine data on face forntals opencv
             
              face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

              def face_cropped(img):
                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
                 faces=face_classifier.detectMultiScale(gray,1.3,5)
                #1.3=scaling factor
                #minimum neighbor=5

                 for(x,y,w,h) in faces:
                     face_cropped=img[y:y+h,x:x+w]
                     return face_cropped
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while(True):
                     ret,myframe=cap.read()
                     if face_cropped(myframe) is not None:
                         img_id+=1
                     face=cv2.resize(face_cropped(myframe),(450,450))
                     face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                     file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                     cv2.imwrite(file_path)
                     cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),2)
                     cv2.imshow("Cropped Face",face)

                     if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("Result","Generating data sets Compled:")

            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        def open_img(self):
            os.startfile("data")
      
       


                   
       
if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Student_Admin(root)#making class object
    root.mainloop()#for end