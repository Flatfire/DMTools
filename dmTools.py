"""
A series of tools designed to speed up on the fly DM tasks
"""

from random import randint
from dmMenu import dmMenu

def enemy_init():
    """
    Randomly generates initiative roles for x number of enemies
    based on 1d20
    """
    # The documentation above is what gets displayed when the user calls for help from the menu
    valid = False
    while valid is False:
        try:
            eNum = int(input("Enter number of enemies: "))
            valid = True
        except:
            print("Please enter a valid integer")
    eArr = []
    for i in range(eNum):
        eArr.append(diceRoller(20))
    eArr.sort()
    for i in range(len(eArr)):
        print("Enemy {}: {}".format(i+1, eArr[i]))

def rollDieMenu():
    """Select a dice to roll"""
    #Menu options for dice rolls
    #TODO implement a custom dice roll
    dieArr = [[printRoll,"Roll a d20", [20]],[printRoll,"Roll a d12", [12]],[printRoll,"Roll a d10", [10]],[printRoll,"Roll a d8", [8]]
    ,[printRoll,"Roll a d6", [6]],[printRoll,"Roll a d4", [4]],[printRoll,"Roll a d100", [100]]]
    dmMenu(dieArr)

def printRoll(dice):
    print("Your roll is: ",diceRoller(dice))

def diceRoller(dice):
    """Rolls a dice of your choosing"""
    #Designed to accomodate static and custom dice rolling. 
    roll = randint(1,dice)
    return roll
# More functions can be added, just be sure to add them to the array in the menu if you use them with dmMain.py