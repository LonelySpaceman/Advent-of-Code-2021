## Import Fish Data ##
with open('day6_input.txt') as fileObject:
    fishList = fileObject.read().strip().split(',')

fishList = [int(fish) for fish in fishList]

#get population of each age of fish
fishCensus = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for fishTimer in fishList:
        fishCensus[fishTimer] += 1

#initiate carousel of exponential growth!
for day in range(0, 256):
    nextDay = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for fishTimer in sorted(fishCensus.keys()):
        if fishTimer !=0:
            nextDay[fishTimer - 1] = fishCensus[fishTimer]

    # deal with population where fishTimer = 0 last  
    nextDay[6] += fishCensus[0]
    nextDay[8] = fishCensus[0]

    fishCensus = nextDay #replace old fish Census with new fish Census

totalFish = sum([populationSize for populationSize in fishCensus.values()])
print(f'After {day + 1} days, there will be {totalFish} fish!')
