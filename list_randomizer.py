import random

seeds = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
randomized_list = []

length = len(seeds)
for x in range(length):
    chosen = seeds[random.randint(0, len(seeds)-1)]
    seeds.remove(chosen)
    randomized_list.append(chosen)
    # print(seeds)
print(randomized_list)