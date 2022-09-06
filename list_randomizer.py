import random

# seeds = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# randomized_list = []

# length = len(seeds)
# for x in range(length):
#     chosen = seeds[random.randint(0, len(seeds)-1)]
#     seeds.remove(chosen)
#     randomized_list.append(chosen)
#     # print(seeds)
# print(randomized_list)

# constants = (0, 5, 15, 70, 100)
constants = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

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


previous_list = randomize()
for x in range(3):
    current = 0
    randomized_list = randomize()
    while previous_list[-1] == randomized_list[0]:
        randomized_list = randomize()
    previous_list = randomized_list
    print('randomized_list =', randomized_list)