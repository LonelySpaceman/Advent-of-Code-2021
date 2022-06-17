## IMPORT DATA ##
with open('day13_input.txt') as fileObject:
    input = fileObject.read()

## BUILD LIST OF COORDS, INSTRUCTIONS ##
import re #using regex
pointCode = '(\d+),(\d+)'
instructCode = 'fold along (\w)=(\d+)'

coords = []
instructions = []
#coords
matchObjects = re.finditer(pointCode, input)
for matchObject in matchObjects:
    matchTuple = matchObject.groups()
    matchTuple = [int(coord) for coord in matchTuple]
    coords.append(matchTuple)

#instructions
matchObjects = re.finditer(instructCode, input)
for matchObject in matchObjects:
    matchTuple = matchObject.groups()
    instructions.append(matchTuple)

## BUILD NUMPY ARRAY FROM COORD LIST ##
#find max x and y values, build table based off those values
xList = []
yList = []
for coord in coords:
    xList.append(coord[0])
    yList.append(coord[1])

import numpy as np
xMax = max([int(xNum) for xNum in xList])
yMax = max([int(yNum) for yNum in yList])
sheet = np.ones([yMax + 1, xMax + 1], dtype=str)
sheet[:] = '.'

#build initial sheet
for coord in coords:
    x,y = coord
    sheet[y,x] = '#'

## FOLDING FUNCTIONS ##
def horizontalfold(sheetIn, foldLine):
    """folds when folddirection is x"""
    foldedSheet = np.copy(sheetIn)
    for coord, value in np.ndenumerate(sheetIn):
        y,x = coord

        #fold points below the fold line up
        if x > foldLine and '#' in value:
            pointDiff = foldLine - x
            foldedSheet[(y, foldLine + pointDiff)] = '#'
    
    #slice off folded section of sheet
    foldedSheet = foldedSheet[:, 0:foldLine]
        
    return foldedSheet

def verticalfold(sheetIn, foldLine):
    """folds when folddirection is y"""
    foldedSheet = np.copy(sheetIn)
    for coord, value in np.ndenumerate(sheetIn):
        y, x = coord
        
        #fold points right of the fold line to the left
        if y > foldLine and '#' in value:
            pointDiff = foldLine - y
            foldedSheet[(foldLine + pointDiff, x)] = '#'
    
    #slice off folded section of sheet
    foldedSheet = foldedSheet[0:foldLine, :]
    
    return foldedSheet

## COMPUTE FOLD INSTRUCTIONS ##
for instruction in instructions:
    direction, line = instruction
    line = int(line)
    if direction == 'y':
        sheet = verticalfold(sheet, line)
    elif direction == 'x':
        sheet = horizontalfold(sheet, line)

## WRITE FINAL RESULT TO TEXT FILE ##
lines = sheet.tolist()
lines = [''.join(line) for line in lines]

with open('result.txt', 'w') as fileObject:
    for line in lines:
        fileObject.write(line)
print("Finished!")

#now go in to result.txt and adjust the
#window width until the letters appear