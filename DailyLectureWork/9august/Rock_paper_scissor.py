import tkinter
import random

screen =tkinter.Tk()
screen.title("ROCK PAPER SCISSOR")
screen.geometry("500x500")

var_user_choice=tkinter.StringVar()
var_computer_choice=tkinter.StringVar()
var_result_choice=tkinter.StringVar()
sum=0
sum1=0
var_final_result=tkinter.StringVar()
game_list=["ROCK","PAPER","SCISSOR"]

def myfun(msg):
    global sum
    global sum1
    var_user_choice.set(msg)
    com=random.choice(game_list)
    var_computer_choice.set(com)
    if msg==com:
        var_result_choice.set("TIE")
    else:
        if (msg=="PAPER" and com=="STONE") or (msg=="SCISSOR" and com=="PAPER") or (msg=="STONE" and com=="SCISSOR"):
            var_result_choice.set("USER WON")
            sum+=1
            user_score.config(text=sum)
            
            
        else:
            var_result_choice.set("COMPUTER WON")

            sum1+=1
            Computer_score.config(text=sum1)
    
           
btn= tkinter.Button(screen,text="ROCK",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("ROCK"))
btn.place(x=10,y=10)

btn= tkinter.Button(screen,text="PAPER",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("PAPER"))
btn.place(x=150,y=10)

btn= tkinter.Button(screen,text="SCISSOR",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("SCISSOR"))
btn.place(x=300,y=10)

user = tkinter.Label(screen,text="USER",font=('arial',14,'bold'),bg="black",fg="white")
user.place(x=10,y=150)

computer= tkinter.Label(screen,text="COMPUTER",font=('arial',14,'bold'),bg="black",fg="white")
computer.place(x=10,y=200)


user = tkinter.Label(screen,textvariable=var_user_choice,font=('arial',14,'bold'),bg="pink",fg="white")
user.place(x=150,y=150)

computer= tkinter.Label(screen,textvariable=var_computer_choice,font=('arial',14,'bold'),bg="pink",fg="white")
computer.place(x=150,y=200)


btn= tkinter.Button(screen,textvariable=var_result_choice,font=('arial',20,'bold'),bg="black",fg="white",width=25)
btn.place(x=10,y=350)

user_score = tkinter.Label(screen,text="sum",font=('arial',14,'bold'),bg="black",fg="white")
user_score.place(x=300,y=150)

Computer_score = tkinter.Label(screen,text="sum1",font=('arial',14,'bold'),bg="black",fg="white")
Computer_score.place(x=300,y=200)


btn= tkinter.Button(screen,textvariable=var_result_choice,font=('arial',20,'bold'),bg="black",fg="white",width=25)
btn.place(x=10,y=420)
screen.mainloop()