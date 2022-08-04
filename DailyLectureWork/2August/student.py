class StudentClass:
    def __init__(self):

        self. name=""
        self.email=""
        self.address=""
        self.contactno=""
        self.subject=""
        self.fees=""
        self.mark=""

    dict={}

    def setcreateStudent(self,name,email,address,no,subject,fees,mark):
        innerDict={}
        self.name=name
        self.email=email
        self.Address=address
        self.number=no
        self.subject=subject
        self.fees=fees
        self.mark=mark

        
        innerDict['email'] =self.email
        innerDict['Address'] = self.Address
        innerDict['Number'] =self.number
        innerDict['Subject']=self.subject
        innerDict['Fees']=fees
        innerDict['mark']=mark

        self.dict[name] =innerDict

        print(self.dict)