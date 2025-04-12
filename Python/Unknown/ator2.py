a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
choice = input("Enter choice: ")
while True:
    if choice == '+':
        print("Sum is", a+b)
        break
    elif choice == '-':
        print("Difference is", a-b)
        break
    elif choice == '*':
        print("Product is", a*b)
        break
    elif choice == '/':
        print("Quotient is", a/b)
        break
    elif choice == '//':
        print("Quotient is", a//b)
        break
    elif choice == '**':
        print("Power of a to b is", a**b)
        break
    elif choice == 'Q':
        break