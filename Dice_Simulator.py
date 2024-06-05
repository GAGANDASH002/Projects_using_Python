import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")#for printing Unicode charachters
#● ┌ ─ ┐ │ └ ┘ 

" ┌─────────┐ "
" │         │ "
" │         │ "
" │         │ "
" └─────────┘ "

dice_art={
    1:(" ┌─────────┐ ",
       " │         │ ",
       " │    ●    │ ",
       " │         │ ",
       " └─────────┘ "),
    2:(" ┌─────────┐ ",
       " │ ●       │ ",
       " │         │ ",
       " │       ● │ ",
       " └─────────┘ "),
    3:(" ┌─────────┐ ",
       " │ ●       │ ",
       " │    ●    │ ",
       " │       ● │ ",
       " └─────────┘ "),
    4:(" ┌─────────┐ ",
       " │  ●   ●  │ ",
       " │         │ ",
       " │  ●   ●  │ ",
       " └─────────┘ "),
    5:(" ┌─────────┐ ",
       " │ ●    ●  │ ",
       " │    ●    │ ",
       " │ ●    ●  │ ",
       " └─────────┘ "),
    6:(" ┌─────────┐ ",
       " │ ●  ●  ● │  ",
       " │         │ ",
       " │ ●  ●  ● │ ",
       " └─────────┘ ")
}#creating dictionary

dice=[]#initializing empty list
total=0
num_of_dice=int(input("-----Enter the number of dice you want to play with-----"))


for die in range(num_of_dice):
    choice=random.randint(1,6)
    dice.append(choice)

#prints dice in different lines

#=for die in range(num_of_dice):
#  for line in dice_art.get(dice[die]):
#      print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")   
    print()

for die in dice:
    total+=die
print("Your Total is",total)