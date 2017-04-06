#!/usr/bin/env python

class Animal:
    def __init__(self, family):
        print('A new animal is born!')
        self.family=family

    def print_name(self):
        print(this.family)

    def change_name(family):
        self.family = family


''' 
This should output:
    tiger
    bear

What is wrong? 
'''

tiger = Animal('tiger')
tiger.print_name()
tiger.change_name('bear')
tiger.print_name()
