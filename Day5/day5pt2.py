## Import Coordinate Data ##
with open('day5_input.txt') as fileObject:
    inputs = fileObject.readlines()

# Get list of relevant coordinate pairs
import re
coordPairList = []
for input in inputs:
    matchCode = '(\d+),(\d+) -> (\d+),(\d+)'

    matchObject = re.search(matchCode, input)
    coordPairList.append(matchObject.groups())

#find max x and y values, build table based off those values
xList = []
yList = []
for coord in coordPairList:
    xList.append(coord[0]); xList.append(coord[2])
    yList.append(coord[1]); yList.append(coord[3])

import numpy as np
xMax = max([int(xNum) for xNum in xList])
yMax = max([int(yNum) for yNum in yList])
grid = np.zeros((xMax, yMax))

#for each coordinate pair, build a list of coordinates on the line and add 1 to the grid at that point
for coord in coordPairList:

    delX = int(coord[2]) - int(coord[0])
    delY = int(coord[3]) - int(coord[1])

    if delX == 0 or delY == 0:
        xCoords = sorted((int(coord[0]), int(coord[2])))
        yCoords = sorted((int(coord[1]), int(coord[3]))) #this only works because of straight lines

        xRange = [xCoord for xCoord in range(xCoords[0], xCoords[1] + 1, 1)]
        yRange = [yCoord for yCoord in range(yCoords[0], yCoords[1] + 1, 1)]

        #add to table at constructed coordinate
        for yVal in yRange:
            for xVal in xRange:
                grid[xVal - 1 , yVal - 1] += 1
    
    elif abs(delX) == abs(delY): #diagonal case
        xUnity = int(delX/abs(delX))
        xRange = [xCoord for xCoord in range(int(coord[0]), int(coord[2]) + xUnity, xUnity)]
        yUnity = int(delY/abs(delY))
        yRange = [yCoord for yCoord in range(int(coord[1]), int(coord[3]) + yUnity, yUnity)]

        for i, x in enumerate(xRange):
            grid[xRange[i] - 1, yRange[i] - 1] += 1

#find number of grid points with values greater than one
answer = 0
for pointVal in np.nditer(grid):
    if pointVal > 1: answer += 1

print(f'{answer} points overlap\n')
