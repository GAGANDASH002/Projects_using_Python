#This is a simple game called rock

import random;


print("Computer's Turn: Rock(r) Paper(p) or Scissors(s) ?")
randnum= random.randint(1,3)
if randnum == 1:
    comp='r'
elif randnum == 2:
    comp='p'
elif randnum == 3:
    comp='s'

def gameWin(comp,you):
    if comp==you:
        return None
    
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
        
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True 

you= input("Your Turn: Rock(r) Paper(p) or Scissors(s) ?")
res= gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if res==None:
    print("--------Game is Tied--------")
elif res==True:
    print("--------You Win--------")
elif res==False:
    print("--------You Lose--------")