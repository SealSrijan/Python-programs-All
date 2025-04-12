qs = input("Enter: ")
with open("AI.txt", "r+") as f:
    dict = f.read().split("\n")
    for i in dict:
        if(qs == i):
            print("PC: Hello") 

#Aro paka pokto na hole mathaa khulche na, type casting shikhte hbe
#Eiboyosh e matchstick ei korte hbe...