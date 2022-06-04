## Import Height Data ##
with open('day9_input.txt') as fileObject:
    inputLines = fileObject.readlines()

lines = []
for line in inputLines:
    lines.append(list(line.strip()))

#build heightmap
import numpy as np
heightMap = np.array(lines)

#loop over all values in heightmap
dangerLevel = 0
for index, height in np.ndenumerate(heightMap):
    if '*' not in height:
        y, x = index
        coords2Check = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)] #left, right, top, bottom
        lowestVal = True

        #check all adjacent coordinates
        for coord in coords2Check:
            try:
                if int(height[0]) >= int(heightMap[coord][0]): 
                    lowestVal = False
                    break
            except IndexError:
                pass
        
        #calculate danger level
        if lowestVal:
            dangerLevel += int(height) + 1
            for yCheck, xCheck in coords2Check: 
                try:
                    heightMap[yCheck, xCheck] += '*' #if one particular coord is the lowest val, all adjacent coords will not be the lowest val
                except IndexError:
                    pass

print(f'The danger level is: {dangerLevel}')