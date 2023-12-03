# Importing Classes
# Importing a Single Class

# from car import Car
#
# my_car = Car('audi', 'a4', 2016)
# print(my_car.get_descriptive_name())
#
# my_car.odometer_reading = 23
# my_car.read_odometer()

# Storing Multiple Classes in a Module
# from car import ElectricCar
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# Importing Multiple Classes from a Module
# from car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

# Importing an Entire Module
# import car
#
# my_beetle = car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

# Importing a Module into a Module
# from car import Car
# from electric_car import ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


