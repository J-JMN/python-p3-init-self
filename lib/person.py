#!/usr/bin/env python3

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        if not age:
            self.age = 0
