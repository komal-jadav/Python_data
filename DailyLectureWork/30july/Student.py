class StudentClass:
    name=""
    email=""
    address=""
    contactno=""
    subject=""
    fees=""
    mark=""

    dict={}

    def createStudent(self,name,email,address,no,subject,fees,mark):
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