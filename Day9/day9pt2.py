## Imports ##
import time
import numpy as np
import curses
from curses import wrapper

def main(stdscr):
    stdscr.getch()
    ## Import Height Data ##
    with open('day9_input.txt') as fileObject:
        inputLines = fileObject.readlines()

    lines = []
    for index, line in enumerate(inputLines):
        lines.append(list(line.strip()))

    #build heightmap
    heightMap = np.array(lines)

    #define color pairs
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK); NUCLEUS_COLOR = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK); CHECK_COLOR = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK); WALL_COLOR = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK); DEFAULT_COLOR = curses.color_pair(4)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLACK); EMPTY_SPACE = curses.color_pair(5)

    #resize terminal
    def resizeterminal():
        resize = curses.is_term_resized(40,101) #true if terminal needs to be resized
        if resize:
            stdscr.clear()
            curses.resize_term(101,40)
            stdscr.refresh()


    def maplimits(heightMap, nucY):
        hmLines = heightMap.tolist()
        #find scrolling map display boundaries
        mapLimit = 40
        startIndex = int(nucY - mapLimit/2); endIndex = int(nucY + mapLimit/2)

        try:
            hmLines[endIndex]
            if startIndex < 0: startIndex = 0; endIndex = mapLimit
        except IndexError:
            maxIndex = len(hmLines)
            startIndex = maxIndex - mapLimit; endIndex = maxIndex
            
        return startIndex, endIndex

    def displaymap(heightMap, nucY):
        #display map in terminal
        hmLines = heightMap.tolist()
        startIndex, endIndex = maplimits(heightMap, nucY)
        displayLines = hmLines[startIndex:endIndex]
        for row, line in enumerate(displayLines):
            for column, char in enumerate(line):
                colorDict = {'!' : NUCLEUS_COLOR, '#' : DEFAULT_COLOR, 'O' : WALL_COLOR, ' ' : EMPTY_SPACE}
                stdscr.addstr(row, column, char, colorDict[char])
    
    def displayspecial(heightMap, checkedCoord, nucCoord):
        nucY, nucX = nucCoord
        checkY, checkX = checkedCoord

        startIndex, endIndex = maplimits(heightMap, nucY)
        stdscr.addstr(nucY - startIndex, nucX, '!', NUCLEUS_COLOR | curses.A_BOLD) #display current nucleation site
        stdscr.addstr(checkY - startIndex, checkX, '#', CHECK_COLOR | curses.A_BOLD) #display newly added checked coordinate

    #loop over all values in heightmap to find basin nucleation sites
    nucSites = []
    for index, height in np.ndenumerate(heightMap):
        if '*' not in height and '9' not in height:
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
            
            #mark nucleation site
            if lowestVal:
                nucSites.append(index)
                for yCheck, xCheck in coords2Check: 
                    try:
                        if heightMap[yCheck, xCheck] != '9': heightMap[yCheck, xCheck] += '*' #if one particular coord is the lowest val, all adjacent coords will not be the lowest val
                    except IndexError:
                        pass
        
    #redraw height map
    for index, height in np.ndenumerate(heightMap):

        if index in nucSites:
            heightMap[index] = '!'
        elif '9' in height:
            heightMap[index] = 'O'
        else:
            heightMap[index] = ' '
        
    #each nucleation site will correspond to a basin
    basinSizes = []
    for nucY, nucX in nucSites:
        basinCoords = [(nucY, nucX)]

        #retrieve new basin coordinates based off of adjacent coordinates
        for y, x in basinCoords:
            #build list of coordinates to check
            coords2Check = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]

            for coord in coords2Check:
                (y,x) = coord
                #check if the coord is actually in heightMap
                inMap = True
                try:
                    heightMap[coord]
                except IndexError: inMap = False
                if y < 0 or x < 0: inMap = False

                #add coord to basinCoords if it's inside heightMap and not a wall ('0') and hasn't already been checked 
                if (inMap is True) and ('O' not in heightMap[coord]) and (coord not in basinCoords):
                    heightMap[coord] = '#'; basinCoords.append(coord)
                    stdscr.refresh() #reset terminal to previous state
                    resizeterminal()
                    displaymap(heightMap, nucY)
                    displayspecial(heightMap, (y,x), (nucY,nucX))
                    time.sleep(0.005)
        
        basinSizes.append(len(basinCoords))

    #code which originally calculated the answer to the puzzle, unneeded in Curses visualization
    """ basinSizes = [int(size) for size in basinSizes]
    basinSizes.sort(reverse=True)
    basinProd = np.prod(basinSizes[0:3])
    print(f"The final basin product is: {basinProd}") """

    resizeterminal()
    displaymap(heightMap, nucY)
    stdscr.getch() #wait for user input to exit program

#initialize wrapper
wrapper(main)
