#Session 2
#Conditional Operators (String er part ta skip korlam)

#code to check whether one is able for driving
age = int(input("Enter your age: "))
if(age >= 18):
    print("Can drive!")
else:
    print("Cannot drive now, have to wait for another", 18-age, "years")

#code to check the colour of traffic light
light = input("\nEnter colour: ")
if(light == "red"):
    print("Stop!")
elif(light == "yellow"):
    print("Wait!")
elif(light == "green"):
    print("Go!")
else:
    print("Wrong entry.")

#important thing to note, there is no {} block in Python, we have to use indentation(proper spacing)
#jmn opore dekhlei bojha jbe if er por <space> elif er por <space>, kono {} hbe na

#Grade checker
marks = int(input("\nEnter marks obtained: "))
if(marks >= 90):
    grade = "A"
elif(marks < 90 and marks >= 80):
    grade = "B"
elif(marks < 80 and marks >= 70):
    grade = "C"
else:
    grade = "D"

print("Obtained grade:", grade)

#End of Lecture 2
#---------------------------------------------------------------------------------------------------------------------------------#

#PRACTICE SET

#WAP to check if a number entered by user is odd or even
num = int(input("Enter number: "))
if(num % 2 == 0):
    print(num,"is even")
else:
    print(num, "is odd")

#WAP to find the greatest of 3 numbers entered by the user
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if(x > y and x > z):
    print(x,"is the greatest")
elif(y > x and y > z):
    print(y, "is the greatest")
else:
    print(z, "is the greatest")

#WAP to check if a number is a multiple of 7 or not
num2 = int(input("Enter number: "))
if(num2 % 7 == 0):
    print(num2, "is a multiple of 7")
else:
    print(num2, "is not a multiple of 7")

#END OF SESSION 2 (55:40)