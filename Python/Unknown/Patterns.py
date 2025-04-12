while(True): 
    choice  = input("\nEnter your choice from content book[Q to quit]: ")
    # * triangle of desired length (forward)
    if(choice == 'A' or choice == 'a'):     
        n = int(input("Enter number of lines: "))
        i = 1
        j = 1
        for i in range (1,n+1):
            for j in range (i):
                print("* ", end="")
            print()
    
    # * triangle of desired length (backward)
    elif(choice == 'B' or choice == 'b'):
        n = int(input("Enter number of lines: "))
        i = 1
        j = 1
        for i in range (1,n+1):
            for j in range (n,i-1, -1):
                print("* ", end="")
            print()

    #1-2-3 triangle
    elif(choice == 'C' or choice == 'c'):
        n = int(input("Enter number of lines: "))
        i = 1
        j = 1
        for i in range (1,n+1):
            for j in range (1,i+1):
                print(j," ", end="")
            print()

    #Floyd's Triangle (forward)
    elif(choice == 'D' or choice == 'd'):
        n = int(input("Enter number of lines: "))
        i = 1
        j = 1
        k = 1
        for i in range (1,n+1):
            for j in range (1,i+1):
                print(k," ", end="")
                k += 1
            print()

    #Floyd's Triangle (backward)
    elif(choice == 'E' or choice == 'e'):
        n = int(input("Enter number of lines: "))
        i = 1
        j = 1
        k = 1
        sum = 0
        for i in range (1,n+1):
            sum += i
            k = sum
        for i in range (1,n+1):
            for j in range (1,i+1):
                print(k," ", end="")
                k -= 1
            print()

    #Fibonacci series
    elif(choice == 'F' or choice == 'f'):
        a = 0
        b = 1
        n = int(input("Enter upto which you want fibonacci series: "))
        print(a)
        print(b)
        for i in range (2, n+1):
            c = a+b
            a = b
            b = c
            print(c," ")

    #Armstrong number b/w 0 to 1000
    elif(choice == 'G' or choice == 'g'):
        print("Armstrong number b/w 1 to 1000: ")
        for n in range(0, 1000):
            a = n % 1000 / 100
            b = n % 100 / 10
            c = n % 10 / 1

            if(n == ((int(a)**3)+(int(b)**3)+(int(c)**3))):
                print(n)

    #Pyramid
    elif(choice == 'H' or choice == 'h'):
        n = int(input("Enter number of lines: "))
        for i in range (1,n+1):
            for j in range (1,n-i+1):
                print(end=" ")
            for k in range (1, i+1):
                print("*", end=" ")
            print()

    #Backside Triangle
    elif(choice == 'I' or choice == 'i'):
        n = int(input("Enter number of lines: "))
        for i in range (1, n+1):
            for j in range(1, n-i+1):
                print("\t", end=" ")
            for k in range (1,i+1):
                print("\t*", end=" ")
            print()

    #Numerical Triangle
    elif(choice == 'J' or choice == 'j'):
        n = int(input("Enter number of lines: "))
        l = 1
        for i in range (1,n+1):
            for j in range (1,n-i+1):
                print(end=" ")
            for k in range (1, i+1):
                print(l, end=" ")
                l += 1
            print()

    #Palindrome Numbers
    elif(choice == 'K' or choice == 'k'):
        n = 0
        sum = 0
        temp = 0
        s = 0
        print("The palindrome numbers from 1 to 1000: ")
        for n in range(1, 1000+1):
            temp = n
            sum = 0
            while(temp != 0):
                s = temp % 10
                sum = (sum*10)+ s
                temp = temp //10
            if(n == sum):
                print(n, end=" ")

    #Prime Numbers
    elif(choice == 'L' or choice == 'l'):
        print("All prime numbers from 1 to 100: ")
        for i in range (2, 100+1):
            prime = 1
            for j in range (2, (i//2)+1):
                if (i % j == 0):
                    prime = 0
                    break
            
            if(prime):
                print(i, "", end=" ")

    elif(choice == 'Q' or choice == 'q'):
        print("\n\n\tEND\n\n")
        break