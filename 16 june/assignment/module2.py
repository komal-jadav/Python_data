
#positive negative Zero
"""
num=int(input("Enter no:"))
if num>0:
    print("no. is positive :")
elif num<0:
    print("no.is negative:")
else:
    print("no is zero:")

#Factorial no.
num=int(input("Enter a no.:-"))
if num>0:
    f=1
    for i in range(1,num+1):
        f*=i
        print("Factorial:",f)
else:
    print("Invalid input")


#Fibonacci series

from itertools import count


n=int(input("enter one no:"))
a=0
b=1
print(a)
print(b)
if n<0:
    print("invalid input")
elif n==0:
    print(0)
elif n==1 and n==2:
    print(b)
else:
    for n in range(1,n):
        c=a+b
        a=b
        b=c
        print(c)


#swap no. without temp variable
x=int(input("enter one no:"))
y=int(input("enter second no:"))
print("Before swaping")
print("value of x:",x,"value of y:",y)
x,y=y,x
print("After swaping")
print("value of x:",x,"value of y:",y)


#swap no. using temp variable
x=int(input("enter one no:"))
y=int(input("enter second no:"))
print("Before swaping")
print("value of x:",x,"value of y:",y)
a=x
x=y
y=a
print("After swaping")
print("value of x:",x,"value of y:",y)


#no is even or odd
num=int(input("enter no. :-"))
if num%2==0:
    print("no is even")
else:
    print("no is odd")


 #passed letter is vowel or not
     
letter=input("enter one letter :")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("it is vowel")
else:
    print("it is not vowel")
 
#sum of three integer but if two no. same than give zero
num1=int(input("enter no1:"))
num2 = int(input("enter no2: "))
num3=int(input("enter no 3:"))

ans= num1+num2+num3
if num1==num2 or num1==num3 or num2==num3:
    print(0)
else:
    print(ans)

# return true if two no equal or sum 5 or difference 5

n1=int(input("enter no1:-"))
n2=int(input("enter no2:-"))
ans1 = n1+n2
ans2 =n1-n2
if n1==n2 or ans1==5 or ans2==5:
    print("true")
else:
    print("false ")



 #sum of first n positive integer

n=int(input("enter no:"))
sum=(n*(n-1))/2
print (sum)


 #Write a Python program to calculate the length of a string.

name= input("Enter ur name:")
print("name length is:",len(name))


 
# Write a Python program to count the number of characters (character frequency) in a string

name =input("Enter ur name :")
for i in name:
    frequency = name.count(i)
    print(str(i) +":"+str(frequency),end=" ")




# What are negative indexes and why are they used?
# Write a Python program to count occurrences of a substring in a string.
name =input("Enter ur name :")
i=name.split(",")
for word in i:
    frequency = name.count(word)
    print(str(word) +":"+str(frequency),end=" ")

# Write a Python program to count the occurrences of each word in a given sentence

name =input("Enter ur name :")
i=name.split()
for word in i:
    frequency = name.count(word)
    print(str(word) +":"+str(frequency),end=" ")

#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = input ("enter one string:")
str2 = input("enter second string:")


x=str1[0:2]

str1=str1.replace(str1[0:2],str2[0:2])

str2=str2.replace(str2[0:2],x)

print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)


 




# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
str1= input("enter one string:-")
length = len(str1)  
  
if length > 2:  
    if str1[-3:] == 'ing':  
      str1 += 'ly' 
      print("Adding ly:",str1) 
    else:  
      str1 += 'ing' 
      print("Adding only ing:",str1)
else:
    print("without adding anything:",str1) 



# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
str1=input("Enter one string:-")
#for find position of not and poor 
snot = str1.find('not')
spoor = str1.find('poor')
  

if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good') #4 is  for length of poor
    print("new string is:-",str1)

  
else:
    print("without change in string :-",str1)


# Write a Python function that takes a list of words and returns the length of the longest one.

# Write a Python function to reverses a string if its length is a multiple of 4.

str1=input("enter one string:-")
rstring = ''.join(reversed(str1))

if len(str1)%4==0:
    print("Reversed string is :",rstring)
else:
    print("As it is string:-",str1)


# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String: w3resource'
# Expected Result: 'w3ce'
# Sample String: 'w3'
# Expected Result: 'w3w3'
# Sample String: ' w'
# Expected Result: Empty String
str1=input("enter one string:-")
if len(str1)>2:
    print("Expected Result is:",str1[0:2]+str1[-2:])
elif len(str1)==2:
    print("Expected Result is: ",str1[0:2]+str1[0:2])
else:
    print("Expected Result is :","Empty String")


"""

# Write a Python function to insert a string in the middle of a string.
str1=input("enter one string:-")
word=input("enter one word to insert:-")
midpoint=len(str1)//2
final_string=str1[:midpoint]+ word +str1[midpoint:]
print("final string is:",final_string)
