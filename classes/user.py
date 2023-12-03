"""A class that can be used to represent a user."""


class User():
    """An attempt to describe user."""

    def __init__(self, first_name, last_name, birthdate, birthplace, position):
        """Initialize attributes of a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.position = position
        self.login_attempts = 0

    def describe_user(self):
        """Print the summary description of a user."""
        print("Full name: " + self.first_name.title() + ' ' + self.last_name.title())
        print("Birthdate: " + self.birthdate.title())
        print("Birthplace: " + self.birthplace.title())
        print("Position: " + self.position.title())

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print("Hello, " + self.first_name.title() + ' ' + self.last_name.title() + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0