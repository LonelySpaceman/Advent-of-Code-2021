## Import Crab Data ##
with open('day7_input.txt') as fileObject:
    crabList = fileObject.read().strip().split(',')

crabList = [int(crab) for crab in crabList]

positionList = range(min(crabList), max(crabList) + 1)

fuelCosts = []
for position in positionList:
    fuelCost = 0
    for crab in crabList:
        fuelCost += sum(range(1, abs(crab-position) + 1))
    fuelCosts.append(fuelCost)

print(f'The alignment will require {min(fuelCosts)} units of fuel.')