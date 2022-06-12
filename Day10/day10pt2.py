## Import Data ##
from audioop import reverse


with open('day10_input.txt') as fileObject:
    inputLines = fileObject.readlines()

inputLines = [line.strip() for line in inputLines]

end2start = {']':'[',')':'(','}':'{','>':'<'} #dictionary which matches end chars with start chars

## FUNCTIONS ##
def legalLine(line: str) -> bool:
    """checks a line to see if it contains an illegal character"""
    legal = True

    for index, char in enumerate(line):
        endStack = []
        #check if an end character
        if char in end2start.keys():
            endStack.append(char)
            #check every character before the found end character
            for backChar in reversed(line[0:index]):
                #if the stack is empty, the end character is legal
                if len(endStack) == 0: legal = True; break
                #if we run in to another end char, add it to the stack
                elif backChar in end2start.keys(): endStack.append(backChar)
                #if char closes the top endchar, pop the end char from the stack
                elif backChar == end2start[endStack[-1]]: endStack.pop()
                #if char does not close the endchar, that char is illegal
                elif backChar != end2start[endStack[-1]]: legal = False; break
        
        if legal is False: break
    
    return legal

def findscore(line: str) -> int:
    """finds the autocomplete score of an inputted line"""
    #build list of incomplete blocks
    charStack = []
    for char in line:
        if char in end2start.keys():
            charStack.pop()
        else: charStack.append(char)
    
    #build score
    score = 0
    charScores = {'(':1,'[':2,'{':3,'<':4}
    #the char in the last index of charStack represents the first unclosed block
    for char in reversed(charStack):
        score = score * 5 + charScores[char]

    return score

## BUILD A SCORE VALUE FOR EACH LEGAL LINE ##
scores = []
for line in inputLines:
    if legalLine(line): scores.append(findscore(line))

#find middle score
scores.sort()
midIndex = int((len(scores) - 1)/2)
midScore = scores[midIndex]

print(f"Middle Score: {midScore}")