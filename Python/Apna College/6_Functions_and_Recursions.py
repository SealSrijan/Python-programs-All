#Functions

#WAP to find Average of 3 numbers

def average(a,b,c):
    avg = (a + b + c)/3
    return avg

print(average(int(input("Enter 1st num: ")), int(input("Enter 1st num: ")), int(input("Enter 1st num: "))))

#WAF to print the length of a list. (list is the parameter)
num = [1,2,3,4,5,6]
def length(list):
    return len(list)

print(length(num))

#WAF to print the elements of a list. (list is the parameter)
num = ["a", "b"]
def length(list):
    for i in range (0, len(list)):
        print(list[i], end = " ")

length(num)

#WAF to find factorial of n
def fact(n):
    factorial = 1
    for i in range (1, n+1):
        factorial *= i
    return factorial

print("Factorial is:", fact(int(input("Enter n: "))))

def convertor(USD):
    INR = USD * 85.57
    return INR

print("INR: ", convertor(float(input("Enter USD: $",))), end="")
