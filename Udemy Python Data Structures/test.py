# def my_sum(*a):
#     sum = 0
#     for i in a:
#         sum = sum + i
#     print(sum)
#
# def display():
#     print('Hello')
#     return 0
#
# print(type(display()))
# my_sum(1, 2, 3, display(), 4, 5, 6)

# import math
# print(dir(math))
# math_contents = dir(math)
# for item in math_contents:
#     print(item)

# from math import pi, e
# print(pi)
# print(e)
# print(math.sqrt(25))

class Student:
    """This is class Student v1.0.0"""

    college = 'CWRU'
    count = 0
    students = []

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.__marks = 0
        Student.students.append(self)
        Student.count += 1

    def __str__(self):
        return 'This is class Student'
    
    def display(self):
        print('College:', Student.college)
        print('Name:', self.name)
        print('Class Number:', self.roll)
        print('Grades:', self.__marks)

S = Student('John', 101)
S2 = Student('Dave', 102)

print(S.college)
print(S.name)
print(S.roll)
# print(S.__marks)    # Generates error
print(S.__doc__)
print(S)
print(dir(S))
S.display()
S.__marks = 100.00
print('New grades:', S.__marks)
for student in Student.students:
    print(student.name)
print(Student.students)
print(Student.count)