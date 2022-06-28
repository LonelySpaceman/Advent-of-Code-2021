## IMPORT DATA ##
import time
startTime = time.time()

import os
os.system('clear')

with open('day14_input.txt') as fileObject:
    inputLines = fileObject.readlines()

polymer = inputLines[0].strip()
polymer = [char for char in polymer]
rules = '\n'.join(inputLines[2::])

## DEFINE INITIAL CHARACTER STACK ##
#convert rules in to a dict of usable tuples
import re
matchCode = R'(\w{2}) -> (\w{1})'
ruleList = dict(re.findall(matchCode, rules))

#build dict of pairs in initial polymer
polyPairs = {rule : 0 for rule in ruleList.keys()}
for index, char in enumerate(polymer[:-1]):
    pair = char + polymer[index + 1]
    polyPairs[pair] += 1

## APPLY RULES ##
def paircheck(pair: str) -> list:
    """returns a list of subsequent pairs for an inputted pair"""
    midChar = ruleList[pair]
    #create sibling pairs
    pairList = [pair[0] + midChar, midChar + pair[1]]
    return pairList

#for each rule, pre-calculate number of pairs out for 1 step
childrenPairs = {}
for pair in ruleList.keys():
    pairStack = [(pair, 0)]
    pairCount = {pair : 0 for pair in ruleList.keys()}

    children = paircheck(pair)
    for child in children:
        pairCount[child] += 1
    
    childrenPairs[pair] = pairCount

#use pair count at 1 to find pair count at 40
for step in range(40):
    stepPairs = {pair : 0 for pair in ruleList.keys()}
    for polyPair in polyPairs:
        startingValue = polyPairs[polyPair]
        pairDict = childrenPairs[polyPair]

        for pair in pairDict:
            stepPairs[pair] += startingValue * pairDict[pair]
    
    polyPairs = stepPairs

## COUNT NUMBER OF CHARS IN PAIRS ##
charCount = {}
for pair in polyPairs:
    char = pair[0]
    occurences = polyPairs[pair]
    try:
        charCount[char] += occurences
    except KeyError:
        charCount[char] = occurences

#preallocation will miss last char in polymer
charCount[polymer[-1]] += 1

## FIND MOST AND LEAST COMMON LETTER ##
print(charCount)
max = max(charCount.values())
min = min(charCount.values())

result = max - min
print(f"Result: {result}")

programTime = time.time() - startTime
print(f"Total Program Time: {programTime} seconds")