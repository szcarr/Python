import os
import random
import time

coordinates = {}

def main(**kwargs):

    '''

    main(Height=50, Width=100, Deadtile = "0", Alivetile = "!", Update=1.5)

    Kwargs is:

    Height = <Integer>  # Sets the width of the game
    Heigt = <Integer>  # Sets the height of the game
    Deadtile = <String> # Sets deadtiles as any char or string
    Alivetile = <String> # Sets alivetile as any char or string
    Update = <Integer> # Sets time before game goes to next frame
    Verbose = <Boolean> # Toggles more info
    '''

    global Deadtile, Alivetile, Height, Width, Verbose

    Deadtile = "0"
    Alivetile = "1"

    Height = 40
    Width = 40

    Update = 1
    Verbose = True

    for k in kwargs:
        if k == "Height":
            Height = kwargs.get(k)
        elif k == "Width":
            Width = kwargs.get(k)
        elif k == "Deadtile":
            Deadtile = kwargs.get(k)
        elif k == "Alivetile":
            Alivetile = kwargs.get(k)
        elif k == "Update":
            Update = kwargs.get(k)
        elif k == "Verbose":
            Verbose = kwargs.get(k)

    setup()
    generateRandomValuesForCoordinates()
    while True:
        determineValue()
        os.system("cls")
        displayGame()
        time.sleep(Update)

def setup():
    for y in range(Height):
        for x in range(Width):
            xy = str(x) + " " + str(y) 
            coordinates[xy] = Deadtile

def getAliveTiles():
    aliveTiles = 0
    for y in range(Height):
        for x in range(Width):
            xy = str(x) + " " + str(y) 
            if coordinates.get(xy) == Alivetile:
                aliveTiles += 1
    return aliveTiles

def generateRandomValuesForCoordinates(**kwargs):

    '''
    Kwargs is:

    Minimum = <Integer> <- not implemented
    Maximum = <Integer> <- not implemented
    '''
        
    Minimum = Height * Width / 100 * 20
    Maximum = Height * Width / 100 * 40
    
    for k in kwargs:
        if k == "Minimum":
            Minimum = kwargs.get(k)
        elif k == "Maximum":
            Maximum = kwargs.get(k) 

    amountOfValuesToBeGenerated = random.randrange(Minimum, Maximum)
    for i in range(amountOfValuesToBeGenerated):
        xy = str(random.randrange(0, Width)) + " " + str(random.randrange(0, Height))
        coordinates[xy] = Alivetile

def getXYValueToInt(coords):
    x = int(coords.split(" ")[0])
    y = int(coords.split(" ")[1])

    return x, y

def determineValue():
    for y in range(Height):
        for x in range(Width):
            xy = str(x) + " " + str(y)
            aliveNeighbors, deadNeighbors = getNeighborsOf(xy)[0], getNeighborsOf(xy)[1]
            if coordinates.get(xy) == Alivetile:
                if aliveNeighbors < 2:
                    coordinates[xy] = Deadtile
                elif aliveNeighbors > 1 and aliveNeighbors < 4:
                    coordinates[xy] = Alivetile
                elif aliveNeighbors > 3:
                   coordinates[xy] = Deadtile 
            else:
                if aliveNeighbors == 3:
                    coordinates[xy] = Alivetile


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
        if coordinates.get(k) == Alivetile:
            amountOfAliveNeighbors += 1 
        elif coordinates.get(k) == Deadtile:
            amountOfDeadNeighbors += 1
    
    return amountOfAliveNeighbors, amountOfDeadNeighbors

def displayGame():
    for y in range(Height):
        for x in range(Width):
            xy = str(x) + " " + str(y)
            print(coordinates.get(xy), end=" ")
        print("")
    if Verbose:
        print("\n")
        amountOfTiles = Width * Height
        totalTiles = f"Total tiles: {amountOfTiles}"
        print(totalTiles)
        aliveTiles = f"Alive tiles: {getAliveTiles()}"
        print(aliveTiles)
        deadTiles = f"Dead tiles: {amountOfTiles - getAliveTiles()}"
        print(deadTiles)

    
main(Height=50, Width=100, Deadtile = "0", Alivetile = "!", Update=1.5)