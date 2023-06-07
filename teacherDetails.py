from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Teacher_Admin:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1530x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title
        #self.root.wm.iconbitmap("icon.ico")
        #-----------------------------------------variable----------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_Teacher_id=StringVar()
        self.var_Teacher_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
        img3=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\code.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg3=ImageTk.PhotoImage(img3)#storing image into variable

        bg_img=Label(self.root,image=self.photoimg3)#to set lebel
        bg_img.place(x=0,y=-5,width=1530,height=710)

        title_lbl=Label(bg_img,text="TEACHER DETAILS",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
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

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=920,height=150)

        #------------------DEPARTMENT-------------------

        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")

        dep_lable.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("select department","Btech","Bpharma","MCA","MBA","Msc","Bsc")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
         #--------------------------------COURSE--------------------------

        course_lable=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="randomly",width=20)
        course_combo["values"]=("select","EC","CS","civil","AI AND ML")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=6,sticky=W)

        #
        #-----------------------YEAR---------------------------------

        year_lable=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="randomly",width=20)
        year_combo["values"]=("select","2023-2024","2022-2023","2021-2020")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)

       
        #=---------------------semester----------------------------

        sem_lable=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_lable.grid(row=1,column=2,padx=10)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="randomly",width=20)
        sem_combo["values"]=("select","I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=6,sticky=W)

    #---------------------CLASS TEACHER INFORMATION--------------------

        class_teacher_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Information",font=("times new roman",12,"bold"))
        class_teacher_frame.place(x=5,y=160,width=920,height=320)      

         #-------------------teacher Id-------------------
        teacherId_label=Label(class_teacher_frame,text="Teacher Id",font=("times new roman",13,"bold"))
        teacherId_label.grid(row=0,column=0,padx=10,pady=6,sticky=W)

        teacherId_entry=ttk.Entry(class_teacher_frame,textvariable=self.var_Teacher_id,width=20,font=("times new roman",13,"bold"))
        teacherId_entry.grid(row=0,column=1,padx=10,pady=6,sticky=W)


       #------------------------------Teacher Name-------------------------------

        teacherId_label=Label(class_teacher_frame,text="Teacher Name",font=("times new roman",13,"bold"))
        teacherId_label.grid(row=0,column=2,padx=10,pady=6,sticky=W)

        teacherId_entry=ttk.Entry(class_teacher_frame,textvariable=self.var_Teacher_name,width=20,font=("times new roman",13,"bold"))
        teacherId_entry.grid(row=0,column=3,padx=10,pady=6,sticky=W)

     #--------------------------GENDER------------------------
        teacherId_label=Label(class_teacher_frame,text="Email",font=("times new roman",13,"bold"))
        teacherId_label.grid(row=1,column=0,padx=10,pady=6,sticky=W)

        studentId_entry=ttk.Entry(class_teacher_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=1,padx=10,sticky=W)
    
    #-----------------------------DOB----------------------
        studentId_label=Label(class_teacher_frame,text="DOB",font=("times new roman",13,"bold"))
        studentId_label.grid(row=1,column=2,padx=10,pady=6,sticky=W)

        teacherId_entry=ttk.Entry(class_teacher_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        teacherId_entry.grid(row=1,column=3,padx=10,pady=6,sticky=W)

    #-----------------------------Gender-----------------------

        teacherId_label=Label(class_teacher_frame,text="Gender",font=("times new roman",13,"bold"))
        teacherId_label.grid(row=2,column=0,padx=10,pady=6,sticky=W)

        gen_combo=ttk.Combobox(class_teacher_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="randomly",width=20)
        gen_combo["values"]=("select","male","female")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=2,pady=6,sticky=W)

         #----------------phone number--------------------------------------
        studentId_label=Label(class_teacher_frame,text="Phone Number",font=("times new roman",13,"bold"))
        studentId_label.grid(row=2,column=2,padx=10,pady=6,sticky=W)

        teacherId_entry=ttk.Entry(class_teacher_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        teacherId_entry.grid(row=2,column=3,padx=10,pady=6,sticky=W)

        #-------------------Address----------------------------------
        teacherId_label=Label(class_teacher_frame,text="Address",font=("times new roman",13,"bold"))
        teacherId_label.grid(row=3,column=0,padx=10,pady=6,sticky=W)

        teacherId_entry=ttk.Entry(class_teacher_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        teacherId_entry.grid(row=3,column=1,padx=10,pady=6,sticky=W)

       
       

       
        #=======================button frame==========================

        btn_frame=Frame(class_teacher_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=220,width=920,height=70)

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
        search_combo["values"]=("select","Teacher Id","Teacher Name")
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

        self.adminteacher_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Teacher_id","Teacher_name","Gender","DOB","E-mail","Phone","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.adminteacher_table.xview)
        scroll_y.config(command=self.adminteacher_table.yview)

        self.adminteacher_table.heading("Department",text="Department")
        self.adminteacher_table.heading("Course",text="Course")
        self.adminteacher_table.heading("Year",text="Year")
        self.adminteacher_table.heading("Semester",text="Semester")
        self.adminteacher_table.heading("Teacher_id",text="Teacher_id")
        self.adminteacher_table.heading("Teacher_name",text="Teacher_name")
        self.adminteacher_table.heading("Gender",text="Gender")
        self.adminteacher_table.heading("DOB",text="DOB")
        self.adminteacher_table.heading("E-mail",text="E-mail")
        self.adminteacher_table.heading("Phone",text="Phone")
        self.adminteacher_table.heading("Address",text="Address")
        self.adminteacher_table["show"]="headings"

        self.adminteacher_table.pack(fill=BOTH,expand=1)

        #-------------------To set width-----------------
        self.adminteacher_table.column("Department",width=100)
        self.adminteacher_table.column("Course",width=100)
        self.adminteacher_table.column("Year",width=100)
        self.adminteacher_table.column("Semester",width=100)
        self.adminteacher_table.column("Teacher_id",width=100)
        self.adminteacher_table.column("Teacher_name",width=100)
     
        self.adminteacher_table.column("Gender",width=100)
        self.adminteacher_table.column("DOB",width=100)
        self.adminteacher_table.column("E-mail",width=100)
        self.adminteacher_table.column("Phone",width=100)
        self.adminteacher_table.column("Address",width=100)

        self.adminteacher_table.pack(fill=BOTH,expand=1)
        self.adminteacher_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
         if self.var_dep.get()=="Select Department" or self.var_Teacher_id.get()=='' or self.var_Teacher_name.get()=='':
            messagebox.showerror("Error","All field Are required",parent=self.root)
         else:
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into adminteacher values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                  
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_Teacher_id.get(),
                                                                                                                self.var_Teacher_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get()
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                    ))
               
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success ","teacher details has been added successfully",parent=self.root)                                                                                             
             except Exception as es:
                messagebox.showerror("Error",f"(Due To:{str(es)}",parent=self.root)
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="lookin@2023",database="lookin")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from adminteacher")
         data1=my_cursor.fetchall()

         if len(data1)!=0:
             self.adminteacher_table.delete(*self.adminteacher_table.get_children())
             for i in data1:
                 self.adminteacher_table.insert("",END,values=i)
             conn.commit()
         conn.close()                                                                              
                                                                                     
    def get_cursor(self,event=""):
        cursor_focus=self.adminteacher_table.focus()
        content=self.adminteacher_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_Teacher_id.set(data[4]),
        self.var_Teacher_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
                                                 
    
    #def add_data(self):
         



if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=Teacher_Admin(root)#making class object
    root.mainloop()#for end