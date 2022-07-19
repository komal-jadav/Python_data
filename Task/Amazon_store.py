from telnetlib import STATUS


data="""
                        Menu
                    Press 1 for add items
                    Press 2 for check items
                    Press 3 for remove items
                    Press 4 for view items


    """

amazon_store=[]
print("Welcome to amazon store")

STATUS=True
while STATUS:
    print(data)
    choice=int(input("enter your choice:"))
    if choice==1:
        item_name=input("Enter item name:")
        amazon_store.append(item_name)
    elif choice==2:
        item_name=input("Enter item name :")
        if item_name in amazon_store:
            print("item is availabe")
        else:
            print("not available")
    elif choice==3:
        item_name=input("Enter item name")
        if item_name in amazon_store:
            amazon_store.remove(item_name)
        else:
            print("Sorry item is not available")
    elif choice==4:
        print("Total no of item:",len(amazon_store))
        print("------------------------------------------------")
        for item in amazon_store:
            print(item)
            print("------------------------------------------------")
    else:
        print("Invalid Input")
    
    
    user_choice= input("do you want to perform more operation press'y' for 'yes' press 'n' for 'no' ")
    if user_choice=='n'or user_choice=='no'or user_choice=='N' or user_choice=='No':
        STATUS=False
    else:
        STATUS=True

    
