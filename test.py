import time

counter = 0

for counter in range(2, 25, 2):
  print("Hello world!: " + str(counter))
  # time.sleep(0.1)


message = input("Please enter a string: ") # \n is stripped from input

if len(message) < 6:
  print("Your string is too short!")