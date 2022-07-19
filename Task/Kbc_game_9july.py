#-----------------------------------------
from telnetlib import STATUS


def new_game():
    guesses =[]
    Correct_guess=0
    
    question_num=1
    for key in questions:
        print("-----------------------------------------")
        print(key)
        for i in options1[question_num-1]:
            print(i)
        guess =input("Enter (A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        Correct_guess += Check_answer(questions.get(key),guess)
        
        
        question_num +=1
    display_score(Correct_guess,guesses) 
 
#-----------------------------------------
def Check_answer(answer,guess):
    if answer == guess:

        print("Correct Answer")
        
        
        return +50
    else:
        print("Wrong")
        
        return -20
    
#-----------------------------------------
def display_score(Correct_guess,guesses):
    print()
    print("Result")
    print()
    print("Answer:",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    
    
        

    #score = int((Correct_guess)*50)
    #print("Your Score is"+str(score))
    print("Your Score is"+str(Correct_guess))

    
#-----------------------------------------
def play_again():
    choice=input("do you want play again press 'y' for yes 'n' for no:")
    if choice=='n' or choice=='no' or choice=='No'or choice=='N':
        return False
    else:
        return True
#-----------------------------------------

questions={  

    "What can you catch but cannot throw?":"A",
    "Pick me up and scratch my head. I’ll turn red and then black. What am I?":"B",
    "I can be broken without being touched or even being seen. What am I?":"C",
    "I have a neck, but I don’t have a head, and I wear a cap. What am I?":"A",
    "If you have it, you want to share it. If you share it, you don’t have it anymore. What is it?":"B",
    "What tree do we all carry in our hands?":"C",
    "What is always coming but never arrives?":"A",
    "What runs around a house but does not move?":"D",
    "I can’t be seen, but I can be heard. I won’t answer until spoken to. What am I?":"B",
    "What is as light as a feather but can’t be held by anyone for very long?":"D"
     
    }

options1=[["A. cold","B. tennis ball","C.Your toys","D. boomerang"],
          ["A. Candle","B. match","C.Caterpillar","D.Caterpillar"],
          ["A. Glass","B.Window ","C. promise","D.Ice"],
          ["A. Bottle","B. Ghost","C.Snake","D.Calm"],
          ["A. Love","B. Secret","C.Talent","D.None of Above"],
          ["A. Cedar","B. Oak","C.Palm","D. Eucalyptus"],
          ["A. Tomorrow","B. A train","C.Your paycheck","D. The mail"],
          ["A.A dog","B. An alarm","C.A garden gnome","D. A fence"],
          ["A. A dream","B. Echo","C.Children","D. A voice"],
          ["A. Tissue paper","B. A baby","C.Your word","D. Your breath"]
        ]
STATUS=True
while STATUS:
    new_game()
    play_again()
print("Thanks")