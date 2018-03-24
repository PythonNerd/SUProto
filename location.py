'''

SU Game Prototype
Locations

Add methods
'''

#TODO Brainstorm what locations can have besides a difficulty.
#TODO Attach lore to a location? Unlock items found only in it?


class Location:
    def __init__(self, name, level, rng):
        self.name = name
        self.level = level
        self.rng = rng
        