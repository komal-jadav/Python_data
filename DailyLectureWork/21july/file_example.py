"""
 r:read mode
 w: write mode 
 a:append mode 
"""


#f=open("C:\\Users\\SONY\\Documents\\GitHub\\Python_data\\DailyLectureWork\\21july\\example.txt","r")

#print(f.read())

#f=open(r"C:\Users\SONY\Documents\GitHub\Python_data\DailyLectureWork\21july\example.txt","r")

#print(f.read())
#print(f.readline())


f=open(r"C:\Users\SONY\Documents\GitHub\Python_data\DailyLectureWork\21july\example.txt","r")

l1=f.readlines()
print("----------->",l1)
print("no.of lines in file:",len(l1))

print("3rd line of file :",l1[2])
print("last line of file :",l1[-1])

