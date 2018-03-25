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
from character import *
from gameState import *
from location import *

import numpy as np
 
#TODO Edit statsLevles in main.py to reflect gameState.
#TODO Finish the basic gameState class and functions. 

#TODO FINISH HUB 3/26
#TODO CREATE LOCATION/ MAP FUNCTION 3/27
#TODO CREATE EQUIPMENT CHANGING 3/28
#TODO ADD LEVELS, XP, GOLD 3/29
#TODO Merge leveling, xp, gold to gameState.


##INITS
#Library file for data of characters and enemy classes.
def load(file):
    with open(file) as file:
        return [line.split() for line in file]
        
def loadEnemies():
    lines = load("enemies.txt")
    return [Enemy(x[0], x[1], x[2], np.random.rand(1)) for x in lines]

#Returns a list [[Armors],[Weapons]]
#Access armors by items[0] and weapons through items[1]. 
def loadItems():
    weapon = load("weapons.txt")
    armor = load("armors.txt")
    return [[Armor(x[0], x[1], x[2]) for x in armor], [Weapon(y[0], y[1], y[2], y[3]) for y in weapon]]

def loadCharacters():
    lines = load("characters.txt")
    return [Character(x[0], x[1], x[2]) for x in lines]
    
def loadLocations():
    lines = load("locations.txt")
    return [Location(x[0], x[1], x[2]) for x in lines]

def loadPerks():
    lines = load("perks.txt")
    return [Perks(x[0]. x[1]) for x in lines]
    
enemies = loadEnemies()
items = loadItems()
characters = loadCharacters()
locations = loadLocations()
perks = loadPerks()

#Creates a gameState with a blank character class.
#Primary use is for providing us with a template when starting a new game.
#If we load in a game, it's overwritten anyways.
#If we find an alternative to this I am all for it.
default = Character("Default","0,0,0,0",[])
gamestate = Gamestate(default)

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
    choice = int(input("Please pick an option!\n"))
    while choice not in [0, 1, 2, 3]:
        print("[0]New Game\n[1]Load Character\n[2]View Achievements\n[3]Quit")
        choice = int(input("Please pick an option from the above!\n"))
    if choice == 0:
        newGame()
    elif choice == 1:
        loadGame()
    elif choice == 2:
        viewAchievements()
    else:
        quitGame()

'''
Ask user to create a name for their character. If name is already in
characters, ask them to try another name. 

Asks you which attributes to put 10 skill points into and then creates
your new character object. It displays the character info
and asks you to confirm it. When you say yes the character object is backed 
up to characters.txt
'''
def newGame():
    global gamestate
    while True:
        name = input("Enter a name for your new character:\n")
        while True:
            for i in range(len(characters)):
                if characters[i][0] == name:
                    print("That name is alrady taken! Please try another!")
                    name = input("Enter a name for your new character:\n")
                    break
            break
        print("Why hello there {}!".format(name))
        print("Please choose one of the follow skills to put points into.")
        points = 3
        while points > 0:
            print("Points to spend: {}".format(points))
            gamestate.displayStats()
            addedPoint = int(input("Enter the number of the skill you want to upgrade:\n"))
            while addedPoint not in [range(len(gamestate.stats)-1)]:
                addedPoint = int(input("Please enter the number of the skill you want to upgrade:\n"))
            gamestate.stats[addedPoint] += 1
            points -= 1

        gamestate.displayStats()
        confirm = input("Please confirm your info! (Y/N)")
        while confirm.lower() not in "yn":
            gamestate.displayStats()
            confirm = input("Please confirm your info! (Y/N)")
        if confirm.lower() == "y":
            tmpCharacter = Character(name, gameState.stats, [])
            characters.append(tmpCharacter)

            gamestate = gameState(tmpCharacter)
            save()
            break
    hub()
        

''''
Displays a list of saved characters. If none exist it prompts you to create one.
Once your character is loaded you move to the hub where you can:
- choose location (based on level)
- change out euipment
- shop
- visit the library (lore is stored here)
'''
def loadGame():
    global gamestate
    print("Here are your saved characters:")
    for i, value in enumerate(characters):
        print("[" + str(i) + "] " + value.name)
    choice = int(input("Please select the character you wish to load:\n"))
    while choice not in range(len(characters)):
        choice = int(input("Please select the character you wish to load:\n"))
    gamestate = Gamestate(characters[choice])
    #gamestate should have the proper stats levels, name, and invetory.
    #Add in inventory loading later. 
    hub()
   
'''
Defined achievements the user can earn. Some might come with rewards.
'''
def viewAchievements():
    print("Achievements are coming soon! :)")
    menu()
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
    print("Welcome to the hub, {}!".format(gamestate.player))
    print("[0] Go on an adventure\n[1] Equipment\n[2] Shop\n[3] Library")
    choice = int(input("What would you like to do?\n"))
    while choice not in [0, 1, 2, 3]:
        print("[0] Go on an adventure\n[1] Equipment\n [2] Shop\n [3] Library")
        choice = int(input("Please pick an option from the above!\n"))
    if choice == 0:
        pass
        #Open Adventure Map
        #Has a back button on it to hub. 
    elif choice == 1:
        pass
        #Open inventory to list Armor/Weapons
        #When you go into either category you can see name and stats.
        #If you choose to equip an item it will show how your stats change.
        #All the choices have a back option.
    elif choice == 2:
        pass
        #Takes you to the shop.
        #Items are unlocked through leveling, achievements, and other stuff.
        #To buy an item you need gems which are earned from adventures.
    else:
        pass
        #The library menu will show all the books you currently own. 
        #A book interface will let you flip the page left, right, or go back.
    
'''
Menu takes user input and then goes from there. 
'''
def start():
    menu()

##SAVE 
#TODO Edit save to take data from gameState instead
'''
Take current inventory of character, experience, light, levels, etc
and save it to the character file under their name.
'''
def save():
    with open("characters.txt", "w") as f: 
        for i in characters:
            f.write("\"" + str(i.name) + "\"" + " " + i.stats + " " + i.inventory)
            f.write("\n")
    
def quitGame():
    pass

##ONSTART
start()