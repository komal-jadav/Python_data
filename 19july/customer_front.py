from view import *
name1=input("Enter your name:")
menu="""
                    Menu
                1) laptop
                2) mobile
    """
print(menu)
choice=int(input("enter yourchoice:"))
if choice==1:
    viewlaptop()
    laptopname=input("enter laptop name which you want to purchase:")
    qty=int(input("enter no.of qty which you want to buy:"))
    total_price=purchaselaptop(laptopname,qty)
    choice=input("do you want to purchase it press'y' for yes :")
    if choice=='y' or choice=='yes':
        addTocart(name1,"laptop",laptopname,qty,total_price)
elif choice==2:
    viewmobile()
else:
    print("Invalid input")