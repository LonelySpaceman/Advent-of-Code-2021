from array import array
import numpy as np

## IMPORT DATA ##
with open('day11_input.txt') as fileObject:
        inputLines = fileObject.readlines()

lines = []
for line in inputLines:
    line  = [int(char) for char in line.strip()]
    lines.append(line)

#build octopus map
octoMap = np.array(lines)

def validCoord(coord: tuple, array: array) -> bool:
    """checks to see if a coordinate in an array is valid"""
    if coord[0] < 0 or coord[1] < 0: return False

    try: array[coord]; return True
    except IndexError: return False

class Octopusses:
    """A class which models octopus behavior at each step"""
    flashes = 0

    def __init__(self, octoMap):
        self.octopusses = octoMap
    
    def addOne(self):
        """add one to each octopus in the simulation"""
        for index, octopus in np.ndenumerate(self.octopusses):
            self.octopusses[index] += 1
    
    def flash(self):
        """calculates flashes using a queue"""
        flashQueue = []
        #-5 means that value has flashed and is temporarily immutable
        for index, octopus in np.ndenumerate(self.octopusses):
            if octopus > 9: flashQueue.append(index)
        
        for octoCoord in flashQueue:
            self.octopusses[octoCoord] = -5
            y, x = octoCoord
            #list of points adjacent to flashpoint with positive coordinates
            connectedPoints = [
            (y+1,x-1),(y+1,x),(y+1,x+1),
            (y,x-1),(y,x+1),
            (y-1,x-1),(y-1,x),(y-1,x+1)]

            connectedPoints = [(y,x) for (y,x) in connectedPoints if validCoord((y,x),self.octopusses)]
            #add one to each connected point
            for point in connectedPoints:
                if self.octopusses[point] != -5:
                    self.octopusses[point] += 1

                    if (self.octopusses[point] > 9) and (point not in flashQueue): flashQueue.append(point)
                        
    def reset(self):
        """reset each flashed point to 0, each time adding to the number of flashes"""
        for index, octopus in np.ndenumerate(self.octopusses):
            if octopus == -5:
                self.octopusses[index] = 0
                self.flashes += 1

## SIMULATE OCTOPUSSES AT EACH STEP ##
octoSim = Octopusses(octoMap)
for step in range(100):
    #perform each action
    octoSim.addOne()
    octoSim.flash()
    octoSim.reset()

octoFlashes = octoSim.flashes

print(f"Number of Flashes: {octoFlashes}")