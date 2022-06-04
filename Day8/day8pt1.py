## Import Input Data ##
with open('day8_input.txt') as fileObject:
    inputLines = fileObject.readlines()

splitLists = []
for line in inputLines:
    [inputList, outputList] = line.split('|')
    splitLists.append([inputList.strip(), outputList.strip()])

outputOccurences = 0
for [inputList, outputList] in splitLists:
    #building blocks
    inputs = inputList.split()
    outputs = outputList.split()
    for output in outputs:
        if len(output) == 2:
            outputOccurences += 1
        elif len(output) == 3:
            outputOccurences += 1
        elif len(output) == 4:
            outputOccurences += 1
        elif len(output) == 7:
            outputOccurences += 1

print(f'There are {outputOccurences} of 1, 7, and 8')