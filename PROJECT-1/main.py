'''
1 for snake
-1 for water
0 for gun
'''
"""
 Snake drinks/beats Water, Water douses/beats Gun, and Gun shoots/beats Snake

 
"""
import random

computer = random.choice([0, 1, -1])
# print(num)
youip=input("Enter your choice")
youdict={
    "s":1,
    "w":-1,
    "g":0
}
reverseddict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}
you=youdict[youip]
print(f"You chose {reverseddict[you]}, Computer chose {reverseddict[computer]}")
if(you==computer):
    print("Its draw!!")
else:
    if(you==1 and computer==-1):
        print("You won!!")
    elif(you ==-1 and computer==1):
        print("You lose and computer wins!!")
    elif(you==0 and computer==1):
        print("You lose and computer wins!!")
    elif(you==0 and computer==-1):
        print("You won!!")
    elif(you==1 and computer==0):
        print("you won")
    elif(you==1 and computer==-1):
        print("You won")
    elif(you==-1 and computer==0):
        print("You won!!")
    elif(you==-1 and computer==1):
        print("you lost and computer wins")
    else:
        print("Somethig went wrong")

