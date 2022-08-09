class pizza:

    Customer={}
    Customer_pasta={}
    Total={}
    
    def __init__(self,price1=10.99,price2=9.5,quantity_pizza=0,quantity_pasta=0,total="",name="",colddrink=1,bruschetta=2,chocobrwni=2,Customer={},Customer_pasta={},Total={}):
       
        self.price1 = price1
        self.price2 = price2
        
        self.quantity_pizza=quantity_pizza
        self.quantity_pasta=quantity_pasta
        self.total=total
        self.name=name
        self.colddrink=colddrink
        self.bruschetta=bruschetta
        self.chocobrwni=chocobrwni
        self.Customer=Customer
        self.Customer_pasta=Customer_pasta
        self.Total=Total


    def inputdetails(self):
        
        self.name = input("enter a customer name : ")
        print(f"Hello {self.name}, Welcome to Pizzariya")
    def food(self):
        
        print("""                ----------Menu--------------
              
                1 large pizza = 10.99 AUD 

                2 large Pizzas = 20.99 AUD 

                3 Large Pizzas = 29.99 AUD

                ***Buy 4 or more pizza and get 1.5lt of soft drink free***


                1 large pasta = 9.5 AUD 

                2 large pastas = 17.00 AUD 
                
                3 large pastas = 27.50 AUD

                ***Buy 4 or more pastas and get 2 bruschetta free.***
                ***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.""")
        
        status = True
        while status:
            specification={}
            print("""
                    1.  Pizza
                    2. Pasta
                    0. exit""")
            choice=int(input(" Order of food : "))
            if choice==1:
                self.quantity_pizza = int(input("enter a quantity "))
                if self.quantity_pizza==1:
                    self.price1=10.99
                    print("Your Pizza Order Ammout is :",self.price1)
                    continue
                elif self.quantity_pizza==2:
                    self.price1=20.99
                    specification['Pizza_Qty']=self.quantity_pizza
                    specification['pizza_Price']=self.price1
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    print("Your Pizza Order Ammout is :",self.price1)
                    continue
                elif self.quantity_pizza==3:
                    self.price1=29.99
                    print("Your Pizza Order Ammout is :",self.price1)
                    specification['Pizza_Qty']=self.quantity_pizza
                    specification['pizza_Price']=self.price1
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    continue
                elif self.quantity_pizza>=4:
                    
                    self.price1=10.99*self.quantity_pizza
                  
                    print("Your Pizza Order Ammout is :",self.price1)

                    total_quantity=self.quantity_pizza
                    print(f" Quantity of pizza is {self.quantity_pizza} ***Congratulations !! 1.5ltr SOFT DRINK free***")
                    specification['Pizza_Qty']=self.quantity_pizza
                    specification['pizza_Price']=self.price1
                    self.Customer[self.name]=specification
                    print(self.Customer)

                else:
                    print(" Invalid Quantity ")
               
            elif choice==2:
                specification1={}
                self.quantity_pasta = int(input("enter a quantity "))
                if self.quantity_pasta==1:
                    self.price2=9.5
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification['Pasta_qty']=self.quantity_pasta
                    specification['Pasta_price']=self.price2
                    self.Customer_pasta[self.name]=specification
                    
                    print(self.Customer_pasta)
                    
                    continue
                elif self.quantity_pasta==2:
                    self.price2=17.00
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification1['Pasta_qty']=self.quantity_pasta
                    specification1['Pasta_price']=self.price2
                    self.Customer_pasta[self.name]=specification1
                    
                    print(self.Customer_pasta)
                    continue
                elif self.quantity_pasta==3:
                    self.price2=27.50
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification1['Pasta_qty']=self.quantity_pasta
                    specification1['Pasta_price']=self.price2
                    self.Customer_pasta[self.name]=specification1
                    
                    print(self.Customer_pasta)
                    continue
                elif self.quantity_pasta>=4:
                    self.price2=self.quantity_pasta*9.5
                    
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification1['Pasta_qty']=self.quantity_pasta
                    specification1['Pasta_price']=self.price2
                    self.Customer_pasta[self.name]=specification1
                    
                    print(self.Customer_pasta)
                    total_quantity=self.quantity_pasta
                    print(f" Quantity of pasta is {self.quantity_pasta} ***Congratulations !! get{self.bruschetta} BRUSCHETTA free***")
               
                else:
                    print(" Invalid Quantity ")
            
            elif choice==0:
                if self.quantity_pasta>=4 and self.quantity_pizza>=4:
                    print(f" Quantity of pasta is {self.quantity_pasta}  and Quantity of pizza is {self.quantity_pizza} ***Congratulations !! get{self.chocobrwni} CHOCOBROWNI free***")
                    total_quantity = self.quantity_pasta+self.quantity_pizza+self.chocobrwni+self.bruschetta+self.colddrink
                    print(f" Quantity of pasta is {self.quantity_pasta},\nQuantity of pizza is {self.quantity_pizza} and \nQuantity of chocobrwni is {self.chocobrwni} and \nQuntity of bruschetta is {self.bruschetta} and \n Quntity of Softdrink is {self.colddrink}Total quantity is : ", total_quantity)
                    self.price1=10.99*self.quantity_pizza
                    self.price2=self.quantity_pasta*9.5
                    print("Total amount of price is ",self.price1+self.price2)
                    """
                    sum=0
                    sum1=0
                    for i,v in self.Customer.items() :
                        if v and 'pizza_Price' in v.keys():
                            sum+=v['pizza_Price']
                        print("Payment Received from pizza",sum)
                    for i,v in self.Customer_pasta.items():
                        if v and 'Pasta_price' in v.keys():
                            sum1+=v['Pasta_price']
                        print("Payment Received from pasta",sum1)

                        print("TOtal AMMOUNT IS=",+(sum+sum1))
                    """    
                      
                elif self.quantity_pasta>self.quantity_pizza or self.quantity_pasta<self.quantity_pizza :
                    print(f"Quantity of pasta is {self.quantity_pasta} and Quantity of pizza is{self.quantity_pizza}")
                    total_quantity=self.quantity_pasta+self.quantity_pizza
                    total_price = self.price1+self.price2
                    print("Total amount is : ",total_price)
                    
                c1=input("Do you want to add more customer y for yes and n for no :")
                if c1=='n':
                    
                    print("----------------Pizza and Pasta Bill----------------")

                    sum_pizaprice=0
                    sum_pizzaqty=0
                
                    sum_pastaprice=0
                    sum_pastaqty=0
                    
                    for i,v in self.Customer.items():
                        if v and 'pizza_Price' in v.keys():
                            sum_pizaprice+=v['pizza_Price']
                    print("Payment Received from pizza",sum_pizaprice)
                    for i,v in self.Customer_pasta.items():
                        if v and 'Pasta_price' in v.keys():
                            sum_pastaprice+=v['Pasta_price']
                    print("Payment Received from pasta",sum_pastaprice)

                    print("Payment Received from Today:",sum_pizaprice+sum_pastaprice)

                    for i, v in self.Customer.items():
                        if v and 'Pizza_Qty' in v.keys():
                            sum_pizzaqty += v['Pizza_Qty']
                    
                    
                    for i, v in self.Customer.items():
                        if v and 'Pasta_qty' in v.keys():
                            sum_pastaqty += v['Pasta_qty']
                        
                    print("Number of Pizza and pasta sold in one shift:",sum_pizzaqty+sum_pastaqty)
                    
                    
                    print("BYE BYE")


                    
                    status=False
                    break
                    
                elif c1=='y':
                    obj.inputdetails()
                    obj.food()

                
            else:
                print(" Invalid Chioce ")
                   
obj=pizza()
obj.inputdetails()
obj.food()


    
        

