# fruits = ["apple", "banana", "cherry", "strawberry"]

# for x in fruits:
#   print(x)

# fruits.append("blueberry")

# for x in fruits:
#   print(x)

# # print(2019 - int("1972"))

# x = ((10 + 3) * 2) ** 2
# print(x)

jedi = [{
  'name': 'Anakin Skywalker',
  'lightsaber': 'green',
  'isSith': True
},
{
  'name': 'Obi Wan Kenobi',
  'lightsaber': 'blue',
  'isSith': False
},
{
  'name': 'Luke Skywalker',
  'lightsaber': 'green',
  'isSith': False
},
{
  'name': 'Yoda',
  'lightsaber': 'green',
  'isSith': False
}]

# for index in range(len(jedi)):
#   for key in jedi[index]:
#     print(jedi[index][key])

firstName = ''
master = ''
saberColor = ''
indexer = 0
isFound = False

nameInput = input("What is your name, young Jedi? ")

for index in range(len(jedi)):
  # for key in jedi[index]:
    # print(index)
    # print(key)
#   print(jedi[index]['name'])

  if nameInput == jedi[index]['name']:
    indexer = index
    isFound = True
    firstName = nameInput.split(" ")[0]

if isFound:
  if jedi[indexer]['isSith']:
    master = "Emperor Palpatine"
    saberColor = 'red'
  else:
    master = "Master Yoda"
    saberColor = 'green'

  jedi[indexer].update({'master': master})
  jedi[indexer].update({'lightsaber': saberColor})

  msg = f"Hi, {firstName}! What would you like {master} to call you? "
  prefName = input(msg)
  jedi[indexer].update({'prefName': prefName})
  masterLastName = master.split(" ")[1]
  msg = f"Ok, {firstName}, from now on {masterLastName} will call you \"{prefName}.\"\nMay the force be with you!"
  
  print()
  print(msg)
  print()
  print(jedi)

else:
  print()
  print(f"The Jedi Council does not seem to have anyone registered under the name \"{nameInput}.\"")
