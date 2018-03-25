'''
GameState
The gameState will be used to keep track of the current player.

So for instance when you load a character it create a gameState(character object) and draw that info.
Whenever we need to pull data we just go gameState.inventory to see what items they have, possibly add gameState.searchInventory("sword"), etc
'''
from character import *

class Gamestate:  
    def __init__(self,playerobject):
        
        self.player = playerobject.name
        tmp = []
        for i in playerobject.stats:
            if i not in ",":
                tmp.append(int(i))
        self.playerStats = tmp
        self.playerInventory = playerobject.inventory
        self.location = None

    def displayStats(self):
        stats = ["Strength", "Speed", "Durability", "Intelligence"]
        statsLevels = [0,0,0,0]
        print("Stats for {}:".format(self.name))
        for i, value in enumerate(stats):
            print("[{}] {}: {}".format(i, value, statsLevels[i]))

#hello = gameState()

    
        