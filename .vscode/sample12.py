from ast import While


menu=""""
             PRESS 1 FOR COUNSELLOR
             PRESS 2 FOR FACULTY
             PRESS 3 FOR STUDENT
     
     """
Counsellor={}
Status=True
while Status:
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
        Specification_Consellor={}
        Choice=int(input("Enter Counsellor Choice:"))
        if Choice==1:
            Status=True
            while Status:
                Sr_no=int(input("Enter Sr_no :"))
                First_name=input("Enter first name :")
                #Last_name = input("Enter last name :")
                #Contact_no=int(input("Enter contact no:"))
                Specification_Consellor['SR_NO'] =Sr_no
                Specification_Consellor['FIRST_NAME']=First_name
               
                Status=True
                while Status:
                    for i in Specification_Consellor:
                        Specification_Subject={}
                        Subject_name=input("Enter subject name :")     
                        Subject_fees=int(input("Enter Subject fess:"))          
                        Faculty_name=input("Enter faculty name:")
                        Specification_Subject['SUBJECT_NAME']=Subject_name
                        Specification_Subject['SUBJECT_FEES']=Subject_fees
                        Specification_Subject['SUBJECT_FACULTY']=Faculty_name
                        Specification_Consellor["COURSE"]=Specification_Subject
                    userchoice="do you want add more subject press'y' for yes and 'n for no:'"
                    if userchoice=='n':
                        Status=False
                Counsellor["SR_NO"]=Specification_Consellor
                print(Counsellor)


