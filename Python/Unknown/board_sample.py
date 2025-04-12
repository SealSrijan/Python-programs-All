def a(msg):
    print(msg)
    return 

def b(a,b,c):
    if a >= b and a >= c:
        print(a,"is larger")
    elif b >= a and b >= c:
        print(b,"is larger")
    elif c >= a and c >= b:
        print(c,"is larger")
    elif a == b and b == c:
        print("All numbers are equal..")
    return 

def c(int):
    for i in range (1, int+1):
        for j in range (65, 65+i):
            print(chr(j), end = " ")
        print("")
    return 

def f(n):
    def perfect_number(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        if n == sum:
            print(n, "is a perfect number.")
        else:
            print(n, "is not a perfect number.")
        return 
    
    def armstrong_number(n):
        if n == ((n%1000//100)**3) + ((n%100//10)**3) + ((n%10//1)**3):
            print(n, "is an Armstrong number.")
        else:
            print(n, "is not an Armstrong number.")
        return 

    def palindrome(n):
        if n == (((n%10//1)*100)+((n%100//10)*10)+((n%1000//100)*1)):
            print(n, "is a palindrome")
        else:
            print(n, "is not a palindrome.")
        return 
    
    perfect_number(n)
    armstrong_number(n)
    palindrome(n)

def g(n):
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break
        else:
            flag = False

    if flag:
        print(n, "is composite")
    else:
        print(n, "is prime")

def h(n):
    a = 0
    b = 1
    print(a,b, end = " ")
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        print(c, end = " ") 
        


a(input("Enter a welcome message: "))
b(int(input("Enter 1st number: ")),int(input("Enter 2nd number: ")),int(input("Enter 3rd number: ")))
c(int(input("Enter number of lines: ")))
f(int(input("Enter number(maximum 3 digit): ")))
g(int(input("Enter number: ")))
h(int(input("Enter number of terms : ")))