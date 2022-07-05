#Number Guessing Game for when u got not right answer
"""
from operator import truediv
import random
Computer_Guess=random.randint(1,100)
status=True
while status:
    User_Guess=int(input("Enter no.:"))
    if User_Guess > Computer_Guess:
        print("HINT: Enter lower no.")
    elif User_Guess < Computer_Guess:
        print("HINT: Enter Higher:")
    else:
        print("You got it!!!")
        status = False

#Number Guessing game for only 5 times 
 
from operator import truediv
import random
Computer_Guess=random.randint(1,100)
trial=5
while trial>0:
    User_Guess=int(input("Enter no.:"))
    if User_Guess > Computer_Guess:
        print("HINT: Enter lower no.")
    elif User_Guess < Computer_Guess:
        print("HINT: Enter Higher:")
    else:
        print("You got it!!!")
        trial=0
    trial-=1


#example of wHILE LOOP
i=1
while i<=5:
    print(i,"Play Mario:")
    i+=1

#Enter subject end if you prss no or n 0r No or N then terminte loop
from ast import While
from telnetlib import STATUS


STATUS = True
while STATUS:
    subject =input("Enter subject name:")
    choice=input("do you want to enter more subjects? press 'y' for yes and 'n' for no:" )
    if choice=='n' or choice=='N' or choice=='no'or choice=='No':
        STATUS=False

#give marks and check pass or fail if fail then terminate the loop
from telnetlib import STATUS


STATUS= True
while STATUS:
    marks=int(input("enter Marks:"))
    if marks<35:
        print("fail")
        STATUS=False
    else:
        print("pass")

#Nested for loop ex1
for row in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print()

"
#ex2 print $ in place rwo3 and col3 
for row in range(1,6):
    for col in range(1,6):
        if row==3 and col==3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

#nested for loo ex2

for row in range(1,6):
    for col in range(1,row+1):   # for loop range 1 to row+1
        print("*",end=" ")
    print()

#nested for loop ex3
for row in range(1,6):
    for col in range(1,row+1):
        print(row,end=" ")   #print row
    print()


#nested for loop ex4
for row in range(1,6):
    for col in range(1,row+1):    
        print(col,end=" ")         #prit col
    print()


#nested for loop ex5
for row in range(1,6):
    for col in range(1,row+1): 
        if row%2==0:   
            print("0",end=" ")     #print 0 if row no is even
        else:
            print("1",end=" ")      #other wise 1
    print()

#nested for loop ex6
for row in range(1,6):
    for col in range(1,row+1): 
        if col%2==0:   
            print("0",end=" ")    #print 0 if col no is even

        else:
            print("1",end=" ")     #otherwise 1   
    print()

#Jumping statement 
#break statement
for i in range(1,6):
    mark=int(input("enter ur marks:"))
    if mark>35:
        print("Pass")
    else:
        break


#continue statement
for i in range(1,6):
    if i==3:
        continue
    else:
        print(i)
"""
#Pass stattement
for i in range(1,6):
    if i==3:
        pass
    else:
        print(i)

        