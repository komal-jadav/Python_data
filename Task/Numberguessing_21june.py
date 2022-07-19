#Number Guessing Game
import random

Computer_Guess=random.randint(1,100)
trial=5
while trial>0:
    user_guess=int(input("Enter one no:"))
    if user_guess>Computer_Guess:
        print("HINT: Enter lower no:")
    elif user_guess<0:
        print("HINT: Enter higher no:")
    else:
        print("You GOT IT")
        trial=0
    trial-=1