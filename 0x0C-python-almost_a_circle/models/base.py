#!/usr/bin/python3
import json
import csv
import turtle


class Base:
    """Base class.
    The 'base' class is represented as a parent for all other classes in this project
    
    Private class attribute:
    __nb_object(int): instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base
        args:
        id(int): identity of the bew base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        