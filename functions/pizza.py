def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# Practice
def make_pizzas(size, *toppings):
    """Summarize the pizza we are about to make."""
    if len(toppings) == 1:
        print("\nMake a " + str(size) + "-inch pizza with the following topping:")
        for topping in toppings:
            print("- " + topping.title())
        print("")
    else:
        print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
        for topping in toppings:
            print("- " + topping.title())
        print("")



