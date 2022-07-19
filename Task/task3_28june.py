# Accept 5 no from user and store positive in positive list and negative in list
positive_list =[]
negative_list =[]

for i in range(1,6):
    num= int(input("Enter no:"))
    if num>0:
        positive_list.append(num)
    else:
        negative_list.append(num)
print(positive_list)
print(negative_list)