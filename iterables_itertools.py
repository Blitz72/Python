###############################################################

# Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?

# https://www.youtube.com/watch?v=jTYiNjvnHZY

###############################################################

# nums = [1, 2, 3]

# i_nums = nums.__iter__()
# i_nums = iter(nums)	# same as prvioius line

# for num in nums:
# 	print(num)

# print(dir(nums))

# print(dir(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# while True:
# 	try:
# 		item = next(i_nums)
# 		print(item)
# 	except StopIteration:
# 		break

# class MyRange:

# 	def __init__(self, start, stop):
# 		self.value = start
# 		self.stop = stop


# 	def __iter__(self):
# 		return self


# 	def __next__(self):
# 		if self.value >= self.stop:
# 			raise StopIteration
# 		current = self.value
# 		self.value += 1
# 		return current


# def my_range_generator(start, stop):
# 	current = start
# 	while current < stop:
# 		yield current
# 		current += 1


# nums = MyRange(1, 10)

# for num in nums:
# 	print(num)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# nums_generator = my_range_generator(1, 10)

# for num in nums_generator:
# 	print(num)

# print(dir(nums_generator))

# print(next(nums_generator))

# class Sentence:

# 	def __init__(self, sentence):
# 		self.sentence = sentence
# 		self.words = self.sentence.split(' ')
# 		self.index = 0
# 		print(self.words)
# 		self.end = len(self.words)


# 	def __iter__(self):
# 		return self


# 	def __next__(self):
# 		if self.index >= self.end:
# 			raise StopIteration
# 		currentIndex = self.index
# 		self.index += 1
# 		return self.words[currentIndex]


# def sentence_generator(sentence):
# 	words = sentence.split(' ')
# 	currentIndex = 0
# 	while currentIndex < len(words):
# 		yield words[currentIndex]
# 		currentIndex += 1


# def sentence_generator(sentence):
# 	for word in sentence.split():
# 		yield word


# my_sentence = Sentence("This is a test.")
# my_sentence_generator = sentence_generator("Dude, seriously this is just a test!")

# for word in my_sentence:
# 	print(word)

# print(next(my_sentence))

# for word in my_sentence_generator:
# 	print(word)

# print(next(my_sentence_generator))
# print(next(my_sentence_generator))
# print(next(my_sentence_generator))
# print(next(my_sentence_generator))


###############################################################

# Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping

# https://www.youtube.com/watch?v=Qu3dThVy6KQ

###############################################################


# import itertools
# import operator

# counter = itertools.count() # this will count CONTINUOUSLY, do not pair with a for num in counter: print(num) statement
# counter = itertools.count(start = 5, step = 5)
# my_data = [100, 200, 300, 400, 500, 600]

# counter2 = itertools.count(start = 5, step = -2.5)

# # print(next(counter))    # printing next(counter) will keep counter from looping forever
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))

# counted_data = zip(itertools.count(), my_data)

# print(dict(counted_data))

# # counted_data = zip(counter, my_data)
# counted_data = zip(counter2, my_data)

# print(dict(counted_data))

# long_counted_data = dict(itertools.zip_longest(range(12), my_data))

# print(long_counted_data)

# counter3 = itertools.cycle([1, 2, 3])
# counter3 = itertools.cycle(["ON", "OFF"])
# counter3 = itertools.repeat(1972, 10)
# counter3 = itertools.repeat(1972, times = 10)

# print(next(counter3))
# print(next(counter3))
# print(next(counter3))
# print(next(counter3))

# for num in counter3:
#     print(num)

# squares = map(pow, range(10), itertools.repeat(2))  # need to use the itertools.repeat(2), just an int 2 will not work
# squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)])

# print(list(squares))

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# names = ["David", "Greg", "Katie", "Timothy", "Joan"]
# selectors = [True, True, False, True, False, True]

# people = [
#     {
#         "name": "David",
#         "city": "Concord Township",
#         "state": "Ohio",
#         "stateAbbr": "OH"
#     },
#     {
#         "name": "Christy",
#         "city": "Concord Township",
#         "state": "Ohio",
#         "stateAbbr": "OH"
#     },
#     {
#         "name": "Abigail",
#         "city": "Concord Township",
#         "state": "Ohio",
#         "stateAbbr": "OH"
#     },
#     {
#         "name": "Hannah",
#         "city": "Concord Township",
#         "state": "Ohio",
#         "stateAbbr": "OH"
#     },
#     {
#         "name": "Leah",
#         "city": "Concord Township",
#         "state": "Ohio",
#         "stateAbbr": "OH"
#     },
#     {
#         "name": "Dudester",
#         "city": "Cambridge",
#         "state": "Massachussets",
#         "stateAbbr": "MA"
#     },
#     {
#         "name": "Dude.com",
#         "city": "Columbus",
#         "state": "Ohio",
#         "stateAbbr": "OH"
#     },
#     {
#         "name": "Dudemeister",
#         "city": "Boston",
#         "state": "Massachussets",
#         "stateAbbr": "MA"
#     }
# ]

# result = itertools.combinations(letters, 2)
# result2 = itertools.permutations(letters, 2)
# result3 = itertools.product(numbers, repeat=3)
# result3 = itertools.combinations_with_replacement(numbers, 3) # same as previous line

# for item in result:
#     print(item)

# print()

# for item in result2:
#     print(item)

# print()

# for item in result3:
#     print(item)

# combined = itertools.chain(letters, numbers, names)
# combined2 = itertools.islice(range(10), 1, 8, 2)    # (iterable, start, end, step)

# for item in combined:
#     print(item)

# for item in combined2:
#     print(item)

# result = itertools.compress(letters, selectors)
# result2 = itertools.accumulate(numbers)
# result3 = itertools.accumulate(itertools.islice(numbers, 1, len(numbers)), operator.mul)

# for item in result:
#     print(item)

# for item in result2:
#     print(item)

# for item in result3:
#     print(item)

# def get_state(person):
#     return person['stateAbbr']


# def sort_function(person):
#     return person['stateAbbr']


# person_group = itertools.groupby(people, get_state)

# for key, group in person_group:
#     print(key)
#     for person in group:
#         print(person)

# print()
# people.sort(key=sort_function)
# person_group = itertools.groupby(people, get_state)

# for key, group in person_group:
#     print(key)
#     for person in group:
#         print(person)