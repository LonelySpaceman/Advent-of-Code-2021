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

def smallcheck(path):
    """checks if a duplicate small cave can be added to the path"""
    smallTypes = []
    for room in path:
        if room.islower() and room not in smallTypes:
            smallTypes.append(room)

    for type in smallTypes:
        occurences = path.count(type)
        if occurences == 2: return False
    
    return True

def findexits(path: list) -> list:
    """finds all valid exits from the end of the current path"""
    room = path[-1]
    exits = []
    addSmalls = smallcheck(path)
    for pair in roomPairs:
        if room in pair: 
            exit = endfromstart(pair, room)
            smallRoom = exit.islower()
            if exit != 'start':
                if smallRoom and addSmalls: 
                    exits.append(exit)
                elif smallRoom and addSmalls is False and exit not in path:
                    exits.append(exit)
                elif smallRoom is False: 
                    exits.append(exit)
    
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