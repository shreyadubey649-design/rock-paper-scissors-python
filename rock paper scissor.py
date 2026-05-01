import random
print("WELCOME TO THE GAME OF ROCK, PAPER AND SCISSORS!")
sc=0
su=0
round=1
choices=['Rock','Paper','Scissor']
while round <= 5:
    print("ENTER YOUR CHOICE BELOW:")
    ans=input()
    print("You chose:", ans)
    a=random.choice(choices)
    print("Computer chose:", a)
    if ans=='Rock' or ans=='rock':
        if a=='Rock':
            print("IT'S A TIE!")
        elif a=='Paper':
            print("COMPUTER WINS!")
            sc+=1
        else:
            print("YOU WIN!")
            su+=1
    elif ans=='Paper' or ans=='paper':
        if a=='Rock':
            print("YOU WIN!")
            su+=1
        elif a=='Paper':
            print("IT'S A TIE!")
        else:
            print("COMPUTER WINS!")
            sc+=1
    elif ans=='Scissor' or ans=='scissor':
        if a=='Rock':
            print("COMPUTER WINS!")
            sc+=1
        elif a=='Paper':
            print("YOU WIN!")
            su+=1
        else:
            print("IT'S A TIE!")
    else:
        print("Invalid input!")
    round+=1
print("\nFINAL SCORE:")
print("User:", su)
print("Computer:", sc)
if su > sc:
    print("YOU ARE THE FINAL WINNER!")
elif sc > su:
    print("COMPUTER IS THE FINAL WINNER!")
else:
    print("MATCH IS A DRAW!")
