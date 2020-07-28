numbers = [5, 2, 5, 2, 2]

for number in numbers:
  # print(number)
  for x in range(number):
    print('x', end = '')
  print()

matrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30]
]

# print(len(matrix))
# print(len(matrix[0]))

for y in range(len(matrix)):
  for x in range(len(matrix[y])):
    # if x < len(matrix[0]) - 1:
    #   endDelimiter = ', '
    # else:
    #   endDelimiter = ''
    print(matrix[y][x], end = ', ' if x < len(matrix[y]) - 1 else '')
  print()
