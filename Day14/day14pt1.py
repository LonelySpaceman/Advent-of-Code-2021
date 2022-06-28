## IMPORT DATA ##
with open('day14_input.txt') as fileObject:
    inputLines = fileObject.readlines()

polymer = inputLines[0].strip()
rules = '\n'.join(inputLines[2::])

## APPLY RULES ##
#convert rules in to a list of usable tuples
from posixpath import split
import re
matchCode = R'(\w{2}) -> (\w{1})'
ruleList = re.findall(matchCode, rules)

for step in range(10):
    #find all rule matches in current string
    polyActions = []

    for rule in ruleList:
        charPair = rule[0]
        result = rule[1]

        matchCodes = [charPair]
        if charPair[0] == charPair[1]:
            #use positive lookbehind for overlapping strings
            newCode = f'(?<={charPair[0]}){charPair}'
            matchCodes.append(newCode)
        
        for code in matchCodes:
            matchObjects = re.finditer(code, polymer)
            for object in matchObjects:
                startIndex = object.start()
                action = (result, startIndex)
                polyActions.append(action)
        
    polyActions.sort(key = lambda x: x[1])

    #add chars to polymer based on polyActions
    charsAdded = 0
    for action in polyActions:
        char2add = action[0]
        charIndex = action[1] + charsAdded + 1

        polymer = polymer[:charIndex] + char2add + polymer[charIndex:]
        charsAdded += 1
    
#find most common and least common letter
from collections import Counter
polymer = [char for char in polymer]
polyLength = len(polymer)
letters = Counter(polymer).most_common(polyLength)

result = letters[0][1] - letters[-1][1]
print(f"Result: {result}")