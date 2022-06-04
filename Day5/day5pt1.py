## Import Coordinate Data ##
with open('day5_input.txt') as fileObject:
    inputs = fileObject.readlines()

# Get list of relevant coordinate pairs
import re
coordPairList = []
for input in inputs:
    matchCode = '(\d+),(\d+) -> (\d+),(\d+)'

    matchObject = re.search(matchCode, input)
    (x1, y1, x2, y2) = matchObject.groups()

    #vertical or horizontal lines
    if x1 == x2 or y1 == y2:
        coordPairList.append([x1, y1, x2, y2])

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
    xCoords = sorted((int(coord[0]), int(coord[2])))
    yCoords = sorted((int(coord[1]), int(coord[3]))) #this only works because of straight lines

    xRange = [xCoord for xCoord in range(xCoords[0], xCoords[1] + 1, 1)]
    yRange = [yCoord for yCoord in range(yCoords[0], yCoords[1] + 1, 1)]

    #add to table at constructed coordinate
    coordList = []
    for yVal in yRange:
        for xVal in xRange:
            grid[xVal - 1 , yVal - 1] += 1

#find number of grid points with values greater than one
answer = 0
for pointVal in np.nditer(grid):
    if pointVal > 1: answer += 1

print(f'{answer} points overlap\n')
