#Sample programs

#1. patterns
def patterns():
    with open("Patterns.py", "r") as f:
        print(f.read())
    return 

#2. Summation
def summation():
    n = int(input("Last term: "))
    sum = 0
    cd = int(input("Enter common difference: "))
    for i in range(1, n+1, cd):
        sum += i
    print("Summation is:", sum)
    return
#3. Factorial
def fact():
    n = int(input("Enter number for factorial: "))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(n,"! :", fact)

#driver code
ans = input("Enter choice: ")
if ans == "patterns":
    patterns()
elif ans == "summation":
    summation()
elif ans == "factorial":
    fact()
