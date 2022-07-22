from array import array
import numpy as np

## IMPORT DATA ##
with open('day15_input.txt') as fileObject:
        inputLines = fileObject.readlines()

lines = []
for line in inputLines:
    line  = [int(char) for char in line.strip()]
    xLen = len(line)
    lines.append(line)
yLen = len(lines)
originalMap = np.array(lines)

#build initial cave map
def carouselsum(number: int, steps: int) -> int:
    """adds steps to input with carousel rules"""
    for _ in range(steps):
        if number == 9:
            number = 1
        else:
            number += 1
    return number

caveMap = np.zeros((yLen * 5, xLen * 5), dtype=int)

for x in range(5):
    for y in range(5):
        steps = x + y
        xOffset = x * xLen
        yOffset = y * yLen

        for (mapY,mapX), value in np.ndenumerate(originalMap):
            mapX += xOffset
            mapY += yOffset

            caveMap[mapY,mapX] = carouselsum(value,steps)

print('Map Constructed!')
## FIND SHORTEST PATH USING A* ##
nodeDict = {}
coordStack = []
for index, value in np.ndenumerate(caveMap):
    nodeDict[index] = {'danger':float('inf'),'heuristic':float('inf')}
    coordStack.append(index)

lastCoord = coordStack[-1]

#starting coordinate
nodeDict[(0,0)] = {'danger':0}

def validCoord(coordPair: tuple, array: array, visitedCoords: list) -> bool:
    """checks to see if a coordinate in an array is valid"""
    if any((coord < 0 for coord in coordPair)): 
        return False
    if coordPair in visitedCoords:
        return False

    try: 
        array[coordPair]
        return True
    except IndexError: 
        return False

vistiedCoords = []
while True:
    coord = coordStack[0]
    del coordStack[0]

    dangerLevel = nodeDict[coord]['danger']

    if coord == lastCoord:
        print(f"The total path danger is: {dangerLevel}")
        exit()

    #find valid coordinates connected to the point
    y,x = coord
    connectedCoords = [
        (y-1,x),(y+1,x),
        (y,x-1),(y,x+1)]

    connectedCoords = [
            (y,x) for (y,x) in connectedCoords if validCoord((y,x),caveMap,vistiedCoords)]
    
    #loop through each connected coord, apply the algorithm
    for checkCoord in connectedCoords:
        
        pathWeight = caveMap[checkCoord] + dangerLevel
        nodeWeight = nodeDict[checkCoord]['danger']

        if pathWeight < nodeWeight and checkCoord not in vistiedCoords:
            #calculate distance to finish
            y,x = checkCoord
            finX, finY = lastCoord
            distance = abs(finY - y) + abs(finX - x)

            nodeDict[checkCoord]['danger'] = pathWeight
            nodeDict[checkCoord]['heuristic'] = pathWeight + distance

            #sort node in to stack
            coordStack.remove(checkCoord)
            biggestCoord = True
            for index, stackCoord in enumerate(coordStack):
                value = nodeDict[stackCoord]['heuristic']

                if value >= nodeDict[checkCoord]['heuristic']:
                    coordStack.insert(index, checkCoord)
                    biggestCoord = False
                    break
            if biggestCoord:
                coordStack.append(checkCoord)
    
    vistiedCoords.append(coord)
    if len(vistiedCoords) % 10000 == 0:
        print(f'Nodes Checked: {len(vistiedCoords)}')