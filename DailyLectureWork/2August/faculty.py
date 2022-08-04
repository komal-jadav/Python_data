class FacultyClass:

    def __init__(self):
        print("Welcome to product panel")
        self.name="anjali"
        self.laptop="a@gmail.com"
        self.address=""
        self.contactno=""
        self.subject=""
    
    

    dict={}

    def setcreateFaculty(self,name,email,city,number,subject):
        innerDict={}
        self.name=name
        self.email=email
        self.Address=city
        self.number=number
        self.subject=subject
        
        innerDict['email'] =self.email
        innerDict['Address'] = self.Address
        innerDict['Number'] =self.number
        innerDict['Subject']=self.subject

        self.dict[name] =innerDict



        print(self.dict)
