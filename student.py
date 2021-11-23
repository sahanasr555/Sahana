from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student management System")

        img=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p1.png")
        img=img.resize((1600,900),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        title_lbl=Label(f_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=30,y=0,width=1200)

        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=7,y=70,width=1258,height=550)

        #Lft label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",18,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=520)

        img_left=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p11.jpg")
        img_left=img_left.resize((590,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        L_lbl=Label(self.root,image=self.photoimg_left)
        L_lbl.place(x=30,y=115,width=590,height=150)

        #current frame
        Curr_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",13,"bold"))
        Curr_frame.place(x=8,y=160,width=590,height=100)

        #dept label
        dept_lbl=Label(Curr_frame,text="Department",font=("times new roman",13))
        dept_lbl.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(Curr_frame,font=("times new roman",13),width=30,state="readonly")
        dept_combo["values"]=('Select Department','Computer Science & Engineering ','Electronics & Communication','Electical & Electronics','Mechanical Engineering','Civil Engineering')
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=6,sticky=W)

        #Year label
        sem_lbl=Label(Curr_frame,text="Semester",font=("times new roman",13))
        sem_lbl.grid(row=1,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Curr_frame,font=("times new roman",13),width=30,state="readonly")
        sem_combo["values"]=('Select Sem','I ','II','III','IV','V','VI','VII','VIII')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)

        #class student information
        Class_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman",13,"bold"))
        Class_frame.place(x=8,y=250,width=590,height=195)

        #usn
        usn=Label(Class_frame,text="USN:",font=("times new roman",13))
        usn.place(x=10,y=10)

        usn.txtuser=ttk.Entry(Class_frame,font=("times new roman",13))
        usn.txtuser.place(x=117,y=10,width=230,height=28)

        #Name
        name=Label(Class_frame,text="Name:",font=("times new roman",13))
        name.place(x=10,y=50)

        name.txtuser=ttk.Entry(Class_frame,font=("times new roman",13))
        name.txtuser.place(x=117,y=50,width=230,height=28)

        #division
        div=Label(Class_frame,text="Division:",font=("times new roman",13))
        div.place(x=10,y=90)

        div_combo=ttk.Combobox(Class_frame,font=("times new roman",13),width=30,state="readonly")
        div_combo["values"]=('Select Div','A','B')
        div_combo.current(0)
        div_combo.place(x=117,y=90,width=230,height=28)

        #Roll number
        roll=Label(Class_frame,text="Phone no. :",font=("times new roman",13))
        roll.place(x=10,y=130)

        roll.txtuser=ttk.Entry(Class_frame,font=("times new roman",13))
        roll.txtuser.place(x=117,y=130,width=230,height=28)

        #radio buttons
        radionbtn1=ttk.Radiobutton(Class_frame,text=("Take a photo sample"),value="Yes")
        radionbtn1.place(x=370,y=13)

        take_button=Button(Class_frame,text="Take Photo",width=10,font=("times new roman",13,"bold"),bg="Darkblue",fg="white")
        take_button.place(x=385,y=46)

        update_button=Button(Class_frame,text="Update Photo",width=10,font=("times new roman",13,"bold"),bg="Darkblue",fg="white")
        update_button.place(x=385,y=88)


        radionbtn2=ttk.Radiobutton(Class_frame,text=("No photo sample"),value="Yes")
        radionbtn2.place(x=370,y=133)

        save_button=Button(Left_frame,text="Save",width=10,font=("times new roman",13,"bold"),bg="Darkblue",fg="white")
        save_button.place(x=1,y=448)

        update_button=Button(Left_frame,text="Update",width=10,font=("times new roman",13,"bold"),bg="Darkblue",fg="white")
        update_button.place(x=132,y=448)

        delete_button=Button(Left_frame,text="Delete",width=10,font=("times new roman",13,"bold"),bg="Darkblue",fg="white")
        delete_button.place(x=263,y=448)

        reset_button=Button(Left_frame,text="Reset",width=10,font=("times new roman",13,"bold"),bg="Darkblue",fg="white")
        reset_button.place(x=393,y=448)

        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"))
        Right_frame.place(x=630,y=10,width=610,height=520)












if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
