'''
rock :0
paper:1
scissor :-1
'''
import random

computer = random.choice([0, 1, -1])
# print(computer)
youstr=input("Enter the  choice")
youdict={
    "r":0,
    "p":1,
    "s":-1
}
you=youdict[youstr]
reverseddict={
      0:"rock",
    1:"paper",
    -1:"scissor"
}
print(f"You chose {reverseddict[you]} and computer chose {reverseddict[computer]}")
if(you ==computer):
    print("Its draw")
else:
    if(you==0 and computer==1):
        print("You lose, Computer won!!")
    elif(you ==0 and computer==-1):
        print("You won!!")
    elif(you==1 and computer==0):
        print("You won!!")
    elif(you==1 and computer==-1):
        print("You lose, Computer won!!")
    elif(you==-1 and computer==0):
        print("you lose, Computer won!!")
    elif(you==1 and computer==-1):
        print("You lost, Computer wons")
    elif(you==-1 and computer==0):
        print("You lost, computer won!!")
    elif(you==-1 and computer==1):
        print("You won!!")
    else:
        print("Something went wrong")
