
from cgi import print_arguments
from operator import index, truediv
from pickle import TRUE
from secrets import choice
from telnetlib import STATUS

from psutil import users




Menu="""
              Menu
            Vadapav:-30
            Dabeli:-30
            Bhel  :-70

     """
        

#menu =[['vadapav',30],['dabeli',30],['bhel',70]]
Item_store=[]
print("JAY BHAVANI")
print("*****************")
print(Menu)
Data="""
         1)PRESS 1 ADD TO CART
         2)PRESS 2 REMOVE FROM CART
         3)PRESS 3 DISPLAY ALL ITEMS
         4)PRESS 4 BILL AMMOUNT
     """
print(Data)     
item=[]
qty=[]
price=[]
total=[]
order_list=[]


STATUS=True
while STATUS:
   
    choice=int(input("enter your choice:"))
    if choice==1:
        item_name=input("enter item name:")
        item_price=int(input("enter price:"))
        item_qty =int(input("enter qty:"))

        item.append(item_name)
        price.append(item_price)
        qty.append(item_qty)

    
    elif choice==2:
        item_name=input("enter item name:")
        if item_name in item:
            for item_name in item:
                index12=item.index(item_name)
                price.pop(index12)
                item.pop(index12)
                qty.pop(index12)   
        
        else:
            print("sorry item is not available ")
    elif choice==3:
        print("total no of item:",len(item))
        print("*******************")
        for i in item:
            print(i)
        print("*********************")
    elif choice==4:
        for i in item:
            print(i)
        print("total number of item in list:",len(item))
        for i in range(0, len(price)):
            total.append(price[i] * qty[i])
        print("total price:",total)
        print("total quntity:", qty)
        print("total amount:",sum(total))

       
            
            
        
    else:
        print("invalid input:")
    user_choice= input("do you want to perform more operation press'y' for 'yes' press 'n' for 'no' ")
    if user_choice=='n'or user_choice=='no'or user_choice=='N' or user_choice=='No':
        STATUS=False
    else:
        STATUS=True

    

    















