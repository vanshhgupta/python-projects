#Random Program-2
#Making a rock, paper and scissors game using random module

import random
print("rock, paper,scissors game")
print("GAME RULES")
print("there will be 5 rounds. Chose among the three options and try to win from computer")
print("rock vs paper-> paper wins")
print("rock vs scissor-> rock wins")
print("paper vs scissor-> scissor wins")
print("")
print("GAME STARTS")
print("")
l=["rock", "scissor", "paper"]

while True:
    ucount=0
    ccount=0
    uc=int(input(' Game Start.....\n Enter 1. Yes\n Enter 2. NO Exit\nenter: '))

    if uc==1:
           for a in range(1,6):
               userInput=int(input('1.Rock\n2.Scissor\n3.Paper\nEnter your choice: '))
               
               if userInput==1:
                   uchoice="rock"
               elif userInput==2:
                    uchoice="scissor"
               elif userInput==3:
                    uchoice="paper"
               cchoice=random.choice(l)
                
               if cchoice==uchoice:
                    print("Computer Value", cchoice)
                    print("User Value", uchoice)
                    print("Game Draw")
                    print("")
               elif (uchoice=="rock" and cchoice == "scissor") or ( uchoice =="paper" and cchoice == "rock") or (uchoice=="scissor" and cchoice=="paper"):
                    print("Computer Value", cchoice)
                    print("User Value", uchoice)
                    print("You Win")
                    print("")
                    ucount=ucount+1
               else:
                    print("Computer Value", cchoice)
                    print("User Value", uchoice)
                    print("Computer Win")
                    print("")
                    ccount=ccount+1

    else:
        break

    if ucount>ccount:
                    print("Computer Value", cchoice)
                    print("User Value", uchoice)
                    print("YOU WON THE GAME")
    elif ucount<ccount:
                    print("Computer Value", cchoice)
                    print("User Value", uchoice)
                    print("COMPUTER WON THE GAME")
