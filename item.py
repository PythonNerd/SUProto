'''

SU Game Prototype
Item class
Armor and Weapons inherit from Item.

Add methods
'''

#TODO Add Methods
class Item:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
    
    
class Armor(Item):
    def __init__(self, name, rarity, health):
        self.name = name
        self.rarity = rarity
        self.health = health
    
class Weapon(Item):
    def __init__(self, name, rarity, level, damage):
        self.name = name
        self.rarity = rarity
        self.level = level
        self.damage = damage
    
        