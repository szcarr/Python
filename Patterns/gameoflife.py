import os
import random
import time

coordinates = {}

def main(**kwargs):

    '''
    V1.0
    main(Height=50, Width=100, Deadtile = "0", Alivetile = "!", Update=1.5)

    Kwargs is:

    Height = <Integer>  # Sets the width of the game
    Heigt = <Integer>  # Sets the height of the game
    Deadtile = <String> # Sets deadtiles as any char or string
    Alivetile = <String> # Sets alivetile as any char or string
    Update = <Integer> # Sets time before "game" updates to next frame
    Verbose = <Boolean> # Toggles more info
    '''

    global deadtile, alivetile, height, width, verbose, minimum, maximum

    deadtile = "0"
    alivetile = "1"

    height = 40
    width = 40

    update = 1
    verbose = True

    minimum = None
    maximum = None

    for k in kwargs:
        if k == "height":
            height = kwargs.get(k)
        elif k == "width":
            width = kwargs.get(k)
        elif k == "deadtile":
            deadtile = kwargs.get(k)
        elif k == "alivetile":
            alivetile = kwargs.get(k)
        elif k == "update":
            update = kwargs.get(k)
        elif k == "verbose":
            verbose = kwargs.get(k)
        elif k == "minimum":
            minimum = kwargs.get(k)
        elif k == "maximum":
            maximum = kwargs.get(k)

    setup()
    generateRandomValuesForCoordinates(minimum=minimum, maximum = maximum)
    

    counter = 0

    while True:
        print(f"alive {getAliveTiles()}")
        displayGame(counter)
        determineValue()
        print(f"alive {getAliveTiles()}")
        #os.system("cls")
        displayGame(counter)
        time.sleep(update)
        counter += 1

def setup():
    for y in range(height):
        for x in range(width):
            xy = str(x) + " " + str(y) 
            coordinates[xy] = deadtile

def getAliveTiles():
    aliveTiles = 0
    for y in range(height):
        for x in range(width):
            xy = str(x) + " " + str(y) 
            if coordinates.get(xy) == alivetile:
                aliveTiles += 1
    return aliveTiles

def star_pattern():
    coordinates["6 4"] = alivetile
    coordinates["7 4"] = alivetile
    coordinates["8 4"] = alivetile

def generateRandomValuesForCoordinates(**kwargs):

    '''
    Kwargs is:

    Minimum = <Integer>
    Maximum = <Integer>
    '''

    minimum = height * width / 100 * 20
    maximum = height * width / 100 * 40

    for k in kwargs:
        if k == "minimum" and kwargs.get(k) != None:
            minimum = round(kwargs.get(k))
        elif k == "maximum" and kwargs.get(k) != None:
            maximum = round(kwargs.get(k)) 

    amountOfValuesToBeGenerated = random.randrange(minimum, maximum)
    for i in range(amountOfValuesToBeGenerated):
        xy = str(random.randrange(0, width)) + " " + str(random.randrange(0, height))
        coordinates[xy] = alivetile

def getXYValueToInt(coords):
    x = int(coords.split(" ")[0])
    y = int(coords.split(" ")[1])
    return x, y

def determineValue():
    for y in range(height):
        for x in range(width):
            xy = str(x) + " " + str(y)
            aliveNeighbors, deadNeighbors = getNeighborsOf(xy)[0], getNeighborsOf(xy)[1]
            if coordinates.get(xy) == alivetile:
                if aliveNeighbors < 2:
                    coordinates[xy] = deadtile
                elif aliveNeighbors == 2 or aliveNeighbors == 3:
                    coordinates[xy] = alivetile
                elif aliveNeighbors > 3:
                   coordinates[xy] = deadtile 
            else:
                if aliveNeighbors == 3:
                    coordinates[xy] = alivetile

def getNeighborsOf(coords):
    
    offset = [
        "-1 -1", "0 -1", "1 -1",
        "-1 0", "0 0", "1 0",
        "-1 1", "0 1", "1 1",
    ]

    amountOfAliveNeighbors = 0
    amountOfDeadNeighbors = 0
    for i, e in enumerate(offset):
        if i == 4:
            continue
        currentX, currentY = getXYValueToInt(coords)[0] + getXYValueToInt(e)[0], getXYValueToInt(coords)[1] + getXYValueToInt(e)[1]
        k = str(currentX) + " " + str(currentY)
        if coordinates.get(k) == alivetile:
            amountOfAliveNeighbors += 1 
        elif coordinates.get(k) == deadtile:
            amountOfDeadNeighbors += 1
    
    return amountOfAliveNeighbors, amountOfDeadNeighbors

def displayGame(counter):
    for y in range(height):
        for x in range(width):
            xy = str(x) + " " + str(y)
            print(coordinates.get(xy), end=" ")
        print("")
    if verbose:
        print("\n")
        amountOfTiles = width * height
        totalTiles = f"Total tiles: {amountOfTiles}"
        print(totalTiles)
        aliveTiles = f"Alive tiles: {getAliveTiles()}. Percentage of map {round(getAliveTiles() / amountOfTiles * 100, 2)} %."
        print(aliveTiles)
        deadTiles = f"Dead tiles: {amountOfTiles - getAliveTiles()}. Percentage of map {round((amountOfTiles - getAliveTiles()) / amountOfTiles * 100, 2)} %."
        print(deadTiles)
        counter = f"Generation: {counter}"
        print(counter)

    

height = 37
width = 79
deadtile = " "
alivetile = "|"
update = 0.05
minimum = height * width / 100 * 6
maximum = height * width / 100 * 10

main(height=height, width=width, deadtile=deadtile, alivetile=alivetile, update=update, minimum=minimum, maximum=maximum)
