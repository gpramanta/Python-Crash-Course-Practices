bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[2].upper())
print(bicycles[3].title() + "\n")

# Accessing the last, 2nd data and so on in the list:
print(bicycles[-1].upper())
print(bicycles[-2].upper())
print(bicycles[-3].title() + "\n")

# Example1:
name = ['komang ', 'pramanta ', 'gerinata']
age = [17, 21, 22, 25]
year = [2014, 2018, 2019, 2022]
full_name = name[0] + name[1] + name[2]
message1 = "\tHello my name is " + full_name.title() + "." + " People usually call me " + name[2].title() + ".\n"
message2 = "I attended university in " + str(year[0]) + " when I was " + str(age[0]) + " years old and graduated in " + str(year[1]) + " when I was " + str(age[-3]) + " years old." + "\n"
message3 = "I got my first job in " + str(year[2]) + " at " + str(age[2]) + " years old and now freelancing at " + str(age[-1]) + " years old in " + str(year[-1]) + ".\n"
print(message1 + message2 + message3 + "\n")

# Try it Yourself
# 3-1. Names:
names = ['mercedes', 'lamborghini', 'ferrari', 'shelby', 'viper']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4] + "\n")

# 3-2. Greetings:
greeting = "Good Morning "
print(greeting + names[0].title())
print(greeting + names[1].title())
print(greeting + names[2].title())
print(greeting + names[3].title())
print(greeting + names[4].title() + "\n")

# 3-3. Your own List:
motor = ['vario', 'mio', 'supra']
grade = ['first', 'second', 'third']
text1 = "At " + grade[0] + " grade senior high school I rode a " + motor[-1].title() + "."  
text2 = "At " + grade[1] + " grade senior high school I rode a " + motor[-2].title() + "."
text3 = "At " + grade[2] + " grade senior high school I rode a " + motor[-3].title() + ".\n"
print(text1 + "\n" + text2 + "\n" + text3)

# Changing, Adding, Removing Elements
countries = ['china', 'us', 'germany', 'netherlands', 'france']
countries[2] = 'leichtenstein'
print(countries[0].title() + " " + countries[1].title() + " " + countries[2].title() + " " + countries[3].title() + " " + countries[4].title() + " \n")

# Adding Elements to the List
# Appending Elements to the End of a List
countries = ['china', 'us', 'germany', 'netherlands', 'france']
countries.append('indonesia')
print(countries)
print(countries[-1].upper() + "\n")

foods = []
foods.append('nasi goreng')
foods.append('cap cay')
foods.append('bakso')
foods.append('mie goreng')
print(str(foods) + "\n")

# Inserting Elements into a List
print(foods)
foods.insert(0, 'cah kangkung')
foods.insert(2, 'tipat santok')
print(str(foods).upper() + "\n")

# Removing Elements from a List
# Removing an Item Using the del Statement
print(foods)
del foods[0]
print(str(foods) + "\n")

# Removing an Item Using the pop() Method
vegetables = ['carrot', 'cabbage', 'spinach', 'cauliflower']
print(vegetables)
popped_vegetables = vegetables.pop()
print(vegetables)
print(popped_vegetables + "\n")

cities = []
cities.append('denpasar')
cities.append('gianyar')
cities.append('badung')
print(cities)
cities_popped = cities.pop()
print(cities_popped)
print(cities)
story = "I went to " + cities_popped.title() + " yesterday"
print(story + "\n")

# Popping Items from any Position in a List
color = []
color.append('golden')
color.append('blue')
color.append('white')
color.append('red')
color.append('orange')
print(color)
story = "The colors of my car are " + color.pop(0) + " and " + color.pop(0) + "." 
print(story)
print(str(color) + "\n")

# Removing an Item by Value
brands = []
brands.append('chitato')
brands.append('cheetos')
brands.append('lays')
brands.append('pringles')
print(brands)
brands.remove('pringles')
print(brands)
del brands[0]
print(str(brands) + "\n")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print("\nThe brands of my motorcycles are " + motorcycles[0].title() + " and " + motorcycles[1].title() + ".\n")

# 3-4. Guest List:
guests = []
guests.append('george harrison')
guests.append('john joseph')
guests.append('thom yorke')
guests.append('paul mcCartney')
my_name = []
my_name.append('komang ')
my_name.append('pramanta ')
my_name.append('gerinata')
full_name = my_name[0] + my_name[1] + my_name[2]
invitation0 = "Congratulation " + guests[0].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation1 = "Congratulation " + guests[1].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation2 = "Congratulation " + guests[2].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation3 = "Congratulation " + guests[3].title() + "! You are invited to " + full_name.title() + "'s birthday party."
print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print("List of Guests: " + str(guests) + "\n")

# 3-5. Changing Guest List:
information = "Unfortunately " + guests.pop(2).title() + " and " + guests.pop(2).title() + " cannot come."
print(information)
guests.insert(2, 'john lennon')
guests.insert(3, 'jonny greenwood')
print(guests)
invitation0 = "Congratulation " + guests[0].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation1 = "Congratulation " + guests[1].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation2 = "Congratulation " + guests[2].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation3 = "Congratulation " + guests[3].title() + "! You are invited to " + full_name.title() + "'s birthday party."
print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3 + "\n")

# 3-6. More Guests:
print("As I found a bigger table for my birthday party I would like to invite more guest.")
guests.insert(0, 'matt bellamy')
guests.insert(2, 'morrissey')
guests.append('alanis morrissete')
print(guests)
invitation0 = "Congratulation " + guests[0].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation1 = "Congratulation " + guests[1].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation2 = "Congratulation " + guests[2].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation3 = "Congratulation " + guests[3].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation4 = "Congratulation " + guests[4].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation5 = "Congratulation " + guests[5].title() + "! You are invited to " + full_name.title() + "'s birthday party."
invitation6 = "Congratulation " + guests[6].title() + "! You are invited to " + full_name.title() + "'s birthday party."
print(invitation0)
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6 + "\n")

# 3-7. Shrinking Guest List:
print("I was just informed that the dinner table won't arrive in time thus I can only invite 2 guests")
print(guests)
cancel0 = "Sorry " + guests.pop(0).title() + " You cannot come to " + full_name.title() + "'s birthday party."
cancel1 = "Sorry " + guests.pop(1).title() + " You cannot come to " + full_name.title() + "'s birthday party."
cancel2 = "Sorry " + guests.pop(2).title() + " You cannot come to " + full_name.title() + "'s birthday party."
cancel3 = "Sorry " + guests.pop(2).title() + " You cannot come to " + full_name.title() + "'s birthday party."
cancel4 = "Sorry " + guests.pop(2).title() + " You cannot come to " + full_name.title() + "'s birthday party."
print(cancel0)
print(cancel1)
print(cancel2)
print(cancel3)
print(cancel4)
print(guests)
final_invitation0 = "Congratulation " +  guests[0].title() + "! You are invited to " + full_name.title() + "'s birthday party."
final_invitation1 = "Congratulation " +  guests[1].title() + "! You are invited to " + full_name.title() + "'s birthday party."
print(final_invitation0)
print(final_invitation1)
del guests[0]

print(str(guests) + "\n")

# Organizing a List
# Sorting a List Permanently with the sort() Method
cars = []
cars.append('bmw')
cars.append('lamborghini')
cars.append('ferrari')
cars.append('tesla')
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(str(cars) + "\n")

elements = []
elements.append('sound')
elements.append('ether')
elements.append('water')
elements.append('fire')
info = "These are the original elements: " + str(elements) + "."
info1 = "These are the sorted elements: " + str(sorted(elements)) + "."
info2 = "Here is the original list of elements: " + str(elements) + "."
print(info)
print(info1)
print(str(info2) + "\n")

islands = []
islands.append('sumatra')
islands.append('borneo')
islands.append('java')
islands.sort(reverse=True)
print(islands)

months = []
months.append('january')
months.append('february')
months.append('march')
print(months)
months.sort(reverse=True)
print(months)
print(str(sorted(months)) + "\n")

# Printing a List in Reverse Order
smartphone = []
smartphone.append('samsung')
smartphone.append('huawei')
smartphone.append('xiaomi')
smartphone.append('microsoft')
print(smartphone)
smartphone.reverse()
print(smartphone)
smartphone.reverse()
print(str(smartphone) + "\n")

# Finding the Length of a List
print(smartphone)
total = len(smartphone)
print(str(total) + "\n")
# Note Python counts the items in a list starting with one, so you shouldn’t run into any offby-one errors 
# when determining the length of a list.

# 3-8. Seeing the World:
destination = []
destination.append('potala palace')
destination.append('ankor wat')
destination.append('tovp')
destination.append('taktsang dzong')
print(destination)
print(sorted(destination))
print(destination)
print(sorted(destination))
print(destination)
destination.reverse()
print(destination)
destination.reverse()
print(destination)
destination.sort()
print(destination)
destination.sort(reverse=True)
print(str(destination) + "\n")

# 3-9. Dinner Guests:
guests = []
guests.append('george harrison')
guests.append('john joseph')
guests.append('thom yorke')
guests.append('paul mcCartney')
total_guests = len(guests)
print(total_guests)

guests.insert(2, 'john lennon')
guests.insert(3, 'jonny greenwood')
print(total_guests)
print(guests)
total_guests = len(guests)
print(total_guests)

guests.insert(0, 'matt bellamy')
guests.insert(2, 'morrissey')
guests.append('alanis morrissete')
print(guests)
total_guests = len(guests)
print(total_guests)

cancel0 = guests.pop(0)
cancel1 = guests.pop(1)
cancel2 = guests.pop(2)
cancel3 = guests.pop(2)
cancel4 = guests.pop(2)
print(guests)
total_guests = len(guests)
print(total_guests)

del guests[0]
del guests[0]
del guests[0]
del guests[0]
total_guests = len(guests)
print(total_guests)

# 3-10. Every Function:
bands = []
bands.append('radiohead')
bands.append('the beatles')
bands.append('cro-magnon')
# Accessing Elements in a List
print(str(bands[-1]).title())
#==============================

# Modifying Elements in a List
print(bands)
bands[0] = "the smiths"
print(bands)
#==============================

# Appending Elements to the End of a List
bands.append('radiohead')
print(bands)
#==============================

# Inserting Elements into a List
bands.insert(1, 'the calling')
print(bands)
#==============================

# Removing an Item Using the del Statement
del bands[-1]
print(bands)
#==============================

# Removing an Item Using the pop() Method
pop = bands.pop(1).title()
review = pop + " is a pop band."
print(review)
#==============================

# Removing an Item by Value
bands.remove('the smiths')
print(bands)
#==============================

# Sorting a List Permanently with the sort() Method
bands.sort()
print(bands)
bands.sort(reverse=True)
print(bands)
#==============================

# Sorting a List Temporarily with the sorted() Function
print(sorted(bands))
#==============================

# Printing a List in Reverse Order
bands.append('muse')
bands.append('coldplay')
print(bands)
bands.reverse()
print(bands)
#==============================

# Finding the Length of a List
total_bands = len(bands)
print(str(total_bands) + "\n")
#==============================

# Avoiding Index Errors When Working with Lists
transportation = []
transportation.append('motorbike')
transportation.append('car')
transportation.append('plane')
transportation.append('ship')
print(transportation[-1])

# 3-11. Intentional Error:
print(transportation)
print(transportation[3])