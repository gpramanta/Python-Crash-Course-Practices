"""A class that can be used to represent a restaurant."""


class Restaurant():
    """A simple attempt to describe a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print description of restaurant."""
        print(self.restaurant_name.title() + " restaurant was established in 2022 by Mr. Nata.\nThe restaurant serves "
              + self.cuisine_type.title() + " cuisines.")

    def open_restaurant(self):
        """Print a message telling the restaurant is now open."""
        print(self.restaurant_name.title() + " restaurant is now open. Come and enjoy our authentic delicious foods.")

    def set_number_served(self, customers):
        """Show the number of customers"""
        if customers >= self.number_served:
            self.number_served = customers

    def increment_number_served(self, number):
        """Increment the number of customer served."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """An attempt to describe ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['avocado', 'vanilla', 'chocolate']

    def display_flavors(self):
        """Display the list of ice cream flavors."""
        print("Here is the list of our flavors:")
        for flavor in self.flavors:
            print("- " + flavor.title())
