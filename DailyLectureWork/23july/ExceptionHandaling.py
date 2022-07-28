#Exception handling using try and except
"""
try:
    print(a)
except:
    print("Invalid input")



#Ex2 

from tkinter.tix import InputOnly


try:
    num1=int(input("Enter one number:"))
    num2=int(input("Enter two number:"))
    ans=num1/num2

    print(ans)
except  ZeroDivisionError:
    print("make sure enterred number is greater than 0")
except:
    print("invalid input")

"""

#ex3

try:
    num1=int(input("Enter one number:"))
    num2=int(input("Enter two number:"))
    ans=num1/num2

  
except  ZeroDivisionError:
    print("make sure enterred number is greater than 0")
except:
    print("invalid input")
else:
    print(ans)
finally:
    print("Thank you for using this app.")