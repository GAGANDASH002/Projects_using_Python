'''GUESS THE NUMBER'''

import random

target=random.randint(1,100)#generates random number between  and 100

while True:
    userChoice=(input("Guess the target or Quit:"))
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Congratulations!: You guessed correctly")
        break
    elif(userChoice<target):
        print("number too small , guess again")
    else:
        print("number too big , guess again")

print("-----GAME OVER-----")