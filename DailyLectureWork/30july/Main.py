from telnetlib import STATUS
import Faculty, Student

f=Faculty.FacultyClass()
s=Student.StudentClass()



choice=int(input("Choice 1 for Faculty and 2 for Student:"))
if choice==1:

    STATUS=True
    while STATUS:
        faname=input("Enter faculty name:")
        subject=input("Enter Subject name :")
        Address=input("Enter Faculty Address:")
        email=input("Enter faculty email:")
        Number=input("Enter mobile no:")
        f.createFaculty(faname,email,Address,Number,subject)
        
        choice=input("Do you want to make details press 'y' for yes and press 'n' for no:")

        if choice =='n':
            STATUS=False


    print("---------------------------------------------")
elif choice==2:
    STATUS=True
    while STATUS:
        fname=input("Enter student name:")
        subject=input("Enter Subject name :")
        Address=input("Enter stusent Address:")
        email=input("Enter student email:")
        Number=input("Enter mobile no:")
        Fees=int(input("Enter fees:"))
        Marks=int(input("Enter ur marks:"))
        s.createStudent(fname,email,Address,Number,subject,Fees,Marks)
        
        choice=input("Do you want to make details press 'y' for yes and press 'n' for no:")

        if choice =='n':
            STATUS=False