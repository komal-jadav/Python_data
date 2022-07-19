#product manager

fruits={} # blank dictionary
menu="""
             Press 1 for add fruits
             Press 2 for view fruits
             Press 3 for Purchase fruits
             press 4 for exit
     """
Status=True
while Status:
    print(menu)
    Specification={}
    choice =int(input("Enter your choice :"))
    if choice ==1:
        friut_name = input("Enter friut name :")
        qty = int(input("enter qty"))
        price = int(input("enter price"))

        Specification['qty'] =qty
        Specification['price'] =price

        fruits[friut_name]=Specification
        print(fruits)
    elif choice == 2:
        for k in fruits.keys():
            print("------------------------------------------")
            print(f"Fruit name: {k}")
            print(f"Fruit qty :",fruits[k]['qty'])
            print(f"Fruit Price:{k}",fruits[k]['price'])

    elif choice ==3:
        for k in fruits.keys():
            print("-----------------------------------")
            print(f"Fruit name: {k}")
            print(f"Fruit Price:(for one pice)",fruits[k]['price'])
        friut_name = input("Enter fruits which you want to purchase :")
        if friut_name in fruits.keys():
            qty = int(input("Enter no. Qty you want:"))
            price = qty * fruits[friut_name]['price']
            print("PRICE=",price)
    else:
        print("INVALID INPUT")
        user_choice =input("do you want continue press'y' for yes 'n' for no")
        if user_choice == 'n':
            Status=False
            
        else:
            Status=True
            

        
