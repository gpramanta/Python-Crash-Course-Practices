# CLASSES

# Creating and Using a Class
# Creating the Dog Class

# class Dog():    # 1
#     """A simple attempt to model a dog."""      # 2
#
#     def __init__(self, name, age):      # 3
#         """Initialize name and age attributes."""
#         self.name = name    # 4
#         self.age = age
#
#     def sit(self):      # 5
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Simulate a dog rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")

# Making an Instance from a Class
# class Dog():
#     """A simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is sitting.")
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
#
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
#

# Practice
# class Cat():
#     """A simple attempt to model a cat."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a cat sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Simulate a cat rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")
#
#
# my_cat = Cat('oyen', 25)
# print("My cat's name is " + my_cat.name.title() + ".")
# print("My dog is " + str(my_cat.age) + " years old.")

# Calling Methods
# class Dog():
#     """A simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in respond to a command."""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Simulate a dog rolling over in respond to a command."""
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
# my_dog.sit()
# my_dog.roll_over()

# Creating Multiple Instances
# class Dog():
#     """A simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Simulate a dog rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucie', 3)
#
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
#
# print("\nYour dog's name is " + your_dog.name.title() + ".")
# print("Your dog is " + str(your_dog.age) + " years old.")
# your_dog.sit()

# Try It Yourself
# 9-1. Restaurant:
# class Restaurant():
#     """An attempt to display description of a restaurant."""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize the name of restaurant and its cuisine type."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Display description of the restaurant."""
#         print(self.restaurant_name.title() + " serves healthy and delicious foods.")
#
#     def open_restaurant(self):
#         """Display the open message."""
#         print("My " + self.restaurant_name.title() + " is now open! Come and enjoy our authentic " +
#               restaurant.cuisine_type.title() + " cuisine.")
#
#
# restaurant = Restaurant('warung mrengos', 'Balinese')
# print(restaurant.restaurant_name.title() + " was opened by Komang Pramanta Gerinata since yesterday.")
# print("The restaurant serves " + restaurant.cuisine_type.title() + " cuisines.")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9-2. Three Restaurants:
# class Restaurant():
#     """An attempt to display information about my restaurant."""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize the name of restaurant and its type of cuisine."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Display the description of restaurant."""
#         print(self.restaurant_name.title() + " serves healthy and delicious " + self.cuisine_type.title()
#               + " cuisine.")
#
#     def open_restaurant(self):
#         """Display the open message."""
#         print(self.restaurant_name.title() + " is now open! Come and enjoy our authentic " +
#               self.cuisine_type.title() + " cuisine.")
#
#
# restaurant = Restaurant('warung mrengos', 'balinese')
# restaurant.describe_restaurant()
# restaurant = Restaurant('shenzen restaurant', 'chinese')
# restaurant.describe_restaurant()
# restaurant = Restaurant('jay sri rama restaurant', 'indian')
# restaurant.describe_restaurant()

# 9-3. Users:
# class User():
#     """An attempt to create a profile."""
#
#     def __init__(self, first_name, last_name, place, birth_date, occupation):
#         """Initialize first and last names for a profile."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.place = place
#         self.birth_date = birth_date
#         self.occupation = occupation
#
#     def describe_user(self):
#         """Display summary description of a user."""
#         print("Full Name: " + self.first_name.title() + ' ' + self.last_name.title())
#         print("Place: " + self.place.title())
#         print("Birthdate: " + self.birth_date.title())
#         print("Occupation: " + self.occupation.title())
#
#     def greet_user(self):
#         """Display greeting message to the user."""
#         print("Hello, " + self.first_name.title() + ' ' + self.last_name.title() + "!\n")
#
#
# user_1 = User('komang', 'pramanta', 'gianyar', 'december 8th, 1996', 'finance advisor & programmer.')
# user_1.describe_user()
# user_1.greet_user()
#
# user_2 = User('john', 'joseph', 'alachua', 'october 3rd, 1962', 'singer & writer')
# user_2.describe_user()
# user_2.greet_user()
#
# user_3 = User('james', 'paul mccartney', 'london', 'june 18th, 1942', 'musician')
# user_3.describe_user()
# user_3.greet_user()

# Working with Classes and Instances
# The Car Class
# class Car():
#     """A simple attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make.title()
#         self.model = model.title()
#         self.year = year
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# Practice
# class Car():
#     """An attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attempt to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#
# my_new_car = Car('hyundai', 'genesis g80', 2021)
# print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute
# class Car():
#
#     def __init__(self, make, model, year):
#         """Initialize attempt to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         full_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return full_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# Practice
# class Car():
#     """An attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def describe_car(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#
# my_new_car = Car('hyundai', 'genesis g80', 2021)
# print(my_new_car.describe_car())
# my_new_car.odometer()

# Modifying Attribute Values
# Modifying an Attribute’s Value Directly
# class Car():
#     """An attempt to describe a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " on it.")
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# Practice:
# class Car():
#     """An attempt to describe a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#
# my_new_car = Car('tesla', 'y', 2020)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 9
# my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
# class Car():
#     """An attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# Practice:
# class Car():
#     """An attempt to describe a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         if self.odometer_reading > 1:
#             print("This car has " + str(self.odometer_reading) + " miles on it.")
#         else:
#             print("This car has " + str(self.odometer_reading) + " mile on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
# my_new_car = Car('tesla', 'y', 2020)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(1)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(0)

# Incrementing an Attribute’s Value Through a Method
# class Car():
#     """An attempt to describe a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         if self.odometer_reading > 1:
#             print("This car has " + str(self.odometer_reading) + " miles on it.")
#         else:
#             print("This car has " + str(self.odometer_reading) + " mile on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         if miles < 0:
#             print("You cannot roll back an odometer!")
#         else:
#             self.odometer_reading += miles
#
#
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(-10)

# Try It Yourself
# 9-4. Number Served:
# class Restaurant():
#     """An attempt to describe a restaurant."""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize name of the restaurant and type of cuisine it serves."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """Print description of the restaurant."""
#         print("The " + self.restaurant_name.title() + " was established by Mr. Nata in 2022. It serves " +
#               self.cuisine_type.title() + " cuisine as the main menu but also offers other asian cuisines.")
#
#     def open_restaurant(self):
#         """Print the open restaurant message."""
#         print("The " + self.restaurant_name.title() + " is now open! We offer the best traditional food "
#                                                       "from Asia!")
#
#     def set_number_served(self, customer):
#         """Set the number customers that have been served."""
#         self.number_served = customer
#         print(self.restaurant_name.title() + " serves " + str(self.number_served) +
#               " customers in average per-day.")
#
#     def increment_number_served(self, number):
#         """Increment the number of customers who have been served."""
#         self.number_served += number
#         print("Currently, the " + self.restaurant_name.title() + " restaurant is serving " +
#               str(self.number_served) + " guests!")
#
#
# restaurant = Restaurant('warung mrengos', 'balinese')
# print("I opened " + restaurant.restaurant_name.title() + " in 2022.")
# print("It mainly serves " + restaurant.cuisine_type.title() + " cuisine as the main dishes.")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# restaurant.set_number_served(50)
# restaurant.increment_number_served(50)

# 9-5. Login Attempts:
# class User():
#     """An attempt to represent a user."""
#
#     def __init__(self, first_name, last_name, birthplace, birthdate, interest):
#         """Initialize attributes to describe a user."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birthplace = birthplace
#         self.birthdate = birthdate
#         self.interest = interest
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """Print a summary of the user's information."""
#         print("First name: " + self.first_name.title())
#         print("Last name: " + self.last_name.title())
#         print("Birthplace: " + self.birthplace.title())
#         print("Birthdate: " + self.birthdate.title())
#         print("Interest: " + self.interest.title())
#
#     def greet_user(self):
#         """Print a personalized message to the user."""
#         print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!\n")
#
#     def increment_login_attempt(self):
#         """Increment the value of login_attempts by 1."""
#         self.login_attempts += 1
#
#     def reset_login_attempt(self):
#         """Reset the value of login_attempts to 0."""
#         self.login_attempts = 0
#
#
# user = User('pramanta', 'gerinata', 'denpasar', 'december 8th, 1996', 'A.I.')
# user.describe_user()
# user.greet_user()
#
# user = User('john', 'joseph', 'new york', 'october 3rd, 1962', 'music')
# user.describe_user()
# user.greet_user()
#
# user.increment_login_attempt()
# user.increment_login_attempt()
# user.increment_login_attempt()
# print(user.login_attempts)
#
# user.reset_login_attempt()
# print(user.login_attempts)

# Inheritance
# The __init__() Method for a Child Class
# class Car():
#     """A simple attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

# Practice
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """Represent aspect of a car, specific to electric vehicles."""
#
#     def __init__(self, make, model, year):
#         """Initiate attributes of the parent class."""
#         super().__init__(make, model, year)
#
#
# my_hyundai = ElectricCar('hyundai', 'genesis g80', 2022)
# print(my_hyundai.get_descriptive_name())

# Defining Attributes and Methods for the Child Class
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """Represent aspect of a car, specific to electric vehicles."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
#
# my_tesla.describe_battery()

# Practice
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicle."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 87.2
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# my_hyundai = ElectricCar('hyundai', 'genesis g80', 2022)
# print(my_hyundai.get_descriptive_name())
# my_hyundai.describe_battery()
#
# my_hyundai.update_odometer(128)
# my_hyundai.read_odometer()

# Overriding Methods from the Parent Class
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         print("Fill the gas tank.")
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicle."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 87.2
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def fill_gas_tank(self):
#         print("Electric car does not have gas tank.")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()

# Instances as Attributes
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=70):
#         """Initialize the battery attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicle."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

# Continue from above
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=70):
#         """Initialize the battery attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         range = ''
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#
#         message = "This car can go approximately " + str(range) + " miles on a full charge."
#         print(message)
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicle."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the present class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# Practice
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=60):
#         """Initialize the battery attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size < 30:
#             range = 90
#         elif self.battery_size <= 60:
#             range = 100
#         else:
#             range = 200
#
#         message = "This car can go approximately " + str(range) + " miles on a full charge."
#         print(message)
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicle."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class. Then Initialize attributes specific to an electric
#         car."""
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#
# my_hyundai = ElectricCar('hyundai', 'genesis g80', 2022)
# print(my_hyundai.get_descriptive_name())
# my_hyundai.battery.describe_battery()
# my_hyundai.battery.get_range()

# Try It Yourself
# 9-6. Ice Cream Stand:
# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + " was established in 2022 by Pramanta. The restaurant mainly "
#                                              "served " + self.cuisine_type.title() + " cuisines.")
#
#     def open_restaurant(self):
#         print("The " + self.restaurant_name.title() + " restaurant is open today! Come and enjoy our "
#                                                       "delicious traditional foods.")
#
#     def set_number_served(self, customer):
#         self.number_served = customer
#
#     def increment_number_served(self, number):
#         self.number_served += number
#
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['banana', 'chocolate', 'vanilla']
#
#     def display_flavors(self):
#         print("The top three " + self.restaurant_name.title() + "'s flavors:")
#         for flavor in self.flavors:
#             print("- " + flavor.title())
#
#
# my_stand = IceCreamStand('mrengos ice cream', 'ice cream')
# my_stand.display_flavors()

# 9-7. Admin:
# class User():
#
#     def __init__(self, first_name, last_name, birthplace, birthdate, position, interests):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birthplace = birthplace
#         self.birthdate = birthdate
#         self.position = position
#         self.interests = interests
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("Full name: " + self.first_name.title() + ' ' + self.last_name.title())
#         print("Place of birth: " + self.birthplace.title())
#         print("Date of birth: " + self.birthdate.title())
#         print("Position: " + self.position.title())
#         print("Interests: " + self.interests)
#
#     def greet_user(self):
#         print("Hello, " + self.first_name.title() + ' ' + self.last_name.title() + "!")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Admin(User):
#
#     def __init__(self, first_name, last_name, birthplace, birthdate, position, interests):
#         super().__init__(first_name, last_name, birthplace, birthdate, position, interests)
#         self.privileges = ['can add post', 'can delete post', 'can ban user', 'can recommend post']
#
#     def show_privileges(self):
#         print("\nThis is administrator's set of privileges:")
#         for privilege in self.privileges:
#             print("- " + privilege.title())
#
#
# admin = Admin('geri', 'nata', 'denpasar', 'december 8th, 1996', 'administrator', 'music')
# admin.describe_user()
# admin.show_privileges()

# Second Version (The best so far) 9-7. Admin:
# class User():
#     """An attempt to describe user."""
#
#     def __init__(self, first_name, last_name, birthdate, birthplace, position):
#         """Initialize attributes of a user."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birthdate = birthdate
#         self.birthplace = birthplace
#         self.position = position
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """Print the summary description of a user."""
#         print("Full name: " + self.first_name.title() + ' ' + self.last_name.title())
#         print("Birthdate: " + self.birthdate.title())
#         print("Birthplace: " + self.birthplace.title())
#         print("Position: " + self.position.title())
#
#     def greet_user(self):
#         """Print a personalized greeting to the user."""
#         print("Hello, " + self.first_name.title() + ' ' + self.last_name.title() + "!")
#
#     def increment_login_attempts(self):
#         """Increment the value of login_attempts by 1."""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         """Reset the value of login_attempts to 0."""
#         self.login_attempts = 0
#
#
# class Admin(User):
#     """An attempt to describe administrator."""
#
#     def __init__(self, first_name, last_name, birthdate, birthplace, position):
#         """Initialize attributes of administrator."""
#         super().__init__(first_name, last_name, birthdate, birthplace, position)
#         self.privileges = ['Can add post', 'Can delete post', 'Can ban user', 'Can pin a post', 'Can add new user']
#         self.privileges = Privileges()
#
#
# class Privileges():
#     """An attempt to describe list of privileges."""
#
#     def __init__(self):
#         """Initialize attribute of administrator's set of list."""
#         self.privileges = ['Can add post', 'Can delete post', 'Can ban user', 'Can pin a post', 'Can add new user']
#
#     def show_privileges(self):
#         """Print the list of administrator's set of privileges."""
#         print("Below is the administrator's set of privileges:")
#         for privilege in self.privileges:
#             print("- " + privilege)
#
#
# admin = Admin('komang', 'pramanta', 'december 8th, 1996', 'denpasar', 'administrator')
# admin.privileges.show_privileges()

# 9-9. Battery Upgrade:
# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cannot roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         range = ''
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#
#         message = "This car can go approximately " + str(range) + " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#
#
# class ElectricCar(Car):
#
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#
# my_car = ElectricCar('tesla', 'model s', 2016)
# print(my_car.get_descriptive_name())
# my_car.battery.describe_battery()
# my_car.battery.get_range()
#
# my_car.battery.upgrade_battery()
# my_car.battery.get_range()

# The other sections are moved to my_car.py

# Try It Yourself
# 9-10. Imported Restaurant:
# from restaurant import Restaurant
#
# my_restaurant = Restaurant('mrengos', 'russian')
# my_restaurant.describe_restaurant()

# 9-11. Imported Admin:
# from user import Admin
#
# admin = Admin('komang', 'pramanta', 'december 8th, 1996', 'denpasar', 'administrator')
# admin.privileges.show_privileges()

# 9-12. Multiple Modules:
# from privilegesadmin import Admin
#
# admin = Admin('komang', 'pramanta', 'december 8th, 1996', 'denpasar', 'administrator')
# admin.privileges.show_privileges()

# The Python Standard Library
# from _collections import OrderedDict
#
# favorite_languages = OrderedDict()
#
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# Practice
# from _collections import OrderedDict
#
# favorite_languages = OrderedDict()
#
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
#
# print("Here are the programming languages that people like:")
# for person, language in favorite_languages.items():
#     print("- " + person.title() + " likes " + language.title() + " programming language.")

# Try It Yourself
# 9-13. OrderedDict Rewrite:
# from _collections import OrderedDict
#
# python_terms = OrderedDict()
#
# python_terms['string'] = "A string is simply a series of characters."
# python_terms['float'] = "Python calls any number with a decimal point a float."
# python_terms['list'] = "A list is a collection of items in a particular order."
# python_terms['for loop'] = "When you want to do the same action with every item in a list, you can use Python’s for " \
#                            "loop."
# python_terms['tuples'] = "a list of items that cannot change."
# python_terms['dictionary'] = "A dictionary in Python is a collection of key-value pairs."
# python_terms['key'] = "Each key is connected to a value, and you can use a key to access the value associated with " \
#                       "that key. A key’s value can be a number, a string, a list, or even another dictionary."
# python_terms['key-value pair'] = "A key-value pair is a set of values associated with each other."
# python_terms['if-elif-else'] = "Often, you’ll need to test more than two possible situations, and to evaluate these " \
#                                "you can use Python’s if-elif-else syntax."
#
# print("Below is the list of Python terms:\n")
# for term, meaning in python_terms.items():
#     print(term.title() + "\n- " + meaning + "\n")

# 9-14. Dice:
# from random import randint
#
#
# class Die():
#     """An attempt to display the sides of dice."""
#
#     def __init__(self, sides):
#         """Initialize attributes of dice."""
#         self.sides = sides
#
#     def roll_die(self):
#         """Print a random number between 1 and the number of sides the die has."""
#         die = randint(1, self.sides)
#         print(die)
#
#
# my_die = Die(6)
# my_die.roll_die()
#
# my_die = Die(10)
# my_die.roll_die()
#
# my_die = Die(20)
# my_die.roll_die()

# TEST
class dog():
    """An effort to describe a dog."""

    def __init__(self, name, age):
        """Initialize attributes of a dog."""
        self.name = name
        self.age = age

    def sit_down(self):
        """Instructing the dog to sit down."""
        print(self.name.title() + ", sit down!")

    def roll_over(self):
        """Instructing the dog to roll over."""
        print(self.name.title() + ", rolled over!")


my_dog = dog('eli', 3)
my_dog.sit_down()
my_dog.roll_over()