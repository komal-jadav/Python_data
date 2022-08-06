from multiprocessing.sharedctypes import Value
import tkinter

screen=tkinter.Tk()
suml=0
sumd=0

screen.geometry("500x500")

screen.configure(bg="pink")

var_ename_id=tkinter.IntVar() # it accept value in string


def like():
    global suml
    suml +=1
    lbl_L.config(text=suml)

def dislike():
    global sumd
    sumd +=1
    lbl_D.config(text=sumd)
 

# lable

lbl_name=tkinter.Label(screen,text="Welcome to tkinter",font=("arial",26,"bold"),bg="grey",fg="blue")

lbl_name.place(x=80,y=10)



#entry(textview)

e1=tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=160,y=80)

#button

btn=tkinter.Button(screen,text="Like",font=("arial",10,"bold"),bg="grey",command=like)
btn.place(x=160,y=100)

btn1=tkinter.Button(screen,text="Dis-Like",font=("arial",10,"bold"),bg="grey",command=dislike)
btn1.place(x=240,y=100)

lbl_L=tkinter.Label(screen,text=suml,font=("arial",10,"bold"),bg="grey")
lbl_L.place(x=160,y=150)

lbl_D=tkinter.Label(screen,text=sumd,font=("arial",10,"bold"),bg="grey")
lbl_D.place(x=200,y=150)


screen.mainloop()


