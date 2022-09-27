from optparse import Values
from turtle import Screen, screensize
import pymysql
from tkinter import Entry, IntVar,Label,Button, StringVar,Tk

mydb=pymysql.connect(host="localhost",user="root",password="",database="python_db1")


cur=mydb.cursor()

cur.execute("create table if not exists student(id int primary key AUTO_INCREMENT, name varchar(20),subject varchar(20))")
mydb.commit()

screen=Tk()
screen.geometry("500x500")

var_ename=StringVar()
var_subject=StringVar()
var_id=IntVar()


def insertData():
    query="insert into student(name,subject) values('%s','%s')"
    values=(var_ename.get(),var_subject.get())

    cur.execute(query%values)
    print("Insert Data Called ")
    mydb.commit()

def deleteData():
    query="delete from student where id= %s"
    Values=(var_id.get())
    cur.execute(query,Values)
    print("data deleted")
    mydb.commit()

lbl_name=Label(screen,text="Enter name:")
lbl_name.place(x=10,y=10)

lbl_subject=Label(screen,text="Enter subject:")
lbl_subject.place(x=10,y=60)

btn=Button(screen,text="Submit",width=6,height=1,font=('arial',12,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=insertData)
btn.place(x=150,y=100)


ename=Entry(screen,textvariable=var_ename)
ename.place(x=150,y=10)

esubject=Entry(screen,textvariable=var_subject)
esubject.place(x=150,y=60)

lbl_id=Label(screen,text="Enter id for delete:")
lbl_id.place(x=10,y=200)

idbox=Entry(screen,textvariable=var_id)
idbox.place(x=150,y=200)

btn=Button(screen,text="Delete",width=6,height=1,font=('arial',12,'bold'),command=deleteData)
btn.place(x=180,y=195)


screen.mainloop()