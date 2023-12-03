"""A set of classes that can be used to represent administrator."""

from user import User


class Admin(User):
    """An attempt to describe administrator."""

    def __init__(self, first_name, last_name, birthdate, birthplace, position):
        """Initialize attributes of administrator."""
        super().__init__(first_name, last_name, birthdate, birthplace, position)
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user', 'Can pin a post', 'Can add new user']
        self.privileges = Privileges()


class Privileges():
    """An attempt to describe list of privileges."""

    def __init__(self):
        """Initialize attribute of administrator's set of list."""
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user', 'Can pin a post', 'Can add new user']

    def show_privileges(self):
        """Print the list of administrator's set of privileges."""
        print("Below is the administrator's set of privileges:")
        for privilege in self.privileges:
            print("- " + privilege)