from cProfile import label
from lib2to3.pgen2.token import DOUBLESLASH
import tkinter
from turtle import Screen

screen=tkinter.Tk()

 #  W X H

screen.geometry("1000x500")

screen.configure(bg="grey")


# tkinter variable

var_ename_id=tkinter.StringVar() # it accept value in string


def myfun():
    print("welcome")
    print("value from entry=",var_ename_id.get())

# lable

lbl=tkinter.Label(screen,text="Welcome to Komal Webpage",font=("arial",26,"bold"),bg="grey",fg="blue",)

lbl.place(x=80,y=10)


#lable
lbl_name=tkinter.Label(screen,text="Enter your name:",font=("arial",10,"bold"),bg="grey")
lbl_name.place(x=20,y=80)

#entry(textview)

e1=tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=160,y=80)

#button

btn=tkinter.Button(screen,text="Submit",font=("arial",10,"bold"),bg="grey",command=myfun)
btn.place(x=300,y=80)

screen.mainloop()

