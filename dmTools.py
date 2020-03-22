"""
A series of tools designed to speed up on the fly DM tasks
"""

from random import randint

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
        eArr.append(randint(1,20))
    for i in range(len(eArr)):
        print("Enemy {}: {}".format(i+1, eArr[i]))

# More functions can be added, just be sure to add them to the array in the menu if you use them with dmMain.py