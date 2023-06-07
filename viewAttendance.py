from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
import csv


mydata=[]

class view_attendance:
    def __init__(self,root):#calling constructor(root(window name))
        self.root=root#intialize root
        self.root.geometry("1430x690+0+0")#width and height(starting point)
        self.root.title("face recognization System")#window title


        self.var_atten_id=StringVar()
        self.var_atten_rollno=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_data=StringVar()
        self.var_atten_attendace=StringVar()

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

        title_lbl=Label(bg_img,text="VIEW ATTENDANCE",font=("times new roman",40,"bold"),bg="white",fg="black")#LABLE ON BG IMAGE
        title_lbl.place(x=0,y=0,width=1300,height=45)
       
        img4=Image.open(r"C:\Users\ashok\OneDrive\Desktop\facepython\image\student.jpg")
        img4=img4.resize((500,130),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg4=ImageTk.PhotoImage(img4)#storing image into variable
       

       
        #========================MAIN FRAME================================
        main_frame=Frame(bg_img,bd=6)
        main_frame.place(x=0,y=50,width=1350,height=610)


        atten=Image.open(r"image\dark.jpg")
        atten=atten.resize((800,300),Image.ANTIALIAS)#antilias covert high level image into low level
        self.photoimg10=ImageTk.PhotoImage(atten)#storing image into variable

        first_lbl=Label(self.root,image=self.photoimg10)#to set lebel
        first_lbl.place(x=-20,y=160,width=720,height=120)
        #=====================left side lable=========


        left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,bg="white",text="STUDENT AATENDANCE DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=140,width=1000,height=500)




        # #current course
        # current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        # current_course_frame.place(x=5,y=0,width=920,height=150)

        attendancenId_label=Label(left_frame,text="AttendanceID",textvariable=self.var_atten_attendace,font=("times new roman",13,"bold"))
        attendancenId_label.grid(row=0,column=0,padx=10,pady=8,sticky=W)

        attendancenId_entry=ttk.Entry(left_frame,width=20,font=("times new roman",13,"bold"))
        attendancenId_entry.grid(row=0,column=1,padx=10,pady=8,sticky=W)
#=================================================================================
        rollno_label=Label(left_frame,text="Roll Number",font=("times new roman",13,"bold"))
        rollno_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        rollno_entry=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_rollno,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=0,column=3,padx=10,pady=8,sticky=W)
#=======================================================================

        name_label=Label(left_frame,text="Name",font=("times new roman",13,"bold"))
        name_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)

        name_entry=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)

  #============================================================================    

        dep_label=Label(left_frame,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=1,column=2,padx=10,pady=8,sticky=W)

        dep_entry=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=8,sticky=W)
#=================================================================================
        time_label=Label(left_frame,text="Time",font=("times new roman",13,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        time_entry=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=8,sticky=W)

#====================================================================================

        date_label=Label(left_frame,text="Date",font=("times new roman",13,"bold"))
        date_label.grid(row=2,column=2,padx=10,pady=8,sticky=W)

        date_entry=ttk.Entry(left_frame,width=20,textvariable=self.export_data,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        status_label=Label(left_frame,text="Status",font=("times new roman",13,"bold"))
        status_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        gen_combo=ttk.Combobox(left_frame,textvariable=self.var_atten_attendace,font=("times new roman",12,"bold"),state="randomly",width=20)
        gen_combo["values"]=("status","Present","Absent")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=2,pady=8,sticky=W)
#--------------------------------------------------------------------------------

        btn_frame=Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=220,width=920,height=70)


        save_btn=Button(btn_frame,text="Import",command=self.import_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        # #==========================update=================
        # update_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_btn.grid(row=0,column=1)
        # #==================delete=======================
        # delete_btn=Button(btn_frame,text="Delete",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # delete_btn.grid(row=0,column=2)
        # #=====================reset====================
        # reset_btn=Button(btn_frame,text="Reset",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # reset_btn.grid(row=0,column=3)
       
        #=====================right frame==================
       
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,bg="white",text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=700,y=10,width=550,height=500)


        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=530,height=430)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("stu_id","rollno","dep","time","date","attendance"),xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=X)


        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("stu_id",text="Attendance ID")
        self.AttendanceReportTable.heading("rollno",text="Roll Number")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance ")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("stu_id",width=100)
        self.AttendanceReportTable.column("rollno",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        # self.AttendanceReportTable.heading("stu_id",text="Attendance ID")
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def import_data(self):
        global mydata
        mydata.clear
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*csv"),("All Files"),"*.*"),parent=self.root)#corrent working directory
        with open(fln) as myfile:
            csv_read=csv.reader(myfile,delimeter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetch_data(mydata)
           


#export csv
    def export_data(self):
         try:
             if len(mydata)<1:
                 messagebox.showerror("No Data","No Data Found",parent=self.root)
             return False
         
             fln=filedialog.asksaveasfile(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*csv"),("All Files"),"*.*"),parent=self.root)
             with open(fln,mode="W",newline="") as myfile:
                 exp_writer=csv.writer(myfile,delimiter=",")
                 for i in mydata:
                     exp_write=writerow(i)
                     exp_write.append(i)
                 messagebox.showinfo("Data Export","your Data exported to "+os.path.basename(fln)+"succesfull")
         except Exception as es:
             messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cusor_row=self.AttendanceReportTable.focus()
        contant=self.AttendanceReportTable.item(cusor_row)
        rows=contant['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_rollno.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_attendace.set(rows[5])
         

    

            


  



      
if __name__ == '__main__':#main
    root=Tk()#calling root
    obj=view_attendance(root)#making class object
    root.mainloop()#for end


