from datetime import datetime
import time
from secrets import choice
from telnetlib import STATUS
import os

vaccineDate=datetime.now()
vaccineDate=(str)(vaccineDate.date())
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
path=r"C:\Users\SONY\Documents\GitHub\Python_data\Task\VACCINATION\REPORT"
file=open(os.path.join(path,vaccineDate),'a')
STATUS=True
while STATUS:
    
    f_name=input("Enter your f_name:")
    l_name=input("Enter your l_name:")
    age=int(input("Enter your age:")) 
    birthday = input("Enter your date of birth in format dd\mm\yyyy: ")
    gender=input("Enter your gender:")
    vaccine=input("Enter your vaccine name:")
    vaccineDoz=int(input("Enter your vaccineDoz:"))
    

    
    file.write("-----------------INFO-------------------")
    file.write(f'\ncurrent time is:{current_time}')
    file.write(f'\ntoday date is:{vaccineDate}')
    file.write(f'\nFIRST NAME:{f_name}')
    file.write(f'\nLAST NAME:{l_name}')
    file.write(f'\nAGE:{age}')
    file.write(f'\nBIRTHDATE:{birthday}')
    file.write(f'\nGENDER:{gender}')
    file.write(f'\nVACCINE:{vaccine}')
    file.write(f'\nVACCINEDOZ:{vaccineDoz}\n')
    
    file.write("-----------------------------------------")
    
    choice=input("do you want enter more name y for yes and n for no:")
    if choice=='n':
         STATUS=False