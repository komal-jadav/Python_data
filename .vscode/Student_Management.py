# STUDENT MANAGEMENT SYSTEM

from ast import If
from itertools import count
from secrets import choice
from telnetlib import STATUS
from tkinter import N, TRUE, W


menu=""""
             PRESS 1 FOR COUNSELLOR
             PRESS 2 FOR FACULTY
             PRESS 3 FOR STUDENT
     
     """
Counsellor={}
STATUS = True
while STATUS:
    print(menu)
    role=int(input("Enter your choice:"))
    if role==1:
        Specification_Consellor={}
        
       
        print("Counsellor")
        Data="""
                  1 for Add student
                  2 for view All student 
                  3 for view specific Student
                  4 for remove student
        
             """
        print(Data)
        Choice1=int(input("Enter choice for counsellor :"))
        if Choice1==1:
          Status=TRUE
          while Status:
               Sr_no=int(input("Enter Sr_no :"))
               First_name=input("Enter first name :")
               Last_name = input("Enter last name :")
               Contact_no=int(input("Enter contact no:"))

               user_choice =input("do you want continue press'y' for yes 'n' for no:-")
               if user_choice == 'n':
                    Status=False
                         
               Course_subject={}
               
               Subject_name=input("Enter subject name :")     
               Subject_fees=int(input("Enter Subject fess:"))          
               Faculty_name=input("Enter faculty name:")
               Specification_Consellor['First_name']=First_name
               Specification_Consellor['Last_name']=Last_name
               Specification_Consellor['Contact_no']= Contact_no     
               Course_subject['Subject_name']=Subject_name
               Course_subject['fees']=Subject_fees
               Course_subject['Faculty_name']=Faculty_name                   
              # Specification_Consellor['Subject_name']=Course_subject

               
       
               Counsellor[Sr_no]=Specification_Consellor
               user_choice =input("do you want continue press'y' for yes 'n' for no:-")
               if user_choice == 'n':
                    Status=False
                         
               else:
                    for i in Course_subject:
                         Specification_Consellor['Subject_name']=Course_subject

               
                         
                    Status=True
          print(Counsellor)
        elif Choice1==2:
          for i in Counsellor.keys():
               
                    print("------------------------------------------")
                    print(f"Sr_no: {i}")
                    print(f"First_name :",Counsellor[i]['First_name'])
                    print(f"Last_name:",Counsellor[i]['Last_name'])
                    print(f"Contact_no :",Counsellor[i]['Contact_no'])
                    
                    print(f"Subject_Detais:",Counsellor[i]['Subject_name'])
        elif Choice1==3:
                    StudentID=int(input("Enter Student ID:"))
                    if StudentID==Sr_no:
                         for Sr_no in Counsellor:
                              print("------------------------------------------")
                              print(f"Sr_no: {Sr_no}")
                              print(f"First_name :",Counsellor[Specification_Consellor]['First_name'])
                              print(f"Last_name:",Counsellor[Specification_Consellor]['Last_name'])
                              print(f"Contact_no :",Counsellor[Specification_Consellor]['Contact_no'])
                              
                              print(f"Subject_Detais:",Counsellor[Specification_Consellor]['Subject_name'])

                         

     
               
     
