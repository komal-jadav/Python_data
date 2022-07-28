from datetime import datetime
import time
from secrets import choice
from telnetlib import STATUS
import os

vaccineDate=datetime.now()
vaccineDate=(str)(vaccineDate.date())
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
path=r"C:\Users\SONY\Documents\GitHub\Python_data\with_Exception\VACCINATION\REPORT"
file=open(os.path.join(path,vaccineDate),'a')
STATUS=True
while STATUS:
    file.write("-----------------INFO-------------------")
    file.write(f'\ncurrent time is:{current_time}')
    file.write(f'\ntoday date is:{vaccineDate}')
    
    try:
        f_name=input("Enter a First Name: ")
        if f_name.isalpha():
            file.write(f'\nFIRST NAME:{f_name}')
        else:
            raise TypeError
    except TypeError:
        print("invalid name use only charactor value in name")
        f_name=input("Enter a First Name: ")
        file.write(f'\nFIRST NAME:{f_name}')

    try:
        l_name=input("Enter your l_name:")
        if l_name.isalpha():
            file.write(f'\nFIRST NAME:{l_name}')
        else:
            raise TypeError
    except TypeError:
        print("invalid name use only charactor value in name")
        l_name=input("Enter your l_name:")
        file.write(f'\nLAST NAME:{l_name}')
    try:
        contact=int(input("Enter your contact number:"))
        if contact.isdigit() and len(contact)==10:
            file.write(f'\nFIRST NAME:{contact}')
        else:
            raise TypeError
    except TypeError:
        print("invalid name use only charactor value in name")
        contact=int(input("Enter your contact number:"))
        file.write(f'\nCotact Number:{contact}')

   
   
    age=int(input("Enter your age:")) 
    try:

        birthday = input("Enter your date of birth in format dd\mm\yyyy: ")
        day,month,year=birthday.split('/')
        if len(birthday)==10 and month<=12:
            datetime(int(day),int(month),int(year))
            file.write(f'\nBIRTHDATE:{birthday}')
        else:
            raise TypeError
    except TypeError:
        print("Invalid Input enter date in dd/mm/yyyy format:")
        birthday=input("Enter your date of birth in format dd\mm\yyyy: ")
        file.write(f'\nBIRTHDATE:{birthday}')



    gender=input("Enter your gender:")
    vaccine=input("Enter your vaccine name:")
    vaccineDoz=int(input("Enter your vaccineDoz:"))
    

    
    
    
    
    
    file.write(f'\nAGE:{age}')
    
    file.write(f'\nGENDER:{gender}')
    file.write(f'\nVACCINE:{vaccine}')
    file.write(f'\nVACCINEDOZ:{vaccineDoz}\n')
    
    file.write("-----------------------------------------")
    
    choice=input("do you want enter more name y for yes and n for no:")
    if choice=='n':
         STATUS=False