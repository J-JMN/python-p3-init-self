#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed=None):
        '''takes a name as an argument and saves it to self.name'''
        self.name = name
        '''takes a breed as an argument and saves it to self.breed'''
        self.breed = breed
        '''sets self.breed = "Mutt" when no breed specified'''
        if not breed:
            self.breed = "Mutt"
