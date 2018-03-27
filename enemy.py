'''

SU Game Prototype
Enemy class
Rng will determine if they drop any assortment of items from
the items file.

Add methods
'''
import numpy as np
from numpy.matlib import rand


class Enemy:
    def __init__(self, name, health, damage, rng, evasion, accuracy, level):
        self.name = name
        self.health = health
        self.damage = damage
        self.rng = rng
        self.evasion = evasion
        self.accuracy = accuracy
        self.level = level
    
    def attack(self, hero_evasion, hero_health):
        if self.accuracy >= hero_evasion:
            hero_health -= self.damage
            print(self.name + " has dealt " + self.damage + "!")
        else:
            print("The hero has dodged it!")
        return hero_health

    def dodge(self, hero_accuracy, dmg_dealt_by_hero):

        #Work more on the dodgeRate!
        dodgeRate = (self.evasion * np.random.randint(1, 6)) / hero_accuracy
        if np.random(rand(1)) > (1 - dodgeRate):
            print(self.name+" dodged it!")
        else:
            self.health -= dmg_dealt_by_hero
            print(dmg_dealt_by_hero + " damage has been inflicted!")
        return self.health

