"""
This module contains the Image model.
"""

from datetime import datetime

class Image:
    """
        A class to represent an image.
        :param id: int
        :param name: str
        :param format: str
        :param size: int
        :param created_at: datetime
    """

    def __init__(self, id, name, format, size):
        self.id = id
        self.name = name
        self.format = format
        self.size = size
        self.created_at = datetime.now()

    def __str__(self):
        return f'Image: {self.name}'

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_format(self):
        return self.format

    def get_size(self):
        return self.size

    def get_created_at(self):
        return self.created_at
