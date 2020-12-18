#!/usr/bin/env python
# coding: utf-8

# In[26]:


from tkinter import *
from tkinter import messagebox
import os
import mysql.connector


def Ok():
    uname=e1.get()
    password=e2.get()
    
    if(uname=="" and password==""):
        messagebox.showinfo("","blanck not allowed")
    elif(uname=="18-bec-011" and password=="2005-05-20"):
        messagebox.showinfo("","login success")
        rollno=uname
        con=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        print("connection successful")
        cur=con.cursor()
        query="select * from student_data where rollnumber='18-bec-011'"
        cur.execute(query)
        res=cur.fetchall()
        for i in res:
            print(i)
        root.destroy()
    else:
        messagebox.showinfo("","incorrect username and passwword")
        
def admin():
    global g1
    global g2
    
    def submit():
        adminname=g1.get()
        adminpassword=g2.get()
        
        if(adminname=="" and adminpassword==""):
            messagebox.showinfo("please enter the credentials")
        elif(adminname=="admin" and adminpassword=="123"):
            def store():
                result = int(e1.get()) + int(e2.get()) + int(e3.get())+int(e4.get())+int(e5.get())
                totText.set(result)

                average = result/5
                avgText.set(average)

                if (average > 50):
                    grade = "pass"
                else:
                    grade = "fail"

                gradeText.set(grade)
                rollnumber=r.get()
                dob=d.get()
                marks1=e1.get()
                marks2=e2.get()
                marks3=e3.get()
                marks4=e4.get()
                marks5=e5.get()
                con=mysql.connector.connect(host="localhost",user="root",password="anuj@2001",database="python")
                print("connection successful")
                cur=con.cursor()
                query="insert into student_data(rollnumber,dob,marks1,marks2,marks3,marks4,marks5) values(%s,%s,%s,%s,%s,%s,%s)"
                b1=(rollnumber,dob,marks1,marks2,marks3,marks4,marks5)
                cur.execute(query,b1)
                con.commit()
                messagebox.showinfo("data store successfully")
                root.destroy()
                        
            root = Tk()
            root.title("Student Marks Calculation System")
            root.geometry("400x600")

            global r
            global d
            global e1
            global e2
            global e4
            global e5
            global totText
            global avgText
            global gradeText

            totText = StringVar()
            avgText = StringVar()
            gradeText = StringVar()

            Label(root,text="Roll No.").place(x=10,y=10)
            Label(root,text="DOB").place(x=10,y=40)
            Label(root, text="Python").place(x=10, y=80)
            Label(root, text="Compiler").place(x=10, y=120)
            Label(root, text="CO").place(x=10, y=160)
            Label(root, text="CN").place(x=10, y=200)
            Label(root, text="Graph Theory").place(x=10, y=240)
            Label(root, text="Total:").place(x=10, y=280)
            Label(root, text="Avg:").place(x=10, y=320)
            Label(root, text="Grade:").place(x=10, y=360)


            r=Entry(root)
            r.place(x=100,y=10)

            d=Entry(root)
            d.place(x=100,y=40)

            e1 = Entry(root)
            e1.place(x=100, y=80)

            e2 = Entry(root)
            e2.place(x=100, y=120)

            e3 = Entry(root)
            e3.place(x=100, y=160)

            e4 = Entry(root)
            e4.place(x=100, y=200)

            e5 = Entry(root)
            e5.place(x=100, y=240)

            result = Label(root, text="", textvariable=totText).place(x=100, y=280)
            avg = Label(root, text="", textvariable=avgText).place(x=100, y=320)
            grade = Label(root, text="", textvariable=gradeText).place(x=100, y=360)

            Button(root, text="store", command=store ,height = 3, width =13).place(x=10, y=400)
            root.destroy()
            root.mainloop()
            
        else:
            messagebox.showinfo("you have enter wrong credentials")
        root.destroy()
    
    root=Tk()
    root.title("Admin")
    root.geometry("300x400")
    
    Label(root,text="username").place(x=10,y=10)
    Label(root,text="password").place(x=10,y=40)

    g1=Entry(root)
    g1.place(x=100,y=10)

    g2=Entry(root)
    g2.place(x=100,y=40)

    Button(root,text="submit",command=submit,height=3,width=13).place(x=10,y=100)    
     
    root.mainloop()
    
    
root=Tk()
root.title("Login")
root.geometry("300x200")
#root.state("zoomed")

global e1
global e2



Label(root,text="Roll No.").place(x=10,y=10)
Label(root,text="DOB").place(x=10,y=40)

e1=Entry(root)
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)

Button(root,text="login",command=Ok,height=3,width=13).place(x=10,y=100)
Button(root,text="Admin",command=admin,height=3,width=13).place(x=160,y=100)
root.mainloop()


# In[ ]:





# In[ ]:




