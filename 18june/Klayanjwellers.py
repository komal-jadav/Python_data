#project on kalyan jwellers




Customer_name= input("Enter ur Name:")
Custmore_mobileno =int(input("Enter ur MobileNo.:"))
Customer_Gender= input("Enter ur Gender:")
Customer_Age = int(input ("Enter ur Age:"))
Product_Name =input("Enter ur Product_Name:")
Product_Quntity =float(input("Enter ur Quntity of ur product:"))
Current_Price =4829
Making_charge=589
Price_Quntity =(Current_Price*Product_Quntity)

#purchace Ammount
if Product_Quntity>=10:
     Making_charge2 =(589*Product_Quntity)/100
     Purchase_Ammount= Price_Quntity + Making_charge2 + Making_charge
    #print("Total Amount: ",float(Purchase_Ammount))
     if Customer_Age >=60:
        if Customer_Gender=="m" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
            total1 =(Purchase_Ammount*10)/100
            Purchase_Ammount1 = Purchase_Ammount-total1
            #print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="m" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
            total2 =(Purchase_Ammount*15)/100
            Purchase_Ammount1 = Purchase_Ammount-total2
            #  print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="m" and Purchase_Ammount>1000000:
            total3 =(Purchase_Ammount*20)/100
            Purchase_Ammount1 = Purchase_Ammount-total3
            # print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="f" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
            total4 =(Purchase_Ammount*15)/100
            Purchase_Ammount1 = Purchase_Ammount-total4
            # print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="f" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
            total5 =(Purchase_Ammount*20)/100
            Purchase_Ammount1 = Purchase_Ammount-total5
            # print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="f" and Purchase_Ammount>1000000:
            total6 =(Purchase_Ammount*25)/100
            Purchase_Ammount1 = Purchase_Ammount-total6
            #print("Discount amount:",Purchase_Ammount1)
    
     else:
        if Customer_Gender=="m" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
            total7 =(Purchase_Ammount*5)/100
            Purchase_Ammount1= Purchase_Ammount-total7
            #print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="m" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
            total8 =(Purchase_Ammount*10)/100
            Purchase_Ammount1 = Purchase_Ammount-total8
            # print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="m" and Purchase_Ammount>1000000:
            total9 =(Purchase_Ammount*15)/100
            Purchase_Ammount1 = Purchase_Ammount-total9
            #print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="f" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
            total10 =(Purchase_Ammount*10)/100
            Purchase_Ammount1 = Purchase_Ammount-total10
            #print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="f" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
            total11 =(Purchase_Ammount*15)/100
            Purchase_Ammount1 = Purchase_Ammount-total11
            #print("Discount amount:",Purchase_Ammount1)
        elif Customer_Gender=="f" and Purchase_Ammount>1000000:
            total12 =(Purchase_Ammount*20)/100
            Purchase_Ammount1 = Purchase_Ammount-total12
            #print("Discount amount:",Purchase_Ammount1)
    
     print("Invoice")
     print("="*80)
     print("Customer name: ",Customer_name)
     print("Mobile no.: ", Custmore_mobileno)
     print("Gender:", Customer_Gender)
     print("Age: ", Customer_Age)
     print("Product Name : ",Product_Name)
     print("Product Weight : ",Product_Quntity )
     print("Current price: ",Current_Price,"(1 GRAM)")
     print("Making charge :", Making_charge)
     print("PURCHASE AMMOUNT: ",Purchase_Ammount1)
    
            #Discount in percentage
     if Customer_Age >=60  :
                if Customer_Gender=="m" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
                    Discount =10
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="m" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
                    Discount =15
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="m" and Purchase_Ammount>1000000:
                    Discount =20
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="f" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
                    Discount =15
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="f" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
                    Discount =20
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="f" and Purchase_Ammount>1000000:
                    Discount =25
                    print("Discount Available :",Discount,"%")
        
     else:
                if Customer_Gender=="m" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
                    Discount =5
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="m" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
                    Discount =10
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="m" and Purchase_Ammount>1000000:
                    Discount =15
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="f" and Purchase_Ammount>200000 and Purchase_Ammount<500000:
                    Discount =10
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="f" and Purchase_Ammount>500000 and Purchase_Ammount<1000000:
                    Discount =15
                    print("Discount Available :",Discount,"%")
                elif Customer_Gender=="f" and Purchase_Ammount>1000000:
                    Discount =20
                    print("Discount Available :",Discount,"%")
            
              
     print("-"*50)
     Gst=(Purchase_Ammount1*3)/100
     print("GST:",end="               ")
     print(Gst)
     print("="*50)
     Net_Ammount=Purchase_Ammount1+Gst
     print("Net Ammount:",Net_Ammount) 
else:
    Making_charge3 = Price_Quntity+Making_charge
    print("Invoice")
    print("="*80)
    print("Customer name: ",Customer_name)
    print("Mobile no.: ", Custmore_mobileno)
    print("Gender:", Customer_Gender)
    print("Age: ", Customer_Age)
    print("Product Name : ",Product_Name)
    print("Product Weight : ",Product_Quntity )
    print("Current price: ",Current_Price,"(1 GRAM)")
    print("Making charge :", Making_charge)
    print("PURCHASE AMMOUNT: ",Making_charge3)
    print("-"*50)
    Gst=(Making_charge3*3)/100
    print("GST:",end="               ")
    print(Gst)
    print("="*50)
    Net_Ammount=Making_charge3+Gst
    print("Net Ammount:",Net_Ammount)   