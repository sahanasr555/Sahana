from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p1.png")
        img=img.resize((1600,900),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=30,y=0,width=1200)

        #======BUTTONS=====#
        img1=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p3.jpg")
        img1=img1.resize((220,220),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(f_lbl,image=self.photoimg1,cursor="hand2")
        b1.place(x=70,y=80,width=220,height=220)

        b1_1=Button(f_lbl,text="Student Details",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b1_1.place(x=70,y=300,width=220,height=40)

        img2=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p4.jpg")
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(f_lbl,image=self.photoimg2,cursor="hand2")
        b2.place(x=370,y=80,width=220,height=220)

        b2_1=Button(f_lbl,text="Face Detection",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b2_1.place(x=370,y=300,width=220,height=40)

        img3=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p5.jpg")
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(f_lbl,image=self.photoimg3,cursor="hand2")
        b3.place(x=670,y=80,width=220,height=220)

        b3_1=Button(f_lbl,text="Attendance",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b3_1.place(x=670,y=300,width=220,height=40)

        img4=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p6.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(f_lbl,image=self.photoimg4,cursor="hand2")
        b4.place(x=970,y=80,width=220,height=220)

        b4_1=Button(f_lbl,text="Help desk",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b4_1.place(x=970,y=300,width=220,height=40)

        img5=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p7.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(f_lbl,image=self.photoimg5,cursor="hand2")
        b5.place(x=70,y=360,width=220,height=220)

        b5_1=Button(f_lbl,text="Train data",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b5_1.place(x=70,y=580,width=220,height=40)
        
        img6=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p8.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(f_lbl,image=self.photoimg6,cursor="hand2")
        b6.place(x=370,y=360,width=220,height=220)

        b6_1=Button(f_lbl,text="Photos",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b6_1.place(x=370,y=580,width=220,height=40)
        
        img7=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p9.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(f_lbl,image=self.photoimg7,cursor="hand2")
        b7.place(x=670,y=360,width=220,height=220)

        b7_1=Button(f_lbl,text="Developer",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b7_1.place(x=670,y=580,width=220,height=40)
        
        img8=Image.open(r"C:\Users\Sahana\Desktop\Face_Recognition\images\p10.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b8=Button(f_lbl,image=self.photoimg8,cursor="hand2")
        b8.place(x=970,y=360,width=220,height=220)

        b8_1=Button(f_lbl,text="Exit",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="brown")
        b8_1.place(x=970,y=580,width=220,height=40)
        



        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
