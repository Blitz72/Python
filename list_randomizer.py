#!/usr/bin/python3

# Rnadomize multiple successive lists so that the first value of the next list 
# is different from the last value of the preceding list.

import random

# Standard values for Cync Voice agent Automated Testing
# constants = (0, 5, 15, 70, 100)

constants = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)

# Python already has a great list randomizer!
my_list = [10, 20, 30, 40, 50]
random.shuffle(my_list)
print(my_list)

# print(random.seed(a=bytes('dave is cooler!', 'utf-8'), version=2))
def randomize():
    seeds = []
    for value in constants:
        seeds.append(value)
    random_list = []
    for x in range(len(constants)):
        chosen = seeds[random.randint(0, len(seeds)-1)]
        seeds.remove(chosen)
        random_list.append(chosen)
        # print(seeds)
    return random_list

if __name__ == "__main__":
    previous_list = randomize()
    for x in range(3):
        randomized_list = randomize()
        while previous_list[-1] == randomized_list[0] or randomized_list[-1] == 0:
            randomized_list[0], randomized_list[-1] = randomized_list[-1], randomized_list[0]
            print("re-randomizing")  # sometimes it re-randomizes
        previous_list = randomized_list
        print('randomized_list =', randomized_list)
