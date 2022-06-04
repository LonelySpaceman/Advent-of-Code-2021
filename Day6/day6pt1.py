## Import Fish Data ##
with open('day6_input.txt') as fileObject:
    fishList = fileObject.read().strip().split(',')

fishList = [int(fish) for fish in fishList]

for day in range(0,80):

    newFishes = []
    for fishNum, fishTimer in enumerate(fishList):
        if fishTimer == 0: #if a fish timer is equal to zero, reset the current fishe's timer to 6
            fishList[fishNum] = 6
            newFishes.append(8) #add a mew fish at the end of the day
        else:
            fishList[fishNum] -= 1 #otherwise just subtract one from the fish timer
    
    #add new fishes at the end of each day to fishList
    fishList += newFishes

print(f'After 80 days there will be {len(fishList)} fishes!')