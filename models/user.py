"""
This file contains the User class.
"""


class User:
    """
        A class to represent a user.
        :param username: str
        :param password: str
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'User: {self.username}'

    def get_password(self):
        return self.password

    def get_username(self):
        return self.username
