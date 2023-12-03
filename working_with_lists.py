# Looping Through an Entire List
items = []
items.append('laptop')
items.append('mask')
items.append('book')
for item in items:
	print(str(item) + " is there on my table")
print('\n')

smartphones = []
smartphones.insert(0, 'huawei')
smartphones.insert(1, 'xiaomi')
smartphones.insert(2, 'samsung')
message = " is a very good smartphone"
for smartphone in smartphones:
	print(str(smartphone) + message)
print('\n')

# Doing More Work Within a for Loop
names = []
names.insert(0, 'komang')
names.insert(1, 'pramanta')
names.insert(2, 'gerinata')
message1 = " is studying Python programming language."
message2 = " will study JavaScript programming language."
for name in names:
	print(name.title() + message1)
	print("After that " + name.title() + message2 + '\n')

# Doing Something After a for Loop
singers = []
singers.insert(0, 'michael')
singers.insert(1, 'jackson')
appreciation = ", you sang wonderfully tonight!"
comment = "Please come again in the next party,"
ending = "Thank you."
for singer in singers:
	print(singer.title() + appreciation)
	print(comment + " " + singer.title() + ".\n")
print(ending)

# Avoiding Indentation Errors
# Forgetting to Indent
colors = []
colors.insert(0, 'golden')
colors.insert(1, 'blue')
colors.insert(2, 'red')
statement = "My favorite colors are "
for color in colors:
	print(statement + str(colors.pop(0)) + " and " + str(colors.pop(0) + " but I don't like " + str(colors.pop(0))) + ".\n")

# Forgetting to Indent Additional Lines
candidates = []
candidates.insert(0, 'tulsi gabbard')
candidates.insert(1, 'hillary clinton')
candidates.insert(2, 'donald trump')
for candidate in candidates:
	print(str(candidate).title() + " will attend the presidential debate.")
print("But will " + str(candidate).title() + " win this debate?" + "\n")

# Indenting Unnecessarily After the Loop
my_names = []
my_names.insert(0, 'komang')
my_names.insert(1, 'pramanta')
my_names.insert(2, 'gerinata')
for my_name in my_names:
	print(my_name.title() + " is writting a program.")
	print("The program that " + my_name.title() + " writes is written in Python.\n")

	print("Next " + my_name.title() + " will write a program in C++.\n") 

# Try It Yourself
# 4-1. Pizzas:
pizzas = []
pizzas.insert(0, 'vegetable pizza')
pizzas.insert(1, 'mozzarella pizza')
pizzas.insert(2, 'macaroni pizza')
opinion = "Pizza Hut has variety of pizzas, one of them is "
for pizza in pizzas:
	print(str(opinion) + pizza.title() + ".")

print("The first pizza that I ate is " + pizzas[0].title() + ".")
print("My favorite pizza is " + pizzas[1].title() + ".")
print(pizzas[1].title() + " is delicous because it full of mozzarella cheese.")
print("I really love pizza.\n")

# 4-2. Animals:
animals = []
animals.insert(0, 'cat')
animals.insert(1, 'dog')
animals.insert(2, 'pig')
opinion1 = " is a cute animal."
fact = "Any of these animals are four legged."
for animal in animals:
	print(animal.title() + opinion1)
	print(str(fact) + "\n")

# Making Numerical Lists
# Using the range() Function
for value in range(1,5):
	print(value)
print("\n")
for value in range(1,6):
	print(value)
print("\n")

# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(str(numbers) + "\n")

# Even & Odd Numbers
explanation = "This is even numbers: "
explanation1 = "This is odd numbers: "

even_numbers = list(range(2,11,2))
print(explanation + str(even_numbers) + "\n")

odd_numbers = list(range(1,11,2))
print(explanation1 + str(odd_numbers) + "\n")

# Squaring Numbers
print("Squaring Numbers")
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(str(squares) + "\n")

# Perpangkatan 2
print("Perpangkatan 5")
perpangkatan_5 = []
for nomer in range(1,6):
	pangkat_5 = nomer**5
	perpangkatan_5.append(pangkat_5)

print(str(perpangkatan_5) + "\n")

# Dollar to Rupiah
print("Dollar to Rupiah:")

dollar_to_rupiah_list = []
for dollar in range(1,11):
	dollar_value = dollar*14383
	dollar_to_rupiah_list.append(dollar_value)

moneys = dollar_to_rupiah_list
indonesian_currency = "Rp. "

for money in moneys:
	print(str(indonesian_currency) + str(money))
print("\n")

# Euro to Rupiah
print("Euro to Rupiah")

euro_to_rupiah_list = []
for value in range(1,11):
	euro_to_rupiah = value*16189
	euro_to_rupiah_list.append(euro_to_rupiah)

for rupiah in euro_to_rupiah_list:
	print(str(indonesian_currency) + str(euro_to_rupiah) + "\n")

# Test
squares = []
for value in range(1,11):
	squares.append(value**2)

print(str(squares) + "\n")

# Simple Statistics with a List of Numbers
digits = []
digits = list(range(1,11))

print(min(digits))
print(max(digits))
print(str(sum(digits)) + "\n")

# List Comprehensions
squares = [value**2 for value in range(1,11)]
print(str(squares) + "\n")

# Try It Yourself
# 4-3. Counting to Twenty:
values = list(range(1,21))
for value in values:
	print(values)
print("\n")

twenty_numbers = [list(range(1,21))]
for number in twenty_numbers:
	print(str(twenty_numbers) + "\n")

number_list = [number for number in range(1,21)]
print(str(number_list) + "\n")

# 4-4. One Million:
#one_million = [number for number in range(1,1000001)]
#print(str(one_million) + "\n")

# 4-5. Summing a Million:
#summing_a_million = [number for number in range(1,1000001)]
#print(min(summing_a_million))
#print(max(summing_a_million))

# 4-6. Odd Numbers:
odd_numbers = [number for number in range(1,21,2)]
print(str(odd_numbers) + "\n")

# 4-7. Threes:
threes = [number**3 for number in range(3,31)]
print(str(threes) + "\n")

# 4-8. Cubes:
cubes = []
for number in range(1,11):
	cube = number**3
	cubes.append(cube)

print(str(cubes) + "\n")

# 4-9. Cube Comprehension:
cube_comprehension = [number**3 for number in range(1,11)]
print(str(cube_comprehension) +"\n")

# Working with Part of a List
# Slicing a List
players = []
players.insert(0, 'rooney')
players.insert(1, 'bekham')
players.insert(2, 'gerrard')
players.insert(3, 'messi')
players.insert(4, 'ronaldo')
print("1. " + str(players[0:3]) + "\n")
print("2. " + str(players[1:4]) + "\n")
print("3. " + str(players[:4]) + "\n")
print("4. " + str(players[2:]) + "\n")
print("5. " + str(players[:-1]) + "\n")
print("6. " + str(players[-2:]) + "\n")
print("7. " + str(players[-4:]) + "\n")
print("8. " + str(players[:-4]) + "\n")

# Looping Through a Slice
his_names = []
his_names.insert(0, 'sir')
his_names.insert(1, 'james')
his_names.insert(2, 'paul')
his_names.insert(3, 'mccartney')
print("Here is my full name:")
for his_name in his_names[:4]:
	print(his_name.title())
print("\n")

say = [print(his_name.title()) for his_name in his_names[:4]]
print("\n")

say1 = [his_name.title() for his_name in his_names]
print(str(say1) + "\n")

full_name = []
full_name.insert(0, 'komang')
full_name.insert(1, 'pramanta')
full_name.insert(2, 'gerinata')
full_name = [character.title() for character in full_name[0:4]]
print(str(full_name) + "\n")

jj_names = []
jj_names.insert(0, 'john')
jj_names.insert(1, 'joseph')
jj_names.insert(2, 'mcgowan')
for jj_name in jj_names:
	print(str(jj_names[0]) + " is his first name.")
	print(str(jj_names[1]) + " is his middle name.")
	print(str(jj_names[2]) + " is his last name.")
print("\n")

# Copying a List
my_foods = []
my_foods.insert(0, 'nasi goreng')
my_foods.insert(1, 'mie kuah')
my_foods.insert(2, 'mie goreng')
my_foods = [my_food.title()for my_food in my_foods]
friends_foods = my_foods[:]
my_foods.append('nasi campur')
friends_foods.append('ramen')

print("These are my favorite foods:")
print(my_foods)

print("These are my friend's favorite foods:")
print(friends_foods)

my_colors = []
my_colors.insert(0, 'blue')
my_colors.insert(1, 'red')
my_colors.insert(2, 'yellow')
my_colors = [my_color.title()for my_color in my_colors]
his_colors = my_colors[:]
my_colors.append('golden')
his_colors.append('black')

print(my_colors)
print(his_colors)
print("\n")

# Without Using Slice ([:])
my_cars = ['buggatti', 'lamborghini', 'ferrari']
her_cars = my_cars
my_cars.append('corvette')
her_cars.append('lotus')
print("My favorite cars are:")
print(my_cars)
print("\nHer favorite cars are:")
print(str(her_cars) + "\n")

# Try It Yourself
# 4-10. Slices:
asians = []
asians.insert(0, 'indonesia')
asians.insert(1, 'malaysia')
asians.insert(2, 'singapore')
asians = [asian.title()for asian in asians]
se_asians = asians[:]
asians.append('japan')
se_asians.append('thailand')
asians = [asian.title()for asian in asians]
se_asians = [se_asian.title()for se_asian in se_asians]

print("The first three items in the lists are:")
print(asians[0:3])
print(str(se_asians[0:3]) + "\n")

# 4-11. My Pizzas, Your Pizzas:
my_pizzas = []
my_pizzas.insert(0, 'mozzarella pizza')
my_pizzas.insert(1, 'vegetable pizza')
my_pizzas.insert(2, 'macaroni pizza')
my_pizzas = [my_pizza.title()for my_pizza in my_pizzas]
print(my_pizzas)
for my_pizza in my_pizzas:
	print("I like " + my_pizza + ".\n")
print("I like pizza with vegetable toppings.\nI like my pizza full of mozzarella cheese.\nAnd I like when they put macaroni topping on my pizza.\nI really love pizzas!\n")

friends_pizzas = my_pizzas[:]
my_pizzas.append('parmesan cheese pizza')
friends_pizzas.append('sausage pizza')

for my_pizza in my_pizzas:
	print("My favorite pizzas are: " + str(my_pizzas))
for friends_pizza in friends_pizzas:
	print("My friend's favorite pizzas are: " + str(friends_pizzas))

foods = []
foods.insert(0, 'pizza')
foods.insert(1, 'falafel')
foods.insert(2, 'carrot cake')
her_foods = foods[:]
foods.append('cannoli')
her_foods.append('ice cream')
for food in foods:
	print(food)
for her_food in her_foods:
	print(her_food)
print("\n")

# Tuples
# Defining a Tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

lucky_numbers = (range(1,6))
print(str(list(lucky_numbers)) + "\n")

# Writing over a Tuple
dimensions = (200, 50)
print("Original Dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("Modified Dimensions")
for dimension in dimensions:
	print(dimension)

print(str(dimensions) + "\n")

# Try It Yourself
# 4-13. Buffet:

simple_foods = ('nasi goreng', 'mie goreng', 'cap cay', 'bakso', 'lawar')
for simple_food in simple_foods:
	print(simple_food)
print("\n")
simple_foods = ('nasi goreng', 'mie goreng', 'cap cay', 'mie ayam', 'soto')
for simple_food in simple_foods:
	print(simple_food)
print("\n")

# Try It Yourself
# 4-15. Code Review:

simple_foods = ('nasi goreng', 'mie goreng', 'cap cay', 'bakso', 'lawar')
for simple_food in simple_foods:
    print(simple_food)
print("\n")
simple_foods = ('nasi goreng', 'mie goreng', 'cap cay', 'mie ayam', 'soto')
for simple_food in simple_foods:
    print(simple_food)
print("\n")


