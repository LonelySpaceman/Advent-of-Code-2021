## Import Data ##
with open('day10_input.txt') as fileObject:
    inputLines = fileObject.readlines()

inputLines = [line.strip() for line in inputLines]

end2start = {']':'[',')':'(','}':'{','>':'<'}
endChars = [']',')','}','>']
charVals = {')':3,']':57,'}':1197,'>':25137}
illegalInstances = {')':0,']':0,'}':0,'>':0}

for line in inputLines:

    illegal = False
    for index, char in enumerate(line):
        endStack = []

        #check if an end character
        if char in endChars:
            endStack.append(char)
            #check every character before the found end character
            for backChar in reversed(line[0:index]):
                #if the stack is empty, the end character is legal
                if len(endStack) == 0: illegal = False; break
                #if we run in to another end char, add it to the stack
                elif backChar in endChars: endStack.append(backChar)
                #if char closes the top endchar, pop the end char from the stack
                elif backChar == end2start[endStack[-1]]: endStack.pop()
                #if char does not close the endchar, that char is illegal
                elif backChar != end2start[endStack[-1]]: illegal = True; break

        if illegal:
            illegalInstances[char] += 1
            break

syntaxError = 0
for charType in illegalInstances:
    syntaxError += illegalInstances[charType] * charVals[charType]

print(f"Syntax Error: {syntaxError}")