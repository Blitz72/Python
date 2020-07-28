###############################################################

# 10 Python Tips and Tricks For Writing Better Code

# https://www.youtube.com/watch?v=C-gEQdGVXbk

###############################################################

# condition = True
# num1 = 10_000_000_000
# num2 = 100_000_000

# if condition:
#     x = 1
# else:
#     x = 0

# Python style ternary conditional
# x = 1 if condition else 0

# print(x)

# total = num1 + num2

# print(total)
# print(f'{total:,}')

# f = open('test.txt', 'r')

# file_contents = f.read()

# f.close()

# words = file_contents.split()
# word_count = len(words)
# print(word_count)


# use a context manager instead when managing resources (file opening, database connections, threads, etc.)
# with open('test.txt', 'r') as f:
#     file_contents = f.read()

# words = file_contents.split()
# word_count = len(words)
# print(word_count)


# index = 0
# names = ["David", "Christy", "Abigail", "Hannah", "Leah", "Greg", "Katie", "Timothy", "Joan"]

# for name in names:
#     print(index, name)
#     index += 1


# can use enumerate() to keep track of index
# for index, name in enumerate(names, start=1):   # or enumerate(names) to start at 0
#     print(index, name)


# names_reg = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
# names_hero = ["Spiderman", "Superman", "Deadpool", "Batman"]
# universes = ["Marvel", "DC", "Marvel", "DC"]

# for index, name in enumerate(names_reg):
#     hero = names_hero[index]
#     print(f"{hero} is actually {name}.")


# USE zip INSTEAD
# for name, hero, universe in zip(names_reg, names_hero, universes):
#     print(f"{hero} is actually {name} from {universe} Comics.")


# a, b = (1, 2)

# if you don't need to use one of the unpacked variables use this:
# a, _ = (1, 2)

# print(a)
# print(b)

# a, b, *c, d = (1, 2, 3, 4, 5, 6, 7, 8)
# print(a)
# print(b)
# print(c)
# print(d)

# a, b, *_, d = (1, 2, 3, 4, 5, 6, 7, 8)

# print(a)
# print(b)
# # print(c)
# print(d)


# class Person():
#     pass


# person = Person()
# person.first = "David"
# person.last = "Bauer"

# USE THIS INSTEAD:
# setattr(person, "first", "David")
# setattr(person, "last", "Bauer")

# first = getattr(person, "first")
# last = getattr(person, "last")
# print(first, last)

# print(person.first, person.last)


# person_info = {"first": "David", "last": "Bauer"}

# for key, value in person_info.items():
#     setattr(person, key, value)

# for key in person_info.keys():
#     print(getattr(person, key))


# username = input("Username: ")
# password = input("Password: ")  # text prints out the password being typed in!!!

# print("Logging in...")

# from getpass import getpass

# username = input("Username: ")
# password = getpass("Password: ")  # text prints out the password being typed in!!!

# print("Logging in...")
# print(password) # Oh no, Davey printed the "password"!!!


# import datetime
# help(datetime)  # Dude, there's a lot of help here!
