# def make_pizza(size, *toppings):
#     """Display description of a pizza."""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping.title())
#
#
# def build_profile(first_name, last_name, **arbitrary):
#     """Display description of a person in dictionary form."""
#     dictionary = {}
#     dictionary['first name'] = first_name
#     dictionary['last name'] = last_name
#     for key, value in arbitrary.items():
#         dictionary[key] = value
#     print(dictionary)
#     return dictionary
#
#
def make_car(manufacturer, model, **arbitrary):
    dictionary = {}
    dictionary['manufacturer'] = manufacturer.title()
    dictionary['model'] = model.title()
    for key, value in arbitrary.items():
        dictionary[key] = value
    print(dictionary)
    return dictionary


