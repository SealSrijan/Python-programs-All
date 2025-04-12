list = []

def entry_list(list):
    max = int(input("Enter max limit: "))
    num = 0
    while num != max:
        list.append(int(input("Enter elements in list: ")))
        num += 1
    print("Entered list:", list)
    return

def min_max(list):
    print(max(list))
    print(min(list))
    return 

def mean(list):
    mean = 0
    for i in list:
        mean += i
    print(mean/len(list))
    return 

def linear_search(list):
    n = int(input("Enter the number you want to find: "))
    count = 0
    for i in list:
        count += 1
        if i == n:
            print("Found at:", count)
            break
        elif count == len(list):
            print("Not found")
    return 

def frequency(list):
    n = int(input("Enter whose frequency you want to know: "))
    count = 0
    for i in list:
        if n == i:
            count += 1
    print("Frequency of", n,"is:",count)
    return 

entry_list(list)
while True:
    ans = int(input("\nEnter choice(0 to exit): "))
    if ans == 1:
        min_max(list)
    elif ans == 2:
        mean(list)
    elif ans == 3:
        linear_search(list)
    elif ans == 4:
        frequency(list)
    else:
        break