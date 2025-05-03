#Dictionary
info = {
    "name" : "Srijan",
    "surname" : "Seal",
    "age" : 17,
    "percentage" : 93.75
}
print(info)
print(info["name"]) #can also access data by putting like index "name"

#empty dictioanry
dict = {}
dict["name"] = input("Enter your name: ")
print(dict)
#after creating a dictionary we can add elements further
#dictionary name may be string or tuple or any data type that are immutable..

#nested dictionary
Class = {
    "student" : "Srijan",
    "subject" : {
        "phys" : 94,
        "chem" : 96,
        "maths" : 98
    },

    "student2" : "Ayush",
    "subjects" : {
        "stat" : 98,
        "econ" : 99,
        "maths" : 94
    }
}
# print(Class["student"], Class["subject"]["phys"], Class["student2"], Class["subjects"]["econ"])

#Dictionary Methods
print(Class.keys())
#to store as list
print(list(Class.keys())) #type casting
print(len(Class)) #length of the Dictionary

#SET is very similar to set in mathematics
set1 = {1,2,2,3,4}
print(set1) #removes duplicate values
set2 = {2,5,3,6}
print(set1.union(set2)) #{1,2,3,4,5,6}
print(set1.intersection(set2)) #{2,3}

dice = {"1",'2','3','4','5','6'}
print("You played:", dice.pop())

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("Number of classrooms needed:",len(subjects))

#WAP to enter marks of 3subjects from the user and store them in a Dictionary. Start with an empty dictionary & add one by one.
marks = {}
marks["English"] = int(input("Enter marks\nEnglish: "))
marks["Bengali"] = int(input("Bengali: "))
marks["Mathematics"] = int(input("Mathematics: "))
print(marks)

#WAP to store 9 and 9.0 as separate in set.
value = {'9', 9.0}
print(value)

#END of LECTURE 4(54:31)