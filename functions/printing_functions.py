# def make_model(unprinted_models, printed_models):
#     """Simulate printing each design, until none are left. Move each design to printed_models after printing."""
#     while unprinted_models:
#         current_model = unprinted_models.pop()
#         print("Printing model: " + current_model.title())
#         printed_models.append(current_model)
#
#
# def show_model(printed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for model in printed_models:
#         print(model.title())
#     print("")
#
#
# def make_car(manufacturer, model, **specifications):
#     """Build a dictionary containing everything we know about a car."""
#     dictionary = {}
#     dictionary['Manufacturer'] = manufacturer.title()
#     dictionary['model'] = model.title()
#     for key, value in specifications.items():
#         dictionary[key] = value
#     print(dictionary)
#     return dictionary
#
#
