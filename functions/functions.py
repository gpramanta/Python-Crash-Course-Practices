# Defining a Function

# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
#
# greet_user()
#
# Practice
#
# def greet_user():
#     print("Hello World!")
#
# greet_user()
#
# def my_name():
#     print("Komang Pramanta Gerinata")
#
# my_name()
#
# def squares():
#     squares = []
#     for number in range(1,11):
#         square = number**2
#         squares.append(square)
#     print(squares)
# squares()

# def even_odd_numbers():
#
#     # Variables
#     even_odd = "Enter 'even' for displaying even numbers & 'odd' for odd numbers. \n"
#     min_num = "Enter minimum number. \n"
#     max_num = "Enter maximum number. \n"
#
#     program = 'active'
#     while program == 'active':
#         even_odd_input = input(even_odd)
#         min_num_input = int(input(min_num))
#         max_num_input = int(input(max_num))
#         if even_odd_input == 'even':
#             number = min_num_input
#             while number < max_num_input:
#                 number += 1
#                 if number % 2 == 0:
#                     print(number)
#         elif even_odd_input == 'odd':
#             number = min_num_input
#             while number < max_num_input:
#                 number += 1
#                 if number % 2 != 0:
#                     print(number)
# even_odd_numbers()

# Passing Information to a Function

# def greet_user(username):
#     """Display a Simple Greeting."""
#     print("Hello " + username.title())
# greet_user('jessie')

# Practice

# def question(country):
#     input("What is the capital city of " + country.title() + "? \n")
#
#
# program = 'active'
# while program == 'active':
#     question('indonesia')

# def birthday(name):
#     print("Happy Birthday " + name.title() + "!")
# birthday('geri')
# birthday('nata')
# birthday('rama')

# Try It Yourself
# 8-1. Message:

# def display_message(name):
#     print(name.title() + " is learning about Functions in Python.\n")
# display_message('geri')

# 8-2. Favorite Book:

# def favorite_book(title):
#     sentence = "One of my favorite books is "
#     print(sentence + title.title() + ".\n")
# favorite_book('python crash course')

# Passing Arguments
# def describe_pet(animal_type, pet_name):
#     print("I have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
#
# def pet(animal, name):
#     print("I have a " + animal + ".\nMy " + animal + "'s name is " + name.title() + ".\n")
# pet('hamster', 'harry')

# Multiple Function Calls

# def describe_pet(animal_type, pet_name):
#     print("I have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# Keyword Arguments

# def describe_pet(animal_type, pet_name):
#     print("I have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')

# Default Values


# def describe_pet(animal_type, pet_name='willie'):
#
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='dog')

# def describe_pet(pet_name, animal_type='dog'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet('willie')

# def describe_pet(animal_type='dog', pet_name='willie'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(animal_type='hamster', pet_name='harry')

# Practice


# def describe_pet(pet_name='willie', animal_type='dog'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet()

# Equivalent Function Calls

# def describe_pet(pet_name, animal_type='dog'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('willie')
#
#
# def describe_pet(pet_name, animal_type='dog'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(pet_name='willie')

# def describe_pet(animal_type, pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet(animal_type='dog', pet_name='willie')
#
# def describe_pet(pet_name, animal_type='cat'):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title())
# describe_pet(pet_name='nunuk')


# Try It Yourself

# 8-3. T-Shirt:
# def make_shirt(size, text):
#     print("My t-shirt's size is " + size.title() +
#           " and a text " + "'" + text.title() + "' is printed on it.")
# make_shirt('l', 'i love bali')
#
# def make_shirt(text, size='l'):
#     print("\nMy t-shirt's size is " + size.title() +
#           " and a text " + "'" + text.title() + "' is printed on it.")
# make_shirt(text='hello world!')

# 8-4. Large Shirts:
# def make_shirt(text, size='large'):
#     print("\nMy t-shirt's size is " + size + " and a text " +
#           "'" + text.title() + "' is printed on it.")
# make_shirt('i love python')
#
# def make_shirt(size, text='i love python'):
#     print("\nMy t-shirt's size is " + size + " and a text " +
#           "'" + text.title() + "' is printed on it.")
# make_shirt('medium')
#
# def make_shirt(size='small', text='hey jude!'):
#     print("\nMy t-shirt's size is " + size + " and a text '" +
#           text.title() + "' is printed on it.\n")
# make_shirt()

# 8-5. Cities:

# def describe_city(city, country='indonesia'):
#     print(city.title() + " is in " + country.title() + ".")
# describe_city('ubud')
# describe_city('nusantara')
# describe_city('paris')

# Return Values
# Returning a Simple Value

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + " " + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# Practice
# def my_name(first_name, middle_name, last_name):
#     full_name = first_name + " " + middle_name + " " + last_name
#     return full_name.title()
# identity = my_name('komang', 'pramanta', 'gerinata')
# print(identity)

# Making an Argument Optional
# def get_formatted_name(first_name, middle_name, last_name):
#     """Return full name, neatly formatted."""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('james', 'paul', 'mccartney')
# print(musician)

# Practice
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# first = 'Enter your first name. \n'
# middle = 'Enter your middle name. Type "skip" if you do not have middle name. \n'
# last = 'Enter your last name. \n'
# stop = 'Enter ''quit'' to end the program. \n'
#
# names = []
# program = 'active'
# while program == 'active':
#     first_input = input(first + stop)
#     if first_input == 'quit':
#         break
#     else:
#         names.append(first_input)
#     middle_input = input(middle + stop)
#     if middle_input == 'quit':
#         break
#     elif middle_input != 'skip':
#         names.append(middle_input)
#     last_input = input(last + stop)
#     if last_input == 'quit':
#         break
#     else:
#         names.append(last_input)
#     print(names)
#     break
#
# if len(names) > 2:
#     person = get_formatted_name(names[0], names[2], names[1])
# else:
#     person = get_formatted_name(names[0], names[1])
# print(person)

# Practice
# def squares():
#     square_list = []
#     minimum = min_num_input
#     maximum = max_num_input
#     for number in range(minimum, maximum):
#         square = number**2
#         square_list.append(square)
#     return square_list
#
#
# min_num = "Enter the minimum number. \n"
# max_num = "Enter the maximum number. \n"
# enter_print = "Enter 'print' to show the squares list. \n"
# enter_quit = "Enter 'quit' to end the program. \n"
#
# program = 'active'
# while program == 'active':
#     min_num_input = input(min_num + enter_quit)
#     if min_num_input != 'quit':
#         min_num_input = int(min_num_input)
#     else:
#         break
#     max_num_input = input(max_num + enter_quit)
#     if max_num_input != 'quit':
#         max_num_input = int(max_num_input)
#     else:
#         break
#     squares()
#     enter_print_input = input(enter_print + enter_quit)
#     if enter_print_input == 'quit':
#         break
#     else:
#         print(squares())

# Returning a Dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {
#         'first name': first_name,
#         'last name': last_name
#     }
#     return person
#
#
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=''):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age='42')
# print(musician)


# Practice 1
# def name(first_name, last_name):
#     dictionary = {
#         'first': first_name,
#         'last': last_name
#     }
#     return dictionary
#
#
# person = name('johnny', 'depp')
# print(person)

# def names(first_name, last_name, middle_name=''):
#     dictionary = {
#         'first': first_name,
#         'last': last_name,
#         'middle': middle_name
#     }
#     return dictionary
# figure = names('james', 'mccartney', 'paul')
# print(figure)

# Practice 2
# def name(first_name, middle_name, last_name):
#     dictionary = {
#         'first': first_name,
#         'middle': middle_name,
#         'last': last_name
#     }
#     return dictionary


# one = "Enter your first name. \n"
# two = "Enter your middle name. \n"
# three = "Enter your last name. \n"
# enter_print = "Enter 'print' to print your name. \n"
# stop = "Enter 'quit' to end the program. \n"
#
# program = 'active'
# while program == 'active':
#     one_input = input(one + stop)
#     if one_input == 'quit':
#         break
#     two_input = input(two + stop)
#     if two_input == 'quit':
#         break
#     three_input = input(three + stop)
#     if three_input == 'quit':
#         break
#     print_input = input(enter_print + stop)
#     if print_input == 'quit':
#         break
#     elif print_input == 'print':
#         person = name(one_input, two_input, three_input)
#         print(person)

# Practice 3
# def name(first_name, last_name, middle_name=''):
#     if middle_name:
#         dictionary = {
#             'first': first_name,
#             'middle': middle_name,
#             'last': last_name
#         }
#     else:
#         dictionary = {
#             'first': first_name,
#             'last': last_name
#         }
#     return dictionary
#
#
# person = name('johnny', 'depp')
# print(person)

# Practice 4

# def odd(minimum, maximum):
#     odd_list = []
#     number = minimum
#     while number < maximum:
#         number += 1
#         if number % 2 != 0:
#             odd_list.append(number)
#     print(odd_list)
#     return odd_list
#
#
# def even(minimum, maximum):
#     even_list = []
#     number = minimum
#     while number < maximum:
#         number += 1
#         if number % 2 == 0:
#             even_list.append(number)
#     print(even_list)
#     return even_list
#
#
# odd_even = "Enter 'odd' to show odd numbers & 'even' to show even numbers. \n"
# min_num = "Enter the minimum number. \n"
# max_num = "Enter the maximum number. \n"
# confirm = "Enter 'print' to show the numbers. \n"
# stop = "Enter 'quit' to end the program. \n"
#
# program = 'active'
# while program == 'active':
#     odd_even_input = input(odd_even + stop)
#     if odd_even_input == 'quit':
#         break
#     elif odd_even_input == 'odd':
#         min_num_input = input(min_num + stop)
#         if min_num_input == 'quit':
#             break
#         else:
#             min_num_input = int(min_num_input)
#         max_num_input = input(max_num + stop)
#         if max_num_input == 'quit':
#             break
#         else:
#             max_num_input = int(max_num_input)
#             odd(min_num_input, max_num_input)       # Function Call for Odd Formula
#
#     elif odd_even_input == 'even':
#         min_num_input = input(min_num + stop)
#         if min_num_input == 'quit':
#             break
#         else:
#             min_num_input = int(min_num_input)
#         max_num_input = input(max_num + stop)
#         if max_num_input == 'quit':
#             break
#         else:
#             max_num_input = int(max_num_input)
#             even(min_num_input, max_num_input)      # Function Call for Even Formula

# Using a Function with a while Loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatlly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()


# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("Hello, " + formatted_name + "!")

# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# while True:
#     print("\nPlease enter your name:")
#     print("Enter 'q' at any time to quit.")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# Practice
# def greeting(first_name, last_name):
#     greet = first_name + ' ' + last_name
#     return greet
#
#
# prompt = "\nPlease tell me your name:\nEnter 'q' at any time to quit)"
# first = "\nFirst name: "
# last = "Last name: "
#
# program = 'active'
# while program == 'active':
#     first_input = input(prompt + first)
#     if first_input == 'q':
#         break
#     last_input = input(last)
#     if last_input == 'q':
#         break
#     argument_greeting = greeting(first_input, last_input)
#     print("\nHello, " + argument_greeting.title() + "!")

# Try It Yourself

# 8-6. City Names:
# def city_country(city, country):
#     my_city_country = city + ", " + country
#     return my_city_country.title()
#
#
# city_with_country = city_country('denpasar', 'indonesia')
# print(city_with_country)
# city_with_country = city_country('rome', 'italy')
# print(city_with_country)
# city_with_country = city_country('paris', 'france')
# print(city_with_country)

# 8-7. Album:
# def make_album(artist_name, album_title, number_of_tracks=''):
#     dictionary = {'artist': artist_name, 'album': album_title}
#     if number_of_tracks:
#         dictionary['number of tracks'] = number_of_tracks
#     return dictionary
#
#
# album = make_album('radiohead', 'ok computer', number_of_tracks=12)
# print(album)
# album = make_album('the smiths', 'meat is murder', number_of_tracks=10)
# print(album)
# album = make_album('bjork', 'post', number_of_tracks=11)
# print(album)

# 8-8. User Albums:
# def make_album(artist_name, album_title, number_of_tracks=''):
#     dictionary = {'artist': artist_name, 'album': album_title}
#     if number_of_tracks:
#         dictionary['number of tracks'] = number_of_tracks
#     return dictionary
#
#
# prompt = "\nPlease enter artist name, album title, and number of tracks:"
# artist = "\nEnter artist name: "
# album = "Enter album title: "
# tracks = "Enter number of tracks: "
# stop = "\n(Enter 'q' to end the program.)"
#
# program = 'active'
# while program == 'active':
#     artist_input = input(prompt + stop + artist)
#     if artist_input == 'q':
#         break
#     album_input = input(album)
#     if album_input == 'q':
#         break
#     tracks_input = input(tracks)
#     if tracks_input == 'q':
#         break
#     music = make_album(artist_input, album_input, tracks_input)
#     print("\n" + str(music))


# Passing a List
# def greet_users(usernames):
#     """Print a simple greeting to each user in the list."""
#     for name in usernames:
#         print("Hello, " + name.title() + "!")
#
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# Practice
# def a_list(names):
#     for name in names:
#         print("Hello, " + name.title() + "!")
#
#
# usernames = ['geri', 'nata', 'komang']
# a_list(usernames)

# Practice 2
# usernames = []
# def user_list(usernames):
#     for name in usernames:
#         print("Hello, " + name.title() + "!")
#
#
# username = "Enter username: "
# stop = "Enter 'q' to end the program. \n"
# greet = "\nEnter 'g' to greet the user. \n"
# skip = "Enter 's' to skip. \n"
#
# program = 'active'
# while program == 'active':
#     usernames_input = input(stop + username)
#     if usernames_input == 'q':
#         break
#     else:
#         usernames.append(usernames_input)
#         print(usernames)
#         if usernames:
#             greet_input = input(greet + skip + stop)
#             if greet_input == 'q':
#                 break
#             elif greet_input == 'g':
#                 user_list(usernames)
#             elif greet_input == 'skip':
#                 continue

# Practice 3
# model_list = []
# def models(model_list):
#     for model in model_list:
#         print(model.title())
#
#
# prompt = "Printing model: "
# confirm = "\nEnter 'print' to print the model. \n"
# ok = "The following models have been printed:"
# skip = "Enter 'skip' to skip. \n"
# stop = "Enter 'q' to end the program. \n"
#
# program = 'active'
# while program == 'active':
#     model_input = input(stop + prompt)
#     if model_input == 'q':
#         break
#     else:
#         model_list.append(model_input)
#         print(model_list)
#         if model_list:
#             confirm_input = input(confirm + skip + stop)
#             if confirm_input == 'q':
#                 break
#             elif confirm_input == 'print':
#                 print(ok)
#                 models(model_list)
#             elif confirm_input == 'skip':
#                 continue

# Modifying a List in a Function
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_model = unprinted_designs.pop()
#     print("Printed model: " + current_model.title())
#     completed_models.append(current_model)
# print("\nThe following models have been printed:")
# for model in completed_models:
#     print(model.title())

# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # Simulate creating a 3D print from the design.
#         print("Printing model: " + current_design.title())
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for model in completed_models:
#         print(model.title())
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Practice (My Version - Lesser Codes Quality)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# def designs(unprinted_designs):
#     while unprinted_designs:
#         current_model = unprinted_designs.pop()
#         print("Printed model: " + current_model.title())
#         completed_models.append(current_model)
#     print("\nThe following models have been printed:")
#     for model in completed_models:
#         print(model.title())
#
#
# design_list = unprinted_designs
# designs(design_list)

# Practice (My Best Version - Lesser Codes Quality)
# def make_model(unprinted_models, printed_models):
#     while unprinted_models:
#         current_model = unprinted_models.pop()
#         print("Printing model: " + current_model.title())
#         printed_models.append(current_model)
#
#
# def show_printed_models(printed_models):
#     print("\nThe following models have been printed:")
#     for model in printed_models:
#         print(model.title())
#
#
# stop = "\nEnter 'q' to end the program."
# prompt = "\nEnter unprinted model: "
# show = "\nEnter 'ok' to print the model."
#
# unprinted_models = []
# printed_models = []
# program = 'active'
# while program == 'active':
#     prompt_input = input(stop + prompt)
#     if prompt_input == 'q':
#         break
#     else:
#         unprinted_models.append(prompt_input)
#         print(unprinted_models)
#         while unprinted_models:
#             prompt_2 = input(stop + show + prompt)
#             if prompt_2 == 'q':
#                 break
#             elif prompt_2 == 'ok':
#                 print(" ")
#                 make_model(unprinted_models, printed_models)
#                 show_printed_models(printed_models)
#             else:
#                 unprinted_models.append(prompt_2)
#                 print(unprinted_models)
#         break

# Preventing a Function from Modifying a List
# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # Simulate creating a 3D print from the design.
#         print("Printing model: " + current_design.title())
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for model in completed_models:
#         print(model.title())
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
#
# print(unprinted_designs)
# print(completed_models)

# Try It Yourself
# 8-9. Magicians:
# def show_magicians(magicians):
#     """Display list of magicians"""
#     print("Here are the list of magicians:")
#     for magician in magicians:
#         print(magician.title())
#
#
# magicians = ['sacred riana', 'david copperfield', 'david blaine']
# show_magicians(magicians)

# 8-10. Great Magicians:
# def make_magicians(list_magicians, printed_magicians):
#     while list_magicians:
#         current_magician = list_magicians.pop()
#         print("Magician name: " + current_magician)
#         printed_magicians.append(current_magician)
#
#
# def show_magicians(printed_magicians):
#     print("\nThe following magician's name has been printed:")
#     for name in printed_magicians:
#         print(name.title())
#
#
# def make_great(printed_magicians):
#     while printed_magicians:
#         magician = "Great " + printed_magicians.pop()
#         list_magicians.append(magician)
#
#
# list_magicians = ['david blaine', 'david copperfield', 'sacred riana']
# printed_magicians = []
#
# make_magicians(list_magicians, printed_magicians)
# show_magicians(printed_magicians)
#
# make_great(printed_magicians)
# show_magicians(list_magicians)

# 8-11. Unchanged Magicians:
# def make_magicians(list_magicians, printed_magicians):
#     while list_magicians:
#         current_magician = list_magicians.pop()
#         print("Magician name: " + current_magician)
#         printed_magicians.append(current_magician)
#
#
# def show_magicians(printed_magicians):
#     print("\nThe following magician's name has been printed:")
#     for name in printed_magicians:
#         print(name.title())
#
#
# def make_great(printed_magicians):
#     while printed_magicians:
#         magician = "Great " + printed_magicians.pop()
#         great_magicians.append(magician)
#
#
# list_magicians = ['david blaine', 'david copperfield', 'sacred riana']
# printed_magicians = []
# great_magicians = []
#
# make_magicians(list_magicians, printed_magicians)
# show_magicians(printed_magicians)
#
# make_great(printed_magicians[:])
# show_magicians(great_magicians)
#
# print(list_magicians)
# print(printed_magicians)
# print(great_magicians)

# Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Now we can replace the print statement with a loop that runs through the list of toppings and describes the pizza
# being ordered:


# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping.title())
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(topping.title())
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Practice
# def make_nachos(size, *fillings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) + "-inch nachos with the following fillings:")
#     for filling in fillings:
#         print(filling.title())
#
#
# make_nachos(9, 'tomatoes', 'potatoes', 'cabbages')
# make_nachos(18, 'just egg', 'beyond meat', 'salad')

# Practice 2
# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(topping.title())
#
#
# greet = "Welcome to Pizza Hut!"
# stop = "Enter 'q' to end the program."
# size = "How large do you want your pizza? (in inch): "
# topping = "What topping do you want on your pizza: "
# topping_2 = "Do you want to add another topping?\nEnter your topping: "
# confirm = "Enter 'ok' to confirm your order & 'or' to order another pizza. "
#
# program = 'active'
# while program == 'active':
#     prompt_1 = input("\n" + stop + "\n" + size)
#     if prompt_1 == 'q':
#         break
#     topping_in = input("\n" + stop + "\n" + topping)
#     if topping_in == 'q':
#         break
#     ok_or = input("\n" + stop + "\n" + confirm)
#     if ok_or == 'q':
#         break
#     elif ok_or == 'or':
#         continue
#     else:
#         make_pizza(prompt_1, topping_in)

# Using Arbitrary Keyword Arguments
# def build_profile(first_name, last_name, **user_info):
#     """Build a dictionary containing everything about a user."""
#     profile = {}
#     profile['first name'] = first_name
#     profile['last name'] = last_name
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)


# Practice
# def build_profile(first_name, last_name, **user_infos):
#     dictionary = {}
#     dictionary['first name'] = first_name
#     dictionary['last name'] = last_name
#     for key, value in user_infos.items():
#         dictionary[key] = value
#     return dictionary
#
#
# profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(profile)
#
#
# def build_musician(first_name, last_name, **musician_info):
#     musician = {}
#     musician['first name'] = first_name
#     musician['last name'] = last_name
#     for key, value in musician_info.items():
#         musician[key] = value
#     return musician


# def build_person2(first_name, last_name, **arbitrary):
#     """Display description of a person in a dictionary form."""
#     dictionary = {}
#     for key, value in arbitrary.items():
#         dictionary['first name'] = first_name
#         dictionary['last name'] = last_name
#         dictionary[key] = value
#     return dictionary
#
#
# person = build_person2('albert', 'einstein', location='princeton', field='physics')
# print(person)

# Try It Yourself
# 8-12. Sandwiches:
# def make_sandwich(bread, *filling):
#     if bread == 2 and len(filling) == 1:
#         print("\nYou order a sandwich with the following filling:")
#         for item in filling:
#             print(item.title())
#     elif bread == 2 and len(filling) > 1:
#         print("\nYou order a sandwich with the following fillings:")
#         for item in filling:
#             print(item.title())
#     elif bread > 2 and len(filling) == 1:
#         print("\nYou order a sandwich with " + str(bread) + " breads and with the following filling:")
#         for item in filling:
#             print(item.title())
#     elif bread > 2 and len(filling) > 1:
#         print("\nYou order a sandwich with " + str(bread) + " breads and with the following fillings:")
#         for item in filling:
#             print(item.title())
#
#
# make_sandwich(2, 'sausages')
# make_sandwich(2, 'mushrooms', 'macaroni')
# make_sandwich(3, 'salad')
# make_sandwich(4, 'extra cheese', 'sausages')

# 8-13. User Profile:
# def build_profile(first_name, last_name, **user_info):
#     dictionary = {}
#     dictionary['first name'] = first_name
#     dictionary['last name'] = last_name
#     for key, value in user_info.items():
#         dictionary[key] = value
#     return dictionary
#
#
# person = build_profile('komang', 'geri', location='gianyar', interest='programming languages', hobby='reading')
# print(person)

# 8-14. Cars:
# def make_car(manufacturer, model, **specifications):
#     dictionary = {}
#     dictionary['Manufacturer'] = manufacturer.title()
#     dictionary['model'] = model.title()
#     for key, value in specifications.items():
#         dictionary[key] = value
#     return dictionary
#
#
# car = make_car('hyundai', 'genesis g80', color='black', technology='ev')
# print(car)
#
#
# def make_car(manufacturer, model, **specifications):
#     dictionary = {}
#     dictionary['Manufacturer'] = manufacturer.title()
#     dictionary['Model'] = model.title()
#     for key, value in specifications.items():
#         dictionary[key] = value
#     return dictionary
#
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# Storing Your Functions in Modules
# Importing an Entire Module
# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Practice
# import pizza
#
# pizza.make_pizzas(16, 'pepperoni')
# pizza.make_pizzas(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from pizza import make_pizza, make_pizzas
#
# make_pizza(16, 'macaroni')
# make_pizzas(9, 'just egg')

# Practice
# from pizza import make_pizzas
#
# make_pizzas(9, 'beyond sausages')
# make_pizzas(13, 'beyond sausages', 'just egg', 'extra cheese')

# Using as to Give a Function an Alias
# from pizza import make_pizza as mp
#
# mp(16, 'macaroni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# import pizza as p
#
# p.make_pizza(16, 'macaroni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# from pizza import *
#
# make_pizza(16, 'macaroni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Try It Yourself
# 8-15. Printing Models:
# import printing_functions
#
# unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# printed_models = []
# printing_functions.make_model(unprinted_models, printed_models)
# printing_functions.show_model(printed_models)
#
#
# 8-16. Imports:
# import printing_functions
# printing_functions.make_car('hyundai', 'genesis g80', color='black', technology='EV')
#
# from pizza import make_pizza
# make_pizza(16, 'macaroni')
#
# from pizza import make_pizzas as mps
# mps(12, 'mushrooms', 'green pepper', 'extra cheese')
#
# import printing_functions as pf
# unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# printed_models = []
# pf.make_model(unprinted_models, printed_models)
# pf.show_model(printed_models)
#
# from printing_functions import *
# make_car('hyundai', 'genesis g80', color='black', technology='EV')
