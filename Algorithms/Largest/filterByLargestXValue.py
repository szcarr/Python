liste = [[442, 660, 230, 100], [424, 653, 232, 101], [740, 823, 400, 300], [902, 400, 289, 188], [580, 230, 230, 59], [1230, 100, 820, 111], [1432, 950, 654, 702]]

def filterByLargestXValue(inputListe):
    '''
    Expected arg is a list with a list with quadruple integers as elements to its parent list
    [[442, 660, 230, 100], [424, 653, 232, 101]]

    Returns the same list but the list in the list is now filtered after its first element in the list by largest value
    '''
    filtrertListe = []
    indexSkipList = []
    skipIndex = 0
    while len(filtrertListe) != len(inputListe):
        largestXValueNow = 0
        xyListe = []
        for y in range(len(inputListe)): #For kvart element i liste. som er endå ei liste
            skip = False
            for x in range(len(indexSkipList)):
                if indexSkipList[x] == y:
                    skip = True
            if skip:
                continue
            if inputListe[y][0] > largestXValueNow: #Sjekkar for kvart element om kva som er størst
                largestXValueNow = inputListe[y][0]
                skipIndex = y
                yValueOfX = inputListe[y][1]
                wValueOfX = inputListe[y][2]
                hValueOfX = inputListe[y][3]
            print(largestXValueNow)
        xyListe.append(largestXValueNow)
        xyListe.append(yValueOfX)
        xyListe.append(wValueOfX)
        xyListe.append(hValueOfX)
        filtrertListe.append(xyListe)
        indexSkipList.append(skipIndex)

    return filtrertListe