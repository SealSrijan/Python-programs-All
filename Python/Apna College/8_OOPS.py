#khub kothin, mathay dhukche na ardhek jinis eiii
#1st we have to define class, then objects
# odbhut sob function, init f(x)

class Student: #ei ta puro Class, database er onek ta
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new students..")

s1 = Student("Srijan", 93.75)
print(s1.name, s1.marks)
s2 = Student("Swapnonil", 94)
print(s2.name, s2.marks)

#Create a student Class that takes name and marks of 3 subjects as argument in constructor. Then create a method to print their average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        return(sum/3)

numbers = input("Enter marks separated by space: ")
numbers = numbers.split()
s1 = Student(input("Enter your name: "),list(map(int, numbers)) )
print(s1.name, s1.marks)
print(s1.avg())