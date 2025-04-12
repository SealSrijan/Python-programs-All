#for printing
#one line er

print("Hello world")

#ekta line ei pasapashi 2to separate line.. comma(,) diye lekha hoe

print("My name is Srijan.", "I am learning Python")

#seperate line, ba porer line er jonno kono \n lagbe na, emni alada line e print likhte hbe, byaas!! r jodi icche hoe, ektar moddhyei hbe then \n

print("Line 1: Semester 3")
print("Line 2: Semester 4")

#cholo eibaar sekha jaak Variable niye.. ekhane C er moto kono variable type declare korte hobe na, like int, float, string.. e Bhai automatic niye ney.. jmn

name = "Srijan"
name2 = "Python"
age = 17
experience = 0.1
boolean = False

print("My name is", name, "I am learning", name2, "My age is", age, "My experience in Python is", experience,"years")

#mojadar jinis, konta ki type er variable setao Python bole debe.. <3

print(type(name), type(name2), type(age), type(experience), type(boolean))

#1st sum

a = 5
b = 2
sum = a+b
print(sum)

#ekhane ja icche kora jay, -, *, /
# mojadar byapar ta hocche amke age theke kono type specify korte hocche na, like division e ki hbe.. o automatic shift kre nicche from int to float and vice versa
#na eta amar bhul dharona, division korle always float ei kore nicche..

#arithmertic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b) #to the power of.. a^b

#relational operators(just like C)
# ==, !=, <, <=, >, >= etc.. Answer e True ba False debe..

print(a > b) #True
print(a == b) #False

#assignment operators(same like C)
# =, +=, -+, *=, /=, %=, **=

a += 1
print(a)

#NOTUN PART
#Logical Operators
#NOT(just reverse True and False), AND(Only True if both are True, else False), OR(Always True unless both are False)

val1 = 50
val2 = 20
bool1 = True
bool2 = False
print("!True:", not bool1)
print("True and False:",bool1 and bool2) #True and False ==> False(since one is False)
print("True and True:",bool1 and bool1) #True and True ==> True(since both are True)
print("True or False:",bool1 or bool2) #True or False ==> True(since one is true)

print("!(50 != 20):",not(a!=b)) #a!=b ==> True, not True ==> False
print("(50>20) and (50>0):",(val1>val2) and (val1>0)) #both are True.. ==> True
print("(50!=20) or (50<20):",(val1 != val2) or (val1<val2)) #True or False.. ==>True

#type conversion(just like C).. agei bolechi python kaka automatically nijer moto float int niye ney
print(type(float(a)))

#Now comes the scanf() in python.. input()
#C te jmn amra age ekta variable banie store kori, ekhane oishob nei
#jaai debo taai niye nebe, jmn dhora jaak

name = input("Enter your name: ")
print("Welcome", name)

#ekdom ezz.. ez hole ki hbe problem ache, ekhane jaai input() diye pass korabo, sob ei string niye nebe.. 5 pass korale "5" hoe jabe
#so ami input() diye jinis tule +, -, *, / korte parbo na, type casting korte hobe.. jmn

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print("Sum is", num1+num2) #simpul ekdum !! jate icche convert korte parbo, Jaat noy, type.. :)
print("Float sum is", float(num1+num2))

#sudhu jdi input() chere di, string nebe, r operation korbe na.. kintu + diye string concatenate kora jaay

str1 = input("Enter first name: ")
str2 = input("Enter surname: ")
print("Your name:", str1+str2)

#End of Lecture 1
#--------------------------------------------------------------------------------------------------------------------------------------------#

#PRACTICE PROBLEMS
#Write a program to enter side of square and find its area.

side = float(input("Enter side of a square: "))
print("Area of the square with side", side, "unit is", side**2, "sq. unit")

#Write a program to input to 2 floating numbers and print their average

x = float(input("Enter 1st float number: "))
y = float(input("Enter 2nd float number: "))
print("Average is", (x+y)/2)

#WAP to input 2 int numbers a and b. Print True if a is greater than or equal to b. If not print False

a1 = int(input("Enter 1st number: "))
b1 = int(input("Enter 2nd number: "))
print(a1 >= b1)

#END OF SESSION 1 (1:22:18)