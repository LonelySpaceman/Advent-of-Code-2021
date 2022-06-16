## IMPORT DATA ##
with open('day12_input.txt') as fileObject:
    input = fileObject.read()

## SPLIT LINES INTO COORDINATE PAIRS ##
import re
searchCode = '(\S+)-(\S+)'

roomPairs = []
matchObjects = re.finditer(searchCode, input)
for matchObject in matchObjects: roomPairs.append(matchObject.groups())

## FUNCTIONS ##
def endfromstart(pair: tuple, start: str) -> str:
    """returns end room given a room pair and start room"""
    #room in pair which is not start
    end = [room for room in pair if room != start]
    return end[0]

def findexits(path: list) -> list:
    """finds all valid exits from the end of the current path"""
    room = path[-1]
    exits = []
    for pair in roomPairs:
        if room in pair: 
            exit = endfromstart(pair, room)
            if exit.islower() and exit in path: pass
            else: exits.append(exit)
    
    return exits

## FIND PATHS USING BREADTH FIRST SEARCH ##
pathQueue = [['start']]
validPaths = []
for path in pathQueue:
    if ('end' in path) and (path not in validPaths): 
        validPaths.append(path)
        exits = []
    else: exits = findexits(path)

    for exit in exits:
        newPath = path.copy()
        newPath.append(exit)
        pathQueue.append(newPath)

print(f"Number of Valid Paths: {len(validPaths)}")