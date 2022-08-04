import faculty,student

    
f=faculty.FacultyClass()
s=student.StudentClass()



choice=int(input("Choice 1 for Faculty and 2 for Student:"))
if choice==1:

    STATUS=True
    while STATUS:
        """ 
        faname=input("Enter faculty name:")
        subject=input("Enter Subject name :")
        Address=input("Enter Faculty Address:")
        email=input("Enter faculty email:")
        Number=input("Enter mobile no:")

        """

        f.setcreateFaculty("komal","k@gmail.com","ahmedabad",1254473438,"java")
        print(f.name)
        print(f.email)
        print(f.Address)
        print(f.number)
        print(f.subject)
        
        
       
        
        choice=input("Do you want to make details press 'y' for yes and press 'n' for no:")

        if choice =='n':
            STATUS=False


    print("---------------------------------------------")
elif choice==2:
    STATUS=True
    while STATUS:
        """
        fname=input("Enter student name:")
        subject=input("Enter Subject name :")
        Address=input("Enter stusent Address:")
        email=input("Enter student email:")
        Number=input("Enter mobile no:")
        Fees=int(input("Enter fees:"))
        Marks=int(input("Enter ur marks:"))
        """

        s.setcreateStudent("Dhvl","D@gmail.com","Surat",9938948325,"python",12000,345)

        print(s.name)
        print(s.email)
        print(s.Address)
        print(s.number)
        print(s.subject)
        print(s.fees)
        print(s.mark)
        
        choice=input("Do you want to make details press 'y' for yes and press 'n' for no:")

        if choice =='n':
            STATUS=False