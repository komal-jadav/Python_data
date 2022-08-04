class ProductClass:
    """
       __init__ work as a constructor 
       it automatically call when object of class create    
    
    """
    def __init__(self):
        print("Welcome to product panel")
        self.mobile=5000
        self.__laptop=45000
    def display(self):
        print(self.mobile)
        print(self.__laptop)

    def updateprice(self,newLaptopPrice):
        self.__laptop=newLaptopPrice
        