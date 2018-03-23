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
from item import *
import numpy as np

##INITS
#Library file for data of characters and enemy classes.
def load(file):
    with open(file) as file:
        return [line.strip() for line in file]
        
def loadEnemies():
    lines = load("enemies.txt")
    return [Enemy(x[0], x[1], x[2], np.random.rand(1)) for x in lines]

def loadItems():
    #Returns a list [[Armors],[Weapons]]
    #Access armors by items[0] and weapons through items[1]. 
    weapon = load("weapons.txt")
    armor = load("armors.txt")
    return [[Armor(x[0], x[1], x[2]) for x in armor], [Weapon(y[0], y[1], y[2], y[3]) for y in weapon]]

def loadCharacters():
    pass
    
def loadLocations():
    pass
    
def loadPerks():
    pass
    
    
    
enemies = loadEnemies()
items = loadItems()
##ENGINE
'''
RNG

For RNG we will check if value > .50 for commons, then > .49 for legendaries, 
> .30 for rares, and > .05 for uncommons.

Items will have their own list.
'''
def search():
    #Go over a list to search for something. Such as rare weapons to drop,
    #leveled weapons to give enemies, etc.
    pass
    
    
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

'''
Ask user to create a name for their character. If name is already in
characters, ask them to try another name. 

Asks you which attributes to put 10 skill points into and then creates
your new character object. It displays the character info
and asks you to confirm it. When you say yes the character object is backed 
up to characters.txt
'''
def newGame():
    pass
   
''''
Displays a list of saved characters. If none exist it prompts you to create one.
Once your character is loaded you move to the hub where you can:
- choose location (based on level)
- change out euipment
- shop
- visit the library (lore is stored here)
''''
def loadGame():
    pass
   
'''
Described above. This is where you will go after adventures. 
Each call to hub backs up character data too.

Going to a location calls loadLocation(location) in gameengine, which then
builds that location.

Going to equipment brings up a menu that shows what you have equipped, along
with a list of your inventory. Pick a part and swap it out to see your stats
change too.

Going to the shop lets you sell loot or buy new items.

Going to the library will let you browse books that have pages you read. 
Library will be stored in another file for now.
'''
def hub():
    pass
    
    
'''
Menu takes user input and then goes from there. 
'''
def start():
    #Bring up menu and take user input.
    menu()
    #Use user input to open that next choice.



##SAVE 
'''
Take current inventory of character, experience, light, levels, etc
and save it to the character file under their name.
'''
def save():
    pass

##ONSTART
start()