from secrets import choice
from telnetlib import STATUS

addtocart={}
mobile_store={}
menu="""
                MENU
            PRESS 1 FOR PROJECT MANAGER
            PRESS 2 FOR CUSTOMER
 
      """
STATUS=True

while STATUS:
    Specificationc={}
    Specification={}
    print(menu)
    role=int(input("enter ur role(1/2): "))
    
    if role==1:
        print("PROJECT MANAGER")
        product_name=input("enter product name: ")

        model_number=input("enter model number: ")
        color=input("enter color: ")
        qty=int(input("enter product qty: "))
        price=int(input("enter product price: "))


        Specification["model"]=model_number
        Specification["color"]=color
        Specification["qty"]=qty
        Specification["price"]=price
        
        mobile_store[product_name]=Specification
        print(mobile_store)


        
        
    elif role==2:

        print("CUSTOMER")

        for k in mobile_store.keys():
                print("------------------------------------------------------")

                print(f"PRODUCT: {k} ")

                print("MODEL: " +mobile_store[k]["model"])
                print("COLOR: " +mobile_store[k]["color"])
                #print("QTY: " +str(mobile_store[k]["qty"]))
                print("PRICE: " +str(mobile_store[k]["price"]))
        
        
        print("------------------------------------------------------")    
        product_namec=input("enter ur product name :")
        
        modelc=input("enter model no:")
        qtyc=int(input("enter quntity:"))
        Specificationc["model"] = modelc
        addtocart[product_namec]=Specificationc
        print("------------------------------------------------------")
        if qtyc<=qty:
            print("PRODUCT IS AVAILABLE")
            Specificationc["qty"]=qtyc
            for k in mobile_store.keys() and addtocart.keys():
                
                print("COLOR: " +mobile_store[k]["color"])
                pricec=+int(mobile_store[k]["price"])*+int(addtocart[k]["qty"])
                print("PRICE FOR ONE: "+str(mobile_store[k]["price"]))
                print("TOTAL PRICE:",pricec)
                Specificationc["price"]=pricec

        else:
            print("OUT OF STOCK")
          
        print(addtocart)
        mobile_store[product_name]['qty']-=qtyc
    else:
        print("INVALID INPUT")
    choice=input("do you want to continue:press 'y' for 'yes' and 'n' for 'no' ")
    if choice=='n' or choice=='no' or choice=='No'or choice=="N":
        STATUS=False
for k in mobile_store.keys():
    print("------------------------------------------------------")

    print(f"PRODUCT: {k} ")

    print("MODEL: " +mobile_store[k]["model"])
    print("COLOR: " +mobile_store[k]["color"])
    print("QTY: " +str(mobile_store[k]["qty"]))
    print("PRICE: " +str(mobile_store[k]["price"]))


       

    