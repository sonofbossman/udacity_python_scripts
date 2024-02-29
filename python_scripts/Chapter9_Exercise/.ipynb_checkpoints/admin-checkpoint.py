from users import User

"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("You are an admin and you can do the following:")
        for privilege in self.privileges:
            print(privilege)

"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.rights = Privileges()

    # def show_privileges(self):
    #     print("You are an admin and you can do the following:")
    #     for privilege in self.privileges:
    #         print(privilege)



if __name__=="__main__":
    admin = Admin("Tunde", "Akingbade", "can add post", "can delete post", "can ban user")
    admin.rights.show_privileges()