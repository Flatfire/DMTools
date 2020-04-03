"""
Menu system for DM Tool access
"""

from dmTools import *
from dmMenu import dmMenu

# Edit this array to add more menu items. The format is (function, function description).
# The function description is not the same as your function documentation. It should be the menu descriptor.
toolArr = [[enemy_init,"Roll Enemy Initiative"], [rollDieMenu, "Roll A Dice"]]

while True:
    dmMenu(toolArr)