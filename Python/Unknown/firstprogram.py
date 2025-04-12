#Basic Calculator

print("The calculator can perform only two digit operations")
ans = str(input("Do you want to start? [Y]es or [N]o: "))
if ans.upper() == 'Y':


    symbol = str(input("What programme do you want to perform? [+, -, x, / ,[P]ower: "))

    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))

    if symbol == '+':
        print ("The sum is" ,x+y)
    elif symbol == '-':
        print ("The difference is" ,x-y)
    elif symbol == 'x':
        print ("The product is" ,x*y)
    elif symbol == '/':
        print ("The quotient is" ,x/y)
    elif symbol.upper() == 'P':
        print ("The 1st number to the power of 2nd is" ,x**y)

else:
    print ("Wrong choice")