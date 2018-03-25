'''

SU Game Prototype
Character
Has perks too.

Add methods
'''

#TODO Handle Leveling in the Character based on a XP system
#Add XP from battles, lore, etc
#Edit display stats to take info from the actual stats instead of placeholders.
#Character inventory will be ids of the items, so we can easily store space.

class Character:
    def __init__(self, name, stats, inventory):
        self.name = name
        self.stats = stats
        self.inventory = inventory
        
    def displayStats(self):
        stats = ["Strength", "Speed", "Durability", "Intelligence"]
        statsLevels = [0,0,0,0]
        print("Stats for {}:".format(self.name))
        for i, value in enumerate(stats):
            print(value + ":     " + str(statsLevels[i]))
        
class Perk:
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
        
