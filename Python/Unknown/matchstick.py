# Reconstructed Model.. ver 0.2
import random
def toss():   
    choice = input("\nChoose head/tail (h/t): ")
    if choice == random.choice(['h', 't']):
        print("You Win, you start!")
        user_matchstick_game()
    else:
        print("Computer Win, computer starts!")
        comp_matchstick_game()
    return 

def comp_matchstick_game():
    matchstick = 21
    name = input("Enter your name: ")
    while(matchstick > 1):
        print("\n\nRemaining matchstick:", matchstick)
        print("\n\n",name, end=": ")
        user = int(input())
        if(user < 1 or user > 4 or user > matchstick):
            user = int(input("\n\nPick up valid matchstick: "))
        print("Computer pick:", 5- user)
        matchstick -= (5)
    print("\n\nRemaining matchstick: 1\nYou have to pick the last one\n\nSystem wins.!\n You lose.. \n")
    ans2 = input("Do you want to play again? (y/n): ")
    if ans2 == 'y' or ans2 == 'Y':
        toss()
    elif ans2 == 'n' or ans2 == 'N':
        print("Exit")
        exit
    else:
        print("Wrong Entry..")
        exit

def user_matchstick_game():
   matchstick = 21
   name = input("Enter your name: ")
   while matchstick > 1:
        print("\nRemaining matchsticks:", matchstick)
        if matchstick == 21:
            comp = 1  
        else:
            comp = 5 - user  

        if comp > matchstick - 1:
            comp = matchstick - 1
        print("Computer picks:", comp)
        matchstick -= comp
        if matchstick == 1:
            print("\nOnly 1 stick left.")
            print("You have to pick the last one.")
            print("System wins! You lose.")
            break
        print(name, end = ": ")
        user = int(input())
        if user < 1 or user > 4 or user > matchstick - 1:
            user = int(input("Invalid pick. Choose 1-4 sticks, but leave at least one: "))
        matchstick -= user
        if matchstick == 1:
            print("\nOnly 1 stick left.")
            print("Computer has to pick the last one.")
            print("You win!")
            break

ans = input("Welcome to the MATCHSTICK GAME.\n\nDo you want to play? (y/n): ")
if(ans == 'y' or ans == "Y"):
    print("\n\nRules for the game are as follows.\n \n")
    print("1. A toss is done, outcome is completely random, if You win, You start, else Computer starts")
    print("2. There are 21 matchsticks.")
    print("3. You are allowed to pick(choose) only 1 or 2 or 3 or 4 matchsticks at a time.")
    print("4. The last person to pick the match will lose the game")
    toss()
elif(ans == 'n' or ans == "N"):
    print("Exit")
    exit
else:
    print("Wrong Choice..")
    exit