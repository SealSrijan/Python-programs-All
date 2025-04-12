#Session 3
#So what is List?
#List kichui na, C te jmn array, tmn ei python e List, simpul !!

#interesting fact, python er list e amra ja icche data type er jinis rakhte pari, not necessary same ei hote hbe..

#1st List
numbers = [0, 1, 2, 3, 4, 5] #list e []er moddhye jinis likhte hoe
print(numbers)
print(len(numbers)) #to find the length

random = ["Srijan", 17, "Seal", 94.00] #different data type.. accessed by index numbers.. niche dekho.. ↓
print("My name is", random[0], random[2], "My age is", random[1], "I obtained", random[3], "percent in Madhyamik")

#Basic difference between STRING and LIST
    #STRING is immutable i.e., we cannot change the value of a particular index of a string
    #LIST is mutable i.e., we can change the value.. like

random[0] = "S."
print("My name is", random[0], random[2], "My age is", random[1], "I obtained", random[3], "percent in Madhyamik")

#List Slicing(important for MCQ)
print(numbers[1:4]) #[starting_index to ending_index-1]
print(numbers[ : 2]) #starts from 0
print(numbers[2: ]) #ends at last, len(numbers)

#List Methods
#Let us consider a List

list = [2,1,3]
list.sort() #list.sort() returns NULL value... ASCENDING ORDER
print("In ascending order:",list)
list.sort(reverse = True)
print("In descending order:", list)#list.sort(reverse = True).. DESCENDING VALUE

#string eo sorting kora jbe... list alphabet diye hoe.. ASCII value diye hoe... 
fruits = ["litchi", "mango", "Banana", "cherry", "apple" , "Guava"]
fruits.sort()
print(fruits)

#reverse list o possible...
list.reverse()
print(list)

#Tuples in python
#Same like list, but it is immutable..
tuple = (1, 2, 3) #written in () rather than []

#can access index
print(tuple[1])

#cannot assign any value, as it is immutable

#error: tuple[3] = 5

#IMPORTANT THING..

tup1 = (1) #tup1 is treated as int
tup2 = (1, ) #tup2 is treated as tuple
print(type(tup1), tup1)
print(type(tup2), tup2)

#Slicing also possible

#TUPLE METHOD
tuple = (1, 2, 3, 1, 2)
print(tuple.index(2)) 
print(tuple.count(2))

#----------------------------------------------------------------------------------------------------------------------------------------#

#PRACTICE SET
#WAP to ask the user to enter names of their 3 favourite movies and store them in a list
movie1 = input("Enter name of your First favourite movie: ")
movie2 = input("Enter name of your Second favourite movie: ")
movie3 = input("Enter name of your Third favourite movie: ")
movie = [movie1, movie2, movie3]
print("Your favourite movies are:", movie)
#OR
movie = []
movie.append(input("1st: "))
movie.append(input("2nd: "))
movie.append(input("3rd: "))
print(movie)

#WAP to check if a list contains a palindrome of elements
list1 = [1,2,3,4,1]
temp = list1.copy()
list1.reverse()
list2 = list1
if(temp == list2):
    print(list1,"is palindrome")
else:
    print(list1, "is not palindrome")

#WAP to find the number of students with the "A" grade in the following tuple. Also store them to list and sort from "A" to "D"
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

Grade = ["C", "D", "A", "A", "B", "B", "A"]
Grade.sort()
print(Grade)

#END OF LECTURE 3 (41:45)

print("Hello World")