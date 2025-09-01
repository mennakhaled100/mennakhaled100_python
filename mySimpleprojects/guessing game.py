#Random Number Generation
import random
from xml.dom.minidom import ProcessingInstruction


def randomGen() :
    return random.randint(0, 100)


secret = randomGen()

count = 0
#Feedback Mechanism
while(True) :
    player_guess = int(input("Enter your number: \n"))
    if player_guess == secret:
        count+=1
        print(f"Win! \n")
        break
    elif player_guess < secret:
        print("It's lower")
        count+=1
    else :
        print("It's greater")
        count+=1


print(f"you found guess number {secret} in {count} tries")
