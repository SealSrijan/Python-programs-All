#Loop toh same ei.. Let's start with while loop

#while condition:
    #do this
    #and this...
    #operation... like ↓

count = 1
while count <= 5:
    print(count,"Hello World")
    count += 1

#from 5 to 1
i = 5
while i >=1 :
    print(i)
    i -= 1

#Print the multiplication table of number n
n = int(input("Enter n: "))
i = 1
while i<= 10:
    print(n,"*",i, "=", n*i)
    i += 1

num = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i< len(num):
    print(num[i])
    i+= 1

num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number you want to find: "))
i = 0
while i < len(num):
    if(x == num[i]):
        flag = True
        break
    else:
        flag = False

    i+= 1
if(flag):
    print("Found")
else:
    print("Not found")

num = [1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)

num = (1,4,9,16,25,36,49,64,81,100)
count = 0
x = int(input("Enter the number you want to find: "))
for i in range (0, len(num)):
    if(num[i] == x):
        print("Found at", i)
        count += 1
    else:
        print("finding..")
print("Element found",count,"time")

n = int(input("Enter n: "))
i = 1
for i in range(1,11): #(start?, stop, step?) --> ?denote not compulsory by deafult 0 and 1 respectively.. stop = stop -1 [REMEMBER  IMPORTANT]
    print(n,"*",i, "=", n*i)
    i += 1

#PRACTICE SET
#WAP to find the sum of first n numbers
n = int(input("Enter n: "))
i = 1 
sum = 0
while i <= n:
    sum = sum+i
    i += 1
print("Sum is", sum)

#WAP to find the factorial a number
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(n,"! = ", fact)

#END OF LECTURE 5(1:03:50)