
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