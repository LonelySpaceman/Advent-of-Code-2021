from array import array
import numpy as np

## IMPORT DATA ##
with open('day15_input.txt') as fileObject:
        inputLines = fileObject.readlines()

lines = []
for line in inputLines:
    line  = [int(char) for char in line.strip()]
    lines.append(line)

#build cave map
caveMap = np.array(lines)

nodeDict = {}
coordStack = []
for index, value in np.ndenumerate(caveMap):
    nodeDict[index] = float('inf')
    coordStack.append(index)

lastCoord = coordStack[-1]

#starting coordinate
nodeDict[(0,0)] = 0

## FIND SHORTEST PATH USING DIJKSTRA'S ALGORITHM ##
def validCoord(coordPair: tuple, array: array, visitedCoords: list) -> bool:
    """checks to see if a coordinate in an array is valid"""
    if any((coord < 0 for coord in coordPair)): 
        return False
    if coordPair in visitedCoords:
        return False

    try: array[coordPair]; return True
    except IndexError: return False

vistiedCoords = []
while True:
    coord = coordStack[0]
    del coordStack[0]

    dangerLevel = nodeDict[coord]

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

        pathValue = caveMap[checkCoord] + dangerLevel
        nodeDanger = nodeDict[checkCoord]

        if pathValue < nodeDanger and checkCoord not in vistiedCoords:
            nodeDict[checkCoord] = pathValue

            #sort node in to stack
            coordStack.remove(checkCoord)
            tempStack = []
            for index, stackCoord in enumerate(coordStack):
                value = nodeDict[stackCoord]

                if value >= nodeDict[checkCoord]:
                    coordStack = tempStack + [checkCoord] + coordStack[index:]
                    break
                else:
                    tempStack.append(coordStack[index])
    
    vistiedCoords.append(coord)