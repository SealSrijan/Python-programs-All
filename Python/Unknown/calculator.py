while(True):
    option = input("Enter option: ")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if (option == '+'):
        print(a+b)
    elif (option == '-'):
        print(a-b)
    elif (option == '*'):
        print(a*b)
    elif (option == '/'):
        print(a/b)
    elif (option == '//'):
        print(a//b)
    elif (option == '**'):
        print(a**b)
    elif(option == 'q'):
        break

# to_do_list = []
# while(True):
#     ans = input("\nType 'new' to add new list or 'remove' to remove\n")
#     if(ans == "new"):
#         to_do_list.append(input("\nEnter new list: "))
#         print("Updated list:",to_do_list, end=" ")
#     elif(ans == "remove"):
#         print(to_do_list.remove())