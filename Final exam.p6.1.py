# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:19:35 2016

@author: WenChen
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Person.say(self, stuff)
    def lecture (self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)