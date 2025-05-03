name = input("Enter your name: ")
char = []
for i in name:
    char.append(i)
for i in range(1,len(name)+1):
    for j in range (i):
        print(char[j], end = " ")
    print()