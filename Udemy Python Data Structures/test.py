#!/usr/bin/python3

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


if __name__ == '__main__':
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
