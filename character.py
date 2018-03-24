'''

SU Game Prototype
Character
Has perks too.

Add methods
'''

#TODO Handle Leveling in the Character based on a XP system
#Add XP from battles, lore, etc

class Character:
    def __init__(self, name, stats, inventory):
        self.name = name
        self.stats = stats
        self.inventory = inventory
        
class Perk:
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus