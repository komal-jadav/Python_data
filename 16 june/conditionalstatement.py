"""#elif statement
num=int(input("Enter a number :"))
if num==10:
    print("num=10")
elif num==20:
    print("num=20")
elif num==30:
    print("num=30")
else:
    print("invalid number")
    
# check the no. is between 10-50 or 50-100

num=int(input("Enter a number:"))
if num>=10 and num<=50:
    print("number is between 10-50")
elif num>=51 and num<=100:
    print("number is between:")
else:
    print("number is below 10 or above 100")

"""
#Accept marks from student and give appropriate grade
"""
Above 70:A
60-70 :B
50-60:C
40-50:D
below 35:fail

"""
"""
marks=int(input("enter ur marks out of 100:"))

if marks>=70:
    print("A grade")
elif marks>=60 and marks<=69:
    print("B grade")
elif marks>=50  and marks<60:
    print("C grade")
elif marks>=40  and marks<=49:
    print("D grade")
else:
    print("Fail")

#nestedif statement 
email="k@gmail.com"
password="12345"
S_email = input("Enter ue email:")
S_password =input("Enter ur password:")
if S_email==email:
    if S_password==password:
            print("Welcome to tops technoogy")
    else:
            print("invalid password")
else:

           print("Invalid email")

#whta is print if student give marks above 100 and negative marks 


marks=int(input("enter ur marks:"))
if marks>=0 and marks<=100:
    if marks>=70:
            print("A grade")
    elif marks>=60 and marks<=69:
            print("B grade")
    elif marks>=50  and marks<60:
            print("C grade")
    elif marks>=40  and marks<=49:
            print("D grade")
    else:
            print("Fail")
else:
    print("Invalid input")

    #looping Statement
#for loop
for i in range(1,6):
    print(i)
    
#By default starting from 0
for i in range(5):
    print(i)

#Decending Order 
for i in range(5,0,-1):
    print(i)

#add 2 in all no.
for i in range(1,11,2):
    print(i)
    """
#to display hello with i 
for i in range(1,6):
    print(i,"hello")

    