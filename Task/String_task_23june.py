# String task
firstName = "Komal"
email = "Solankikomal225@gmail.com"
password = "12345678"

User_Email = input("Enter email:")
User_Password = input("Enter password:")

if User_Email==email and User_Password==password:
    print(firstName)
elif User_Email!=email and User_Password==password:
    print("Invalid Email")
elif User_Email==email and len(User_Password)!=8:
    print("password must be 8 character")
elif User_Email==email and User_Password!=password:
    print("Invalid password")

else:
    print("Invalid user")