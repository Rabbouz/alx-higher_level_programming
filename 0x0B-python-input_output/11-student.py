#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        return self.__dict__
    
    def reload_from_json(self, json):
        for s, d in json.items():
            setattr(self, s, d)
