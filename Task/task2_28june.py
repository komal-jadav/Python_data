# Accept 5 number from user and store even numbers in even list and odd numbers in odd list
even_list=[]
odd_list=[]

for i in range(1,6):
    no=int(input("Enter No:"))
    if no%2==0:
        even_list.append(no)
    else:
        odd_list.append(no)
print(even_list)
print(odd_list)
