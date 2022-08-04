class pizza:

    Customer={}

    
    def __init__(self,price1=10.99,price2=9.5,quantity_pizza=0,quantity_pasta=0,total="",name="",colddrink=1,bruschetta=2,chocobrwni=2,Customer={}):
       
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
                    1. PRESS FOR PIZZA
                    2. PRESS FOR PASTA
                    0. PRESS FOR EXIST  """)
            choice=int(input(" Order of food : "))
            if choice==1:
                self.quantity_pizza = int(input("enter a quantity "))
                if self.quantity_pizza==1:
                    self.price1=10.99
                    print("Your Pizza Order Ammout is :",self.price1)
                    specification['Pizza_Qty']=self.quantity_pizza
                    specification['pizza_Price']=self.price1
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    continue
                elif self.quantity_pizza==2:
                    self.price1=20.99
                    print("Your Pizza Order Ammout is :",self.price1)
                    specification['Pizza_Qty']=self.quantity_pizza
                    specification['pizza_Price']=self.price1
                    self.Customer[self.name]=specification
                    print(self.Customer)
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
                    
                    self.price1=self.price1*self.quantity_pizza
                  
                    print("Your Pizza Order Ammout is :",self.price1)

                    total_quantity=self.quantity_pizza
                    print(f" Quantity of pizza is {self.quantity_pizza} ***Congratulations !! 1.5ltr SOFT DRINK free***")
                    specification['Pizza_Qty']=self.quantity_pizza
                    specification['pizza_Price']=self.price1
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    sum=0
                    for i,v in self.Customer.items():
                        if v and 'pizza_Price' in v.keys(): 
                            sum+=v['pizza_Price']
                    print(sum)


                else:
                    print(" Invalid Quantity ")
                
            elif choice==2:
                specification2={}
                self.quantity_pasta = int(input("enter a quantity "))
                if self.quantity_pasta==1:
                    self.price2=9.5
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification2['Pasta_qty']=self.quantity_pasta
                    specification2['Pasta_price']=self.price2
                    #specification['self.Customer']=specification2
                    self.Customer[self.name]=specification2
                    print(self.Customer)
                    continue
                elif self.quantity_pasta==2:
                    self.price2=17.00
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification['Pasta_qty']=self.quantity_pasta
                    specification['Pasta_price']=self.price2
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    continue
                elif self.quantity_pasta==3:
                    self.price2=27.50
                    print("Your Pasta Order Ammout is :",self.price2)
                    specification['Pasta_qty']=self.quantity_pasta
                    specification['Pasta_price']=self.price2
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    continue
                elif self.quantity_pasta==0:
                    self.price2=0
                    specification['Pasta_qty']=self.quantity_pasta
                    specification['Pasta_price']=self.price2
                    self.Customer[self.name]=specification
                    print(self.Customer)
                    continue
                elif self.quantity_pasta>=4:
                    self.price2=self.quantity_pasta*9.5
                    
                    print("Your Pasta Order Ammout is :",self.price2)
                    total_quantity=self.quantity_pasta
                    print(f" Quantity of pasta is {self.quantity_pasta} ***Congratulations !! get{self.bruschetta} BRUSCHETTA free***")
                    specification['Pasta_qty']=self.quantity_pasta
                    specification['Pasta_price']=self.price2
                    self.Customer[self.name]=specification
                    print(self.Customer)
               
                else:
                    print(" Invalid Quantity ")
            
            elif choice==0:
                if self.quantity_pasta>=4 and self.quantity_pizza>=4:
                    print(f" Quantity of pasta is {self.quantity_pasta}  and Quantity of pizza is {self.quantity_pizza} ***Congratulations !! get{self.chocobrwni} CHOCOBROWNI free***")
                
                elif self.quantity_pasta>self.quantity_pizza or self.quantity_pasta<self.quantity_pizza:
                    print(f"Quantity of pasta is {self.quantity_pasta} and Quantity of pizza is{self.quantity_pizza}")
                    total_quantity=self.quantity_pasta+self.quantity_pizza
                    sum=0
                    sum1=0
                    for i,v in self.Customer.items():
                        if v and 'pizza_Price' in v.keys(): 
                            sum+=v['pizza_Price']
                    for i,v in self.Customer.items():
                        if v and 'Pasta_price' in v.keys(): 
                            sum1+=v['Pasta_price']
                    
                    print("Total amount is : ",self.price1+self.price2)
                    
                c1=input("Do you want to add more customer y for yes and n for no :")
                if c1=='n':
                    print("----------------Pizza and Pasta Bill----------------")
                    sum=0
                    sum1=0
                    for i,v in self.Customer.items():
                        if v and 'pizza_Price' in v.keys():
                            sum+=v['pizza_Price']
                        print("Payment Received from pizza",sum)
                    for i,v in self.Customer.items():
                        if v and 'Pasta_price' in v.keys():
                            sum1+=v['Pasta_price']
                        print("Payment Received from pizza",sum1)
                    
                    
                    status=False
                    
                else:
                    obj.inputdetails()
                    obj.food()

                
            else:
                print(" Invalid Chioce ")
                   
obj=pizza()
obj.inputdetails()
obj.food()


    
        

