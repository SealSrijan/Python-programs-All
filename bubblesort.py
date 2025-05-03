num = []
max = int(input("Enter max limit: "))

for i in range(max):
    num.append(int(input("Enter elements: ")))
num.sort()
for i in num:
    print(i, end = " ")

for i in num:
    print(i, end = " ")
for i in range(max-1):
    for j in range (max - i - 1):
        if(num[j] > num[j+1]):
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp

for i in num:
    print(i, end = " ")