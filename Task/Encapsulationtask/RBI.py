class ROIClass:
    """
       __init__ work as a constructor 
       it automatically call when object of class create    
    
    """
    def __init__(self):
        print("Welcome to ROI Panel")
        self.__ROI=6.5
        
    def display(self):
        print(self.__ROI)
        

    def updateprice(self,newROI):
        self.__ROI=newROI
        