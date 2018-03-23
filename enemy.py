'''

SU Game Prototype
Enemy class
Rng will determine if they drop any assortment of items from
the items file.
'''
class Enemy:
    def __init__(self, name, health, damage, rng):
        self.name = name
        self.health = health
        self.damaeg = damage
        self.rng = rng
    
    def attack(self):
        print("it works!")
        