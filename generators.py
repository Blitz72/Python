###############################################################

# Python Tutorial: Generators - How to use them and the benefits you receive

# https://www.youtube.com/watch?v=bD05uGo_sVI

###############################################################


# def square_nums(nums):
# 	for num in nums:
# 		yield(num * num)


# my_nums = square_nums([1, 2, 3, 4, 5])

# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))

# for num in my_nums:
# 	print(num)

# my_nums = [x*x for x in [1, 2, 3, 4, 5]]	# list comprehension
# my_nums = (x*x for x in [1, 2, 3, 4, 5])	# generator

# print(my_nums)
# print(list(my_nums))	# convert generator to list to print but lose performance

# import memory_profiler
# import random
# import time

# names = ["Dave", "Brian", "Rich", "Mark", "Matt", "Tom", "Greg", "Bob", "Steve", "George", "Frank"]
# majors = ["Math", "Engineering", "Computer Science", "Arts", "Business", "Frolicking"]


# # @profile	used with memory_profiler, when running code use "-m memory_profiler"
# def people_list(num_people):
# 	result = []
# 	for i in range(num_people):
# 		person = {
# 			"id": i,
# 			"name": random.choice(names),
# 			"major": random.choice(majors)
# 		}
# 		result.append(person)
# 	return result


# # @profile	used with memory_profiler, when running code use "-m memory_profiler"
# def people_generator(num_people):
# 	for i in range(num_people):
# 		person = {
# 			"id": i,
# 			"name": random.choice(names),
# 			"major": random.choice(majors)
# 		}
# 	yield person

# t1 = time.time()
# people = people_list(1000000)
# t2 = time.time()

# # t1 = time.time()
# # people = people_generator(1000000)
# # t2 = time.time()

# print("Completed in {} seconds".format(t2 - t1))

###############################################################

# Generators in Python || Python Tutorial || Learn Python Programming
# Socratica

# https://www.youtube.com/watch?v=gMompY5MyPg

###############################################################

# import string

# def letters():
#     for c in string.ascii_lowercase:
#         yield c
#     for c_upper in string.ascii_uppercase:
#         yield c_upper

# for letter in letters():
#     print(letter)

import itertools


def prime_numbers():
    yield 2
    prime_cache = [2]

    for n in itertools.count(3, 2):
        is_prime = True
        print('n =', n)

        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break

        if is_prime:
            prime_cache.append(n)
            yield n
        print('prime_cache =', prime_cache)


for p in prime_numbers():
    print('p =', p)
    if p > 30:
        break
