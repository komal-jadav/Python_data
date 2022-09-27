from abc import ABC, abstractclassmethod
#ABC = Abstract Base Class

class RBI(ABC):
    @abstractclassmethod
    def roi(self):
        #method declaration only 
        pass

class SBI(RBI):
    def roi(self):
        print("6.5")

class HDFC(RBI):
    def roi(self):
        print("7.5")


sbi=SBI()
hdfc=HDFC()

sbi.roi()
hdfc.roi()