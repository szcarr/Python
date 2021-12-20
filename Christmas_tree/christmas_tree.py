import random
import os
import time
from termcolor import colored

toggleStarOn = True

def createStarTree(width):
    #Width should be an odd number
    #Length should be length = round(width/2)
    middle = round(width / 2)
    length = round(width / 2)
    tree(middle, width, length)
    treeBase(middle, width, length)
    

def tree(middle, width, length):
    global toggleStarOn
    increment = 0
    firstRow = True

    #https://unicode-table.com/en/sets/star-symbols/

    for l in range(length):
        for w in range(width + 1):
            if firstRow and w == middle and toggleStarOn:
                print(colored('\u2605', "yellow"))
                toggleStarOn = False
                firstRow = False
                break
            elif not toggleStarOn and w == middle and firstRow:
                print(colored('\u2606', "yellow"))
                toggleStarOn = True
                firstRow = False
                break
            elif firstRow:
                print(" ", end="")
                continue

            if w >= middle - increment and w <= middle + increment and not firstRow:
                print(colored("*", "green"), end="")
            else:
                print(" ", end="")
        print("")
        increment = increment + 1


def treeBase(middle, width, length):
    baseLength = round(length * 0.15)
    baseWidth = round(width * 0.09)
    for l in range(baseLength):
        for w in range(width):
            if w >= middle - baseWidth and w <= middle + baseWidth:
                print(colored("*", "cyan"), end="")
            else:
                print(" ", end="")
        print("")

def playAnimatedStar(width):
    while True:
        print("\033[H\033[J")
        #os.system('cls')
        createStarTree(width)
        time.sleep(1)

def promptUser():
    print("\nInput should be an odd number.\nInput should be an integer.\nInput should be larger than 5.\n")
    print("\nInput the width of the tree: ")
    width = int(input("> "))
    playAnimatedStar(width)

promptUser()
