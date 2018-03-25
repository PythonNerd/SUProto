'''
GameState
The gameState will be used to keep track of the current player.

So for instance when you load a character it create a gameState(character object) and draw that info.
Whenever we need to pull data we just go gameState.inventory to see what items they have, possibly add gameState.searchInventory("sword"), etc
'''
class gameState:
    def __init__(self, playerOjbect=Character("",[0,0,0,0],[])):
        self.player = playerObject.name
        tmp = []
        for i in playerObject.stats:
            if i not in ",":
                tmp.append(int(i))
        self.playerStats = tmp
        self.playerInventory = playerObject.inventory
        self.location = None
        
    def displayStats(self):
        stats = ["Strength", "Speed", "Durability", "Intelligence"]
        statsLevels = [0,0,0,0]
        print("Stats for {}:".format(self.name))
        for i, value in enumerate(stats):
            print("[{}] {}: {}".format(i, value, statsLevels[i]))
    
        