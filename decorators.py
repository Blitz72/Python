###############################################################

# Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions

# https://www.youtube.com/watch?v=FsAPt_9Bf3U

###############################################################

# outerFunction()

# def square(x):
# 	return x * x

# def myMap(func, argList):
# 	result = []
# 	for i in argList:
# 		result.append(func(i))
# 	return result

# squares = myMap(square, [1, 3, 5, 7, 9])

# print(squares)


# def outerFunction(msg):
# 	# message = msg

# 	def innerFunction():
# 		print(msg)		# print(message)
	
# 	return innerFunction


# hiFunction = outerFunction("Wassup!")
# goodDayFunction = outerFunction("Good Day, Sir!")
# hiFunction()
# goodDayFunction()


# def decoratorFunction(originalFunction):
# 	def wrapperFunction(*args, **kwargs):
# 		print("this executed before {}".format(originalFunction.__name__))
# 		return originalFunction(*args, **kwargs)
# 	return wrapperFunction


# @decoratorFunction
# def display():
# 	print("Ran display function")


# @decoratorFunction
# def displayInfo(name, age):
# 	print("displayInfo ran with arguments: '{}', '{}'".format(name, age))

###############################################################

# class decoratorClass(object):
# 	def __init__(self, originalFunction):
# 		self.originalFunction = originalFunction


# 	def __call__(self, *args, **kwargs):
# 		print("call method executed before {}".format(self.originalFunction.__name__))
# 		return self.originalFunction(*args, **kwargs)


# @decoratorClass
# def display():
# 	print("Ran display function")


# @decoratorClass
# def displayInfo(name, age):
# 	print("displayInfo ran with arguments: '{}', '{}'".format(name, age))

# decoratedDisplay = decoratorFunction(display)
# decoratedDisplay()


# displayInfo("David", 47)
# display()

###############################################################

# from functools import wraps


# def myLogger(originalFunction):
# 	import logging
# 	logging.basicConfig(filename='{}.log'.format(originalFunction.__name__), level = logging.INFO)

# 	@wraps(originalFunction)
# 	def wrapper(*args, **kwargs):
# 		logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
# 		return originalFunction(*args, **kwargs)


# 	return wrapper


# def myTimer(originalFunction):

# 	@wraps(originalFunction)
# 	def wrapper(*args, **kwargs):
# 		t1 = time.time()
# 		result = originalFunction(*args, **kwargs)
# 		t2 = time.time() - t1
# 		print("{} ran in: {} seconds".format(originalFunction.__name__, t2))
# 		return result

	
# 	return wrapper


# @myLogger
# @myTimer
# def displayInfo(name, age):
# 	time.sleep(0.5)
# 	print("displayInfo ran with arguments: {}, {}".format(name, age))


# import time

# displayInfo("David", 47)
# displayInfo("Dude.com", 75)