## Import Crab Data ##
with open('day7_input.txt') as fileObject:
    crabList = fileObject.read().strip().split(',')

crabList = [int(crab) for crab in crabList]

#calculate median crab
from statistics import median
medianCrab = median(crabList)

#calculate fuel cost of aligning to the median crab
fuelCost = 0
for crab in crabList:
    fuelCost += abs(crab - medianCrab)

print(f'The alignment will require {int(fuelCost)} units of fuel.')