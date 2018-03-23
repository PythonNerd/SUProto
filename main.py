'''
SU Game Prototype
-- INITS
----Load enemies, items, characters, locations, perks
-- ENGINE
----Calculates actions, rng, variables. Handles user inputs.
-- GAME
----Running the actual game. You create your character, 
----assign 10 points to skills, then choose a location to delve into.
----Each location will have a random number of areas to clear and enemies in them.
----Locations will have difficulty and this will be used to spawn harder enemies.
----After clearing an area you return to the hub with your new loot.
-- SAVE
----Character info is backed up so next time you play you have your data.

Add a story / campaign mode.
'''
from enemy import *
import numpy as np

##INITS
#Library file for data of characters and enemy classes.
def loadEnemies():
    with open("enemies.txt") as file:
        lines = [line.strip() for line in file]
        return [Enemy(x[0], x[1], x[2], np.random.rand(1)) for x in lines]

enemies = loadEnemies()

def loadItems():
    pass
    
def loadCharacters():
    pass
    
def loadLocations():
    pass
    
def loadPerks():
    pass
    
##ENGINE
'''
RNG

For RNG we will check if value > .50 for commons, then > .49 for legendaries, 
> .30 for rares, and > .05 for uncommons.

Items will have their own list.
'''

##GAME
'''
Menu
New Game - Create a new character.
Load Character - Play an existing character. A list of characters will be displayed and their levels. 
View Achievements - Coming soon ;)
Quit - Save and quit.
'''
def menu():
    print("Welcome to Game!")
    print("[0]New Game\n[1]Load Character\n[2]View Achievements\n[3]Quit")
    choice = input("Please pick an option!\n")


def start():
    #Bring up menu and take user input.
    menu()
    #Use user input to open that next choice.
    
    #If user is going to a location



##SAVE 










##ONSTART
start()