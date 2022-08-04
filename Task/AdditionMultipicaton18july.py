from telnetlib import STATUS


def menu():
    
    data=""" 
                       Menu
                    Press 1 for Addtion
                    Press 2 for Multiplication

         """
    print(data)
    choice=int(input("enter your choice:"))
    if choice==1:
        addition()
    elif choice==2:
        mul()
def addition():
        num1=int(input("Enter number1:"))
        num2 = int(input("Enter number2:"))
        ans=num1+num2
        print(ans)
def mul():  
        num1=int(input("Enter number1:"))
        num2 = int(input("Enter number2:"))
        ans1=num1*num2
        print(ans1)
STATUS=True
while STATUS:
    menu()
    user_choice= input("do you want to perform more operation press'y' for 'yes' press 'n' for 'no' ")
    if user_choice=='n'or user_choice=='no'or user_choice=='N' or user_choice=='No':
        STATUS=False
