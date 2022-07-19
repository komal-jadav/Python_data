unique_list=[]
print(unique_list)
count=12
for i in range  (count):
    list=int(input("enter ur no:"))
    for x in  list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
         print(x)