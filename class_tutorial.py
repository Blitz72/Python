# Python Object Oriented Programming (OOP) - For Beginners

# https://www.youtube.com/watch?v=JeznW_7DlB0

###############################################################

# class Student:
# 	def __init__(self, name, age, grade):
# 		self.name = name
# 		self.age = age
# 		self.grade = grade

# 	def get_grade(self):
# 		return self.grade


# class Course:
# 	def __init__(self, name, max_students):
# 		self.name = name
# 		self.max_students = max_students
# 		self.students = []

# 	def add_student(self, student):
# 		if len(self.students) < self.max_students:
# 			self.students.append(student)
# 			return True
# 		return False

# 	def get_avg_grade(self):
# 		sum = 0
# 		for student in self.students:
# 			sum += student.get_grade()
# 		return sum/len(self.students)


# s1 = Student("Dave", 47, 96)
# s2 = Student("Christy", 43, 100)
# s3 = Student("Abby", 15, 99)
# s4 = Student("Hannah", 12, 99)
# s5 = Student("Leah", 10, 99)

# course = Course("Math", 5)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# course.add_student(s4)
# print(course.add_student(s5))
# print(course.get_avg_grade())

###############################################################

# class Pet:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def show(self):
# 		print(f"I am {self.name} and I am {self.age} years old!")

# 	def speak(self):
# 		print("I don't know what to say!")


# class Cat(Pet):
# 	def __init__(self, name, age, color):
# 		super().__init__(name, age)
# 		self.color = color

# 	def speak(self):
# 		print("Meow!")

# 	def show(self):
# 		print(f"I am {self.name}, I'm {self.age} years old, and I'm {self.color} colored!")


# class Dog(Pet):
# 	def speak(self):
# 		print("Bark!")


# class Fish(Pet):
# 	pass


# p = Pet("Chippy", 2)
# p.show()
# p.speak()

# c = Cat("Calico", 10, "calico")
# c.show()
# c.speak()

# d = Dog("Spot", 14)
# d.show()
# d.speak()

# f = Fish("Fishy", 8)
# f.show()
# f.speak()

###############################################################

# class Person:
# 	num_people = 0

# 	def __init__(self, name):
# 		self.name = name
# 		Person.add_person()

# 	@classmethod
# 	def num_people_func(cls):
# 		return cls.num_people

# 	@classmethod
# 	def add_person(cls):
# 		cls.num_people += 1


# p1 = Person("Dave")
# p2 = Person("Christy")
# p3 = Person("Abby")
# p4 = Person("Hannah")
# p5 = Person("Leah")

# print(Person.num_people_func())

###############################################################

# class Math:

# 	@staticmethod
# 	def add5(x):
# 		return x + 5

# 	@staticmethod
# 	def add10(x):
# 		return x + 10

# 	@staticmethod
# 	def pr():
# 		print("Hello World!")


# print(Math.add5(1))
# print(Math.add10(2))
# Math.pr()


###############################################################

# Python OOP Tutorial 1: Classes and Instances - YouTube

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

###############################################################

# import datetime

# class Employee:

# 	numEmployees = 0
# 	raiseAmount = 3.0
	
# 	def __init__(self, first, last, pay):
# 		self.first = first
# 		self.last = last
# 		self.pay = pay

# 		Employee.numEmployees += 1


# 	@property
# 	def email(self):
# 		firstLower = self.first.lower()
# 		lastLower = self.last.lower()
# 		return '{}.{}@ge.com'.format(firstLower, lastLower)


# 	@property
# 	def fullname(self):
# 		return '{} {}'.format(self.first, self.last)

	
# 	@fullname.setter
# 	def fullname(self, name):
# 		first, last = name.split(' ')
# 		self.first = first
# 		self.last = last


# 	@fullname.deleter
# 	def fullname(self):
# 		print("Deleting Name!")
# 		self.first = None
# 		self.last = None


# 	def applyRaise(self):
# 		multiplier = self.raiseAmount/100 + 1
# 		self.pay = int(self.pay * multiplier)

	
# 	def __repr__(self):
# 		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)


# 	def __str__(self):
# 		return "{}, {}, ${}.00".format(self.fullname, self.email, self.pay)

	
# 	@classmethod
# 	def setRaiseAmt(cls, amount):
# 		cls.raiseAmount = amount

	
# 	@classmethod
# 	def fromString(cls, empStr):
# 		first, last, pay = empStr.split(',')
# 		first = first.strip()
# 		last = last.strip()
# 		pay = pay.strip()
# 		return cls(first, last, pay)


# 	@staticmethod
# 	def isWorkday(day):
# 		if day.weekday() >= 5:	# if day.weekday() == 5 or day.weekday() == 6:
# 			return False
# 		return True


# class Developer(Employee):

# 	raiseAmount = 7.0

# 	def __init__(self , first, last, pay, favLanguage):
# 		super().__init__(first, last, pay)
# 		self.favLanguage = favLanguage


# class Manager(Employee):

# 	raiseAmount = 10.0

# 	def __init__(self, first, last, pay, employees=None):
# 		super().__init__(first, last, pay)
# 		if employees is None:
# 			self.employees = []
# 		else:
# 			self.employees = employees

	
# 	def addEmployee(self, emp):
# 		if emp not in self.employees:
# 			self.employees.append(emp)


# 	def removeEmployee(self, emp):
# 		if emp in self.employees:
# 			self.employees.remove(emp)


# 	def printEmployees(self):
# 		# print("Length:", len(self.employees))
# 		for emp in self.employees:
# 			print("-->", emp.fullname)



# # print("Number of employees:", Employee.numEmployees)

# emp1 = Employee("David", "Bauer", 75000)
# emp2 = Employee("Abigail", "Bauer", 125000)

# print(emp1.email)
# print(emp2.email)

# # print(emp1.fullname)	# same as Employee.fullname(emp1), may not work since adding @property for fullname
# # print(emp2.fullname)

# # Employee.setRaiseAmt(6.0)
# # emp1.setRaiseAmt(0.7)		# applies raise amount to the entire class

# # print(Employee.raiseAmount)
# # print(emp1.raiseAmount)
# # print(emp2.raiseAmount)

# # print(emp1.__dict__)
# # print(Employee.__dict__)

# emp3 = Employee.fromString("Hannah, Bauer, 150000")
# # print(emp3.pay)
# # print("Number of employees:", Employee.numEmployees)

# # myDate = datetime.date(2016, 7, 11)
# # print(Employee.isWorkday(myDate))

# mattsKids = [emp1, emp2]

# mgr1 = Manager("Mathew", "Sommers", 1000000, mattsKids)
# print(mgr1.email)
# mgr1.applyRaise()
# print(mgr1.pay)
# mgr1.printEmployees()
# print("Swapping out Abby for Hannah!")
# mgr1.addEmployee(emp3)
# mgr1.removeEmployee(emp2)
# mgr1.printEmployees()

# print("Number of employees:", Employee.numEmployees)

# # print(isinstance(mgr1, Developer))
# # print(isinstance(mgr1, Employee))
# # print(isinstance(mgr1, Manager))
# # print(issubclass(Developer, Manager))
# # print(issubclass(Manager, Employee))

# print(emp1)
# print(repr(emp1))

# print(emp1.fullname)

# emp1.fullname = "Heavy D"
# print(emp1.fullname)
# print(emp1.email)