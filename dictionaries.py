# A Simple Dictionary
print("A Simple Dictionary\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Working with Dictionaries
# A dictionary in Python is a collection of key-value pairs. Each key is 
# connected to a value, and you can use a key to access the value associated 
# with that key. A key’s value can be a number, a string, a list, or even 
# another dictionary. In fact, you can use any object that you can create in 
# Python as a value in a dictionary.

# Accessing Values in a Dictionary
print("Accessing Values in a Dictionary\n")

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!\n")

my_laptop = {'brand': 'ASUS', 'price': 15000000}
print("My " + my_laptop['brand'] + " costs for about Rp. " + str(my_laptop['price']) + "\n")

# Adding New Key-Value Pairs
print("Adding New Key-Value Pairs")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

my_laptop = {'brand': 'ASUS', 'price': 15000000}
my_laptop['version'] = 'ZenBook 14'
print(my_laptop)

# Starting with an Empty Dictionary
print("\nStarting with an Empty Dictionary")

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Modifying Values in a Dictionary
print("\nModifying Values in a Dictionary")

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".\n")

my_laptop = {'brand': 'ASUS', 'version': 'ZenBook', 'price': 15000000}
print("I have " + my_laptop['brand'] + " " + my_laptop['version'] + ". I bought it at Rp." + str(my_laptop['price']))

my_laptop['brand'] = 'Apple'
my_laptop['version'] = 'MacBook'
my_laptop['price'] = 25000000
print("I have " + my_laptop['brand'] + " " + my_laptop['version'] + ". I bought it at Rp. " + str(my_laptop['price']) + ".\n")

# More Interesting Examples:
print("More Interesting Examples:")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
print("Original x_position: " + str(alien_0['x_position']))

# Move Alien to the Right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3

# This new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x_position: " + str(alien_0['x_position']))

# Removing Key-Value Pairs
print("Removing Key-Value Pairs\n")

alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
print(alien_0)

del alien_0['points'], alien_0['speed']
print(alien_0)

# Practice
print("\nPractice 1\n")

entries = ['VENOM MARVEL']
entries = [entry.lower() for entry in entries]

venom1 = {}
venom1['keyword'] = ['venom', 'venom marvel']
venom1['name'] = 'Venom (Marvel Character)'
venom1['definition'] = ("Venom is a fictional character appearing in American comic books published by Marvel Comics."
"The character is a sentient alien symbiote with an amorphous, liquid-like form, who survives by bonding with a host,"
"usually human. This dual-life form receives enhanced powers and usually refers to itself as 'Venom'.")

venom2 = {}
venom2['keyword'] = ['venom', 'venom poison']
venom2['name'] = 'Venom (Poisonous Substance)'
venom2['definition'] = ("A poisonous substance secreted by animals such as snakes, spiders, and scorpions "
"and typically injected into prey or aggressors by biting or stinging.")

for entry in entries:
	if entry in venom1['keyword']:
		print(venom1['name'])
		print(venom1['definition'])
	elif entry in venom2['keyword']:
		print(venom2['name'])
		print(venom2['definition'])
	else:
		print("Entry not found.")

print("\nPractice 2\n")

laptop_searches = ['apple']
laptop_searches = [laptop_search.lower() for laptop_search in laptop_searches]

apple = {}
apple['keyword'] = ['apple', 'macbook']
apple['brand'] = 'Apple'
apple['version'] = 'MacBook'
apple['description'] = (
"\n13-inch MacBook Pro with Touch Bar (Space Grey)"
"\n1.4 GHz quad-core 8th gen Intel core i5"
"\nIntel Iris Plus Graphics 645"
"\n16 GB 2133MHz LPDDR3" 
"\n256 GB SSD"
"\nRetina display with True Tone"
"\nTwo Thunderbolt 3 ports"
"\nTouch Bar & Touch ID"
"\nBacklit Magic Keyboard - US English"
"\nAccessory Kit")
apple['price'] = 25000000

asus = {}
asus['keyword'] = ['asus', 'zenbook']
asus['brand'] = 'ASUS'
asus['version'] = 'ZenBook'
asus['description'] = (
"\nProcessor: Intel Core i7-1165G7 1.2-2.8 GHz (12M Cache, up to 4.7 GHz)" 
"\nRAM: 16GB LPDDR4X"
"\nStorage: 1TB PCIe NVMe SSD"
"\nWeight: 2.49 lbs (1.13 kg)"
"\nDimensions: 12.56 x 8.19 x 0.55 inches (319 x 208 x 13.9 mm)"
"\nBattery: 67Wh"
"\nDisplay: 14-inch 1920 x 1080 IPS level display"
"\nCamera: HD infrared camera"
"\nWi-Fi: Wi-Fi 6")
asus['price'] = 15000000

for laptop_searches in laptop_searches:
	if laptop_searches in apple['keyword']:
		print(apple['brand'] + " " + apple['version'])
		print(apple['description'])
		print("\nPrice: Rp. " + str(apple['price']))
	if laptop_searches in asus['keyword']:
		print(asus['brand'] + " " + asus['version'])
		print(asus['description'])
		print("\nPrice: Rp. " + str(asus['price']))

# Practice 3
print("\nPractice 3\nSmartphones:")

smartphone_keywords = ['mi']
smartphone_keywords = [smartphone_keyword.lower() for smartphone_keyword in smartphone_keywords]

samsung = {}
samsung['keyword'] = ['samsung', 'galaxy', 's21', 'ultra']
samsung['brand'] = '\nSamsung'
samsung['version'] = 'Galaxy S21 ultra'
samsung['specifications'] = (
	"\nRelease date: January 2021"
	"\nWeight: 227 g"
	"\nDimensions: 165.1 x 75.6 x 8.9 mm"
	"\nOS: Android 11"
	"\nScreen size: 6.8-inch"
	"\nResolution: 1440 x 3200"
	"\nCPU: Snapdragon 888 / Exynos 2100"
	"\nRAM: 12GB / 16 GB"
	"\nStorage: 128 GB/256 GB/512 GB"
	"\nBattery: 5,000 mAh"
	"\nRear camera: 108MP + 10MP + 10MP + 12MP"
	"\nFront camera: 40MP")
samsung['price'] = 12115000

apple = {}
apple['keyword'] = ['apple', 'iphone', '13', 'pro', 'max']
apple['brand'] = '\nApple'
apple['version'] = 'iPhone 13 Pro Max'
apple['specifications'] = (
	"\nWeight: 240 g"
	"\nDimensions: 160.8 x 78.1 x 7.7 mm"
	"\nOS: iOS 15"
	"\nScreen size: 6.7-inch"
	"\nResolution: 1284 x 2778"
	"\nCPU: A15 Bionic"
	"\nRAM: 6 GB"
	"\nStorage: 128 GB/256 GB/512 GB/1 TB"
	"\nBattery: Up to 28 hours"
	"\nRear camera: 12 MP + 12 MP + 12 MP"
	"\nFront camera: 12 MP")
apple['price'] = 18000000

huawei = {}
huawei['keyword'] = ['huawei', 'p30', 'pro']
huawei['brand'] = '\nHuawei'
huawei['version'] = 'P30 Pro'
huawei['specifications'] = (
	"\nRelease date: March 2019"
	"\nWeight: 192 g"
	"\nDimensions: 158 x 73.4 x 8.4 mm"
	"\nOS: Android 9"
	"\nScreen size: 6.47-inch"
	"\nCPU: Kirin 980"
	"\nRAM: 8 GB"
	"\nStorage: 128/256/512 GB"
	"\nBattery: 4,200 mAh"
	"\nRear camera: 40 MP + 20 MP + 8 MP + ToF"
	"\nFront camera: 32MP")
huawei['price'] = 8399000

xiaomi = {}
xiaomi['keyword'] = ['xiaomi', 'mi', '11']
xiaomi['brand'] = '\nXiaomi'
xiaomi['version'] = 'Mi 11'
xiaomi['specifications'] = (
	"\nRelease date: March 2021"
	"\nWeight: 196 g"
	"\nDimensions: 164.3 x 74.6 x 8.6 mm"
	"\nOS: Android 11"
	"\nScreen size: 6.8-inch"
	"\nResolution: 1440 x 3200"
	"\nCPU: Snapdragon 888"
	"\nRAM: 8 GB"
	"\nStorage: 128 GB/256 GB"
	"\nBattery: 4,600mAh"
	"\nRear camera: 108 MP + 13 MP + 5 MP"
	"\nFront camera: 20 MP")
xiaomi['price'] = 5649000

google = {}
google['keyword'] = ['google', 'pixel', '6', 'pro']
google['brand'] = '\nGoogle'
google['version'] = 'Pixel 6 Pro'
google['specifications'] = (
	"\nRelease date: October 2021"
	"\nWeight: 210 g"
	"\nDimensions: 163.9 x 75.9 x 8.9 mm"
	"\nOS: Android 12"
	"\nScreen size: 6.71-inch"
	"\nResolution: 1440 x 3120"
	"\nCPU: Google Tensor"
	"\nRAM: 12 GB"
	"\nStorage: 128 GB/256 GB/512 GB"
	"\nBattery: 5,003 mAh"
	"\nRear camera: 50 MP + 48 MP + 12 MP"
	"\nFront camera: 11.1MP")
google['price'] = 13499000

for smartphone_keyword in smartphone_keywords:
	if smartphone_keyword in samsung['keyword']:
		print(samsung['brand'] + " " + samsung['version'])
		print(samsung['specifications'])
		print("Price: Rp. " + str(samsung['price']))
	if smartphone_keyword in apple['keyword']:
		print(apple['brand'] + " " + apple['version'])
		print(apple['specifications'])
		print("Price: Rp. " + str(apple['price']))
	if smartphone_keyword in huawei['keyword']:
		print(huawei['brand'] + " " + huawei['version'])
		print(huawei['specifications'])
		print("Price: Rp. " + str(huawei['price']))
	if smartphone_keyword in xiaomi['keyword']:
		print(xiaomi['brand'] + " " + xiaomi['version'])
		print(xiaomi['specifications'])
		print("Price: Rp. " + str(xiaomi['price']))
	if smartphone_keyword in google['keyword']:
		print(google['brand'] + " " + google['version'])
		print(google['specifications'])
		print("\nPrice: Rp. " + str(google['price']))

# A Dictionary of Similar Objects
print("\nA Dictionary of Similar Objects\n")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + 
	".\n")

# Practice
print("Practice\n")

android_keywords = ['pro']
android_keywords = [android_keyword.lower() for android_keyword in android_keywords]

smartphones = {
	'oneplus_keywords': ['oneplus', '9', 'pro'], 
	'oneplus_brand': 'OnePlus 9 Pro', 
	'oneplus_review': 'The best Android phone for ultra-wide shots.', 
	'oneplus_price': [650],

	'oppo_keywords': ['oppo', 'find', 'x3', 'pro'], 
	'oppo_brand': 'Oppo Find X3 Pro', 
	'oppo_review': 'The best Android phone for macro photography.',
	'oppo_price': [797], 

	'realme_keywords': ['realme', 'gt'], 
	'realme_brand': 'Realme GT', 
	'realme_review': 'The best relatively cheap Android phone.',
	'realme_price': [370]
}

for android_keyword in android_keywords:
	if android_keyword in smartphones['oneplus_keywords']:
		print(smartphones['oneplus_brand'] + str("\n" + smartphones['oneplus_review']))
		rupiahs = []
		for price in smartphones['oneplus_price']:
			rupiah = price * 14382
			rupiahs.append(rupiah)
		converted_rupiah = rupiahs[0]
		print("Price: Rp. " + str(converted_rupiah) + "\n")
	if android_keyword in smartphones['oppo_keywords']:
		print(smartphones['oppo_brand'] + str("\n" + smartphones['oppo_review']))
		rupiahs = []
		for price in smartphones['oppo_price']:
			rupiah = price * 14382
			rupiahs.append(rupiah)
		converted_rupiah = rupiahs[0]
		print("Price: Rp. " + str(converted_rupiah) + "\n")
	if android_keyword in smartphones['realme_keywords']:
		print(smartphones['realme_brand'] + str("\n" + smartphones['realme_review']))
		rupiahs = []
		for price in smartphones['realme_price']:
			rupiah = price * 14382
			rupiahs.append(rupiah)
		converted_rupiah = rupiahs[0]
		print("Price: Rp. " + str(converted_rupiah) + "\n")

# Try It Yourself
print("Try It Yourself\n")
print("6-1. Person:\n")

paul = {
	'first_name': 'paul',
	'middle_name': 'james',
	'last_name': 'mccartney',
	'age': 79,
	'city': 'london'
}

print("First name: " + str(paul['first_name'].title()) + "\n" +
	"Middle name: " + str(paul['middle_name'].title()) + "\n"+
	"Last name: " + str(paul['last_name'].title()) + "\n" +
	"Age: " + str(paul['age']) + "\n" +
	"City: " + str(paul['city'].title()) + 
	"\n")

print("6-2. Favorite Numbers:\n")

favorite_numbers = {
	'george': 'george',
	'george_num': 25,
	'paul': 'paul',
	'paul_num': 18,
	'thom': 'thom',
	'thom_num': 7,
	'morrissey': 'morrissey',
	'morrissey_num': 22,
	'john': 'john',
	'john_num': 9
}

print(str(favorite_numbers['george']).title() + ": " + str(favorite_numbers['george_num']) + "\n" + 
	str(favorite_numbers['paul']).title() + ": " + str(favorite_numbers['paul_num']) + "\n" +  
	str(favorite_numbers['thom']).title() + ": " + str(favorite_numbers['thom_num']) + "\n" +  
	str(favorite_numbers['morrissey']).title() + ": " + str(favorite_numbers['morrissey_num']) + "\n" +  
	str(favorite_numbers['john']).title() + ": " + str(favorite_numbers['john_num']) +
	 "\n")

# 6-3. Glossary:
print("6-3. Glossary:\n")

programming_words = {
	'dictionary': 'dictionary',
	'dictionary_def': 'A dictionary in Python is a collection of key-value pairs.',

	'key_value_pair': 'key value pair',
	'key_value_pair_def': 'A key-value pair is a set of values associated with each other.',

	'if_statement': 'if statement',
	'if_statement_def': 'Python’s if statement allows you to examine the current state of a program '
		'and respond appropriately to that state.',

	'boolean_value': 'boolean value',	
	'boolean_value_def': 'A Boolean value is either True or False, just like the value of a conditional '
		'expression after it has been evaluated.',

	'if_else_block': 'if_else_block',	
	'if_else_block_def': 'An if-else block is similar to a simple if statement, but the else statement '
		'allows you to define an action or set of actions that are executed when the conditional test fails.'
}

print(str(programming_words['dictionary'].title()) + "\n\t" + str(programming_words['dictionary_def']) + "\n\n" + 
	str(programming_words['key_value_pair'].title()) + "\n\t" + str(programming_words['key_value_pair_def']) + "\n\n" + 
	str(programming_words['if_statement'].title()) + "\n\t" + str(programming_words['if_statement_def']) + "\n\n" + 
	str(programming_words['boolean_value'].title()) + "\n\t" + str(programming_words['boolean_value_def']) + "\n\n" + 
	str(programming_words['if_else_block'].title()) + "\n\t" + str(programming_words['if_else_block_def'])
	 + "\n")

# Looping Through a Dictionary
print("Looping Through a Dictionary\nLooping Through All Key-Value Pairs\n")

user_0 = {
	'user_name': 'efermi',
	'first_name': 'enrico',
	'last_name': 'fermi'
}

for key, value in user_0.items():   # 1
	print("\nKey: " + key)			# 2
	print("Value: " + value)		# 3

# As shown at u, to write a for loop for a dictionary, you create names for the 
# two variables that will hold the key and value in each key-value pair. You can 
# choose any names you want for these two variables. This code would work just 
# as well if you had used abbreviations for the variable names, like this:

# for k, v in user_0.items()

# Practice
print("\nPractice 1:")

geri = {
	'first_name': 'komang',
	'middle_name': 'pramanta',
	'last_name': 'gerinata'
}

for key, value in geri.items():
	print("\nKey: " + key)
	print("Value: " + value.title())

john_names = {
	'first_name': 'john',
	'middle_name': 'joseph',
	'last_name': 'mcgowan'
}

for key, value in john_names.items():
	print("\nKey: " + key)
	print("Value: " + value.title())

paul_names = {
	'first_name': 'paul',
	'middle_name': 'james',
	'last_name': 'mccartney'
}

for key, value in paul_names.items():
	print("\nKey: " + key)
	print("Value: " + value.title())
print("\n")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")
print("\n")

favorite_numbers = {
	'george': 25,
	'paul': 18,
	'thom': 7,
	'morrissey': 22,
	'john': 9
}

for name, number in favorite_numbers.items():
	print(name.title() + "'s favorite number is " +
		str(number) + ".")

# Looping Through All the Keys in a Dictionary
print("\nLooping Through All the Keys in a Dictionary")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name in favorite_languages.keys():
	print(name.title())

# Practice 1
print("\nPractice 1")

favorite_numbers = {
	'george': 25,
	'paul': 18,
	'thom': 7,
	'morrissey': 22,
	'john': 9
}

for name in favorite_numbers.keys():
	print(name.title())
print("\n")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

friends = ['sarah', 'edward']

for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi " + name.title() + ". I see your favorite language is " +
			favorite_languages[name].title() + ".")
print("\n")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

if 'erin' not in favorite_languages :
	print("Erin, please take our poll!")

# Looping Through a Dictionary’s Keys in Order
print("\nLooping Through a Dictionary’s Keys in Order")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("\nLooping Through All Values in a Dictionary\n")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# This approach pulls all the values from the dictionary without checking for 
# repeats. That might work fine with a small number of values, but in a poll 
# with a large number of respondents, this would result in a very repetitive 
# list. To see each language chosen without repetition, we can use a set. A set 
# is similar to a list except that each item in the set must be unique:

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# Try It Yourself
# 6-4. Glossary 2:
print("6-4. Glossary 2:\n")

programming_words = {
	'dictionary': 'A dictionary in Python is a collection of key-value pairs.',

	'key_value_pair': 'A key-value pair is a set of values associated with each other.',

	'if_statement': 'Python’s if statement allows you to examine the current state of a program '
		'and respond appropriately to that state.',

	'boolean_value': 'A Boolean value is either True or False, just like the value of a conditional '
		'expression after it has been evaluated.',

	'if_else_block': 'An if-else block is similar to a simple if statement, but the else statement '
		'allows you to define an action or set of actions that are executed when the conditional test fails.',
	'list': 'A list is a collection of items in a particular order.',
	'append': 'A way to add a new element to a list.',
	'insert': 'A way to add a new element at any position in a list.',
	'del': 'A way to remove an item from any position in a list.',
	'pop': 'The pop() method removes the last item in a list, but it lets you work with that item after removing it. '
		'The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.'
}

for word, definition in programming_words.items():
	print(word.title() + ":\n\t" + definition + "\n")

# 6-5. Rivers:
print("6-5. Rivers:\n")

rivers = {
	'nile': 'egypt',
	'ganges': 'india',
	'amazon': 'brazil'
}

for river, country in rivers.items():
	print(river.title() + " runs through " + country.title() + ".")
for river in rivers.keys():
	print(river.title())
for country in rivers.values():
	print(country.title())

# 6-6. Polling:
print("\n6-6. Polling:\n")

names = ['jen', 'sarah', 'edward', 'phil', 'erin']

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in names:
	if name in favorite_languages.keys():
		print("Thank you " + name.title() + " for taking the poll.")
	else:
		print(name.title() + ", please take the favorite language poll.")

# Nesting
# You can nest a set of dictionaries inside a list, a list of items inside a 
# dictionary, or even a dictionary inside another dictionary.
print("\nNesting\nA List of Dictionaries\n")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# A Fleet of 30 Aliens
print("\nA Fleet of 30 Aliens.\n")

aliens = []

# Make 30 green aliens:
for alien in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)) + "\n")

# Make an empty list for storing aliens.
aliens = []

for alien_number in range(0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] =='yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15		

# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")

# Practice (How to change alien's color for one particular section)
print("\nPractice (How to change alien's color for one particular section)\n")

aliens = []
for new_alien in range(30):
	alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
	aliens.append(alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

for alien in aliens[0:5]:
	print(alien)
print("...")

# Practice (How to change alien's color for one particular section)
print("\nPractice (How to change alien's color for all section)\n")

aliens = []
for new_alien in range(30):
	alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(alien)

for alien in aliens[:10]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
for alien in aliens[10:20]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

for alien in aliens:
	print(alien)
print("...")

# A List in a Dictionary
print("\nA List in a Dictionary\n")
# Store information about s pizza being ordered.

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese']
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping.title())
print("\n")

# Nesting a list inside a dictionary

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['python', 'haskell'],
	'phil': ['ruby', 'go']
}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(name.title() + "'s favorite language is:")
	else:
		print(name.title() + "'s favorite languages are:")
	if languages:
		print(len(languages))	
	for language in languages:
		print("\t" + language.title())

# A Dictionary in a Dictionary
print("\nA Dictionary in a Dictionary\n")

users = {
	'aeinstein': {
		'first_name': 'albert',
		'last_name': 'einstein',
		'location': 'princeton'
		},
	'mcurie': {
		'first_name': 'marie',
		'last_name': 'curie',
		'location': 'paris'
		}
}

for name, user_info in users.items():
	print("\nUsername: " + name)
	full_name = user_info['first_name'].title() + " " + user_info['last_name'].title()
	location = user_info['location'].title()

	print("\tFull name: " + full_name)
	print("\tLocation: " + location)

# Practice
print("\nPractice")

users = {
	'aeinstein':{
		'first_name': 'albert',
		'last_name': 'einstein',
		'location': 'princeton'
		},
	'mcurie': {
		'first_name': 'marie',
		'last_name': 'curie',
		'location': 'paris'
		}
}

for username, user_info in users.items():
	print("\nUsername: " + username + "\n\tFull name: " + 
		user_info['first_name'].title() + " " + user_info['last_name'].title() 
		+ "\n\tLocation: " + user_info['location'].title())

# Try It Yourself
print("\nTry It Yourself\n")

print("6-7. People:\n")

paul = {
	'first_name': 'paul',
	'last_name': 'mccartney',
	'age': 79,
	'city': 'london'
}

thom = {
	'first_name': 'thom',
	'last_name': 'yorke',
	'age': 53,
	'city': 'oxford'
}

john = {
	'first_name': 'john',
	'last_name': 'joseph',
	'age': 59,
	'place': 'alachua'
}

people = [paul, thom, john]

for person in people:
	print(person)

# 6-8. Pets:
print("\n6-8. Pets:\n")

apah = {
	'animal': 'bison',
	'owner': 'ang'
}

mishka = {
	'animal': 'bear',
	'owner': 'putin'
}

kurama = {
	'animal': 'fox',
	'owner': 'naruto'
}

gyuki = {
	'animal': 'octopus',
	'owner': 'bee'
}

pets = []
pets.append(apah)
pets.append(mishka)
pets.append(kurama)
pets.append(gyuki)

for pet in pets:
	print(pet)

# 6-9. Favorite Places:
print("\n6-9. Favorite Places:\n")

favorite_places = {
	'john': ['cape peninsula', 'dolomites', 'yellowstone national park'],
	'george': ['milford sound', 'mopion island', 'Red Center'],
	'paul': ['bruges', 'lake garda', 'tromso']
}

for name, places in favorite_places.items():
	print(name.title() + ": " + str(places))

# 6-10. Favorite Numbers:
print("\n6-10. Favorite Numbers:\n")

favorite_numbers = {
	'george': 25,
	'paul': 18,
	'thom': 7,
	'morrissey': 22,
	'john': 9
}

for name, number in favorite_numbers.items():
	if name == 'george':
		number = 25, 15
	elif name == 'paul':
		number = 18, 8
	elif name == 'thom':
		number = 7, 1
	elif name == 'morrissey':
		number = 22, 12
	elif name == 'john':
		number = 9, 1

	print(name.title() + ": " + str(number))

# Practice for exercise 6-10. Favorite numbers
print("\nPractice for exercise 6-10. Favorite numbers")

favorite_numbers = {
	'john': [3, 62],
	'paul': [18, 42],
	'george': [25, 43],
	'thom': [7, 68],
	'morrissey': [22, 59]
}

for name, numbers in favorite_numbers.items():
	if name == 'john':
		numbers.append(59)
	elif name == 'paul':
		numbers.append(79)
	elif name == 'george':
		numbers.append(78)
	elif name == 'thom':
		numbers.append(53)
	elif name == 'morrissey':
		numbers.append(62)

	print("\n" + name.title() + ":")
	for number in numbers:
		print("\t" + str(number))

favorite_numbers = {
	'john': [3, 62],
	'paul': [18, 42],
	'george': [25, 43],
	'thom': [7, 68],
	'morrissey': [22, 59]
}

for name, numbers in favorite_numbers.items():
	if name == 'john':
		numbers.insert(2, 59)
	elif name == 'paul':
		numbers.insert(2, 79)
	elif name == 'george':
		numbers.insert(2, 78)
	elif name == 'thom':
		numbers.insert(2, 53)
	elif name == 'morrissey':
		numbers.insert(2, 62)

	print("\n" + name.title() + ":")
	for number in numbers:
		print("\t" + str(number))

# 6-11. Cities:
print("\n6-11. Cities:\n")

cities = {
	'milan': {
		'country': 'italy',
		'population': '1.352.000',
		'fact': 'The first skyscraper in Italy is now the 10th tallest building '
			'in Milan, and the first one (Unicredit Tower) is almost twice as high. '
			'Milan is home to many skyscrapers; it''s the highest concentration of '
			'skyscrapers in Italy.'
			},
	'paris': {
		'country': 'france',
		'population': '2.161.000',
		'fact': 'Paris is one of the most beautiful cities in the world. It is '
			'known worldwide for the Louvre Museum, Notre-Dame cathedral, and the '
			'Eiffel tower. It has a reputation of being a romantic and cultural '
			'city. The city is also known for its high-quality gastronomy and the '
			'terraces of its cafés.'
			},
	'madrid': {
		'country': 'spain',
		'population': '3.223.000',
		'fact': 'Right after the spectacular demographics of London, home to '
			'around 8.5 million people, and the 3.6 million inhabitants of Berlin, '
			'Madrid comes in third in terms of peaking population numbers of the '
			'European Union.'
			}
}

for city, information in cities.items():
	print("\n" + city.title())
	for key, fact in information.items():
		print("\t" + key.title() + ": " + fact.title())

# 6-12. Extensions:

cars = {
	'supercars': {
		'horsepower': '550+'
		},
	'hypercars': {
		'horsepower': '800+'
		},
	'megacars': {
		'horsepower': '1340+'
		}
}

cars['supercars'] = {'horsepower': '550+', 'product': 'ford gt'}
cars['hypercars'] = {'horsepower': '800+', 'product': 'pagani huayra'}
cars['megacars'] = {'horsepower': '1340+', 'product': 'koenigsegg one'}

for car, dictionary in cars.items():
	print("\n" + car.title())
	for key, info in dictionary.items():
		print("\t" + key.title() + ": " + info.title())

users = {
	'aeinstein': {
		'first_name': 'albert',
		'last_name': 'einstein',
		'location': 'princeton'
		},
	'mcurie': {
		'first_name': 'marie',
		'last_name': 'curie',
		'location': 'paris'
		}
}

for user, dictionary in users.items():
	if user == 'aeinstein':
		user = 'john'
		dictionary = {
			'full name': 'john joseph mcgowann',
			'place & birthdate': 'new york, october 3rd, 1962',
			'band': 'cro-magnon',
			'song': 'show you no mercy',
			'genre': 'hardcore punk'
			}
	elif user == 'mcurie':
		user = 'george'
		dictionary = {
			'full name': 'george harrison',
			'place & birthdate': 'liverpool, February 25th, 1943',
			'band': 'the beatles',
			'song': 'here comes the sun',
			'genre': 'rock'
			}
	print("\n" + user.title() + ":")
	for key, value in dictionary.items():
		print("\t" + key.title() + ": " + value.title() + ".")

