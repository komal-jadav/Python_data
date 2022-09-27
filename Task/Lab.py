input_str1=input("Please Enter your first name:")
count=0
if input_str1.isalnum()== False:
    for i in input_str1:  
        count=count+1
        print(f"{i} {count}")
        #print(f"There are {} letters in {input_str1} ") 
    if input_str1.isalpha()==True: 
        if len(input_str1)>1 or input_str1.isalpha() or input_str1.isalnum()==False  :
            print(f"There are {len(input_str1)- input_str1.count('-')} letters in {input_str1}")
        elif len(input_str1)==1:
            print(f"There is {len(input_str1)} letter in {input_str1}")
        elif len(input_str1)==0 or input_str1.isalpha():
            print("you did not enter any character")
    else:   
        print("Non alphabatical characters were entered")

   