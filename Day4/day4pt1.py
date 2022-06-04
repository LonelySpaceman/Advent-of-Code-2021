## RETRIEVE INPUTS FROM .txt FILE ##
with open('day4_input.txt') as fileObject:
    inputs = fileObject.readlines()

## PULL ALL BINGO NUMBERS ##
bingoNumbers = inputs[0].rstrip().split(',')

## PULL ALL BINGO CARDS ##
bingoCards = []
bingoCard = -1
for inputCheck in inputs[1:]:
    if inputCheck == '\n':
        bingoCards.append([])
        bingoCard += 1
    else:
        bingoCards[bingoCard].append(inputCheck.rstrip())

## RE-FORMAT BINGO CARDS ##
for bingoCard in bingoCards:
    index = 0
    for line in bingoCard:
        bingoCard[index] = line.split()
        index += 1

## REMOVE NUMBERS FROM BOARD UNTIL ONE BOARD WINS ##
noWinner = True
numberIndex = 0

while noWinner:
    numToCheck = bingoNumbers[numberIndex]
    for bingoCard in bingoCards: # replace all numbers that match numToCheck with 'X'
        for line in bingoCard:
            index = 0
            for number in line:
                if number == numToCheck:
                    line[index] = 'X'
                index += 1

    winnerVector = ['X','X','X','X','X']
    winningCard = -1
    for bingoCard in bingoCards:
        if noWinner is False:
            break
        winningCard += 1
        for line in bingoCard:
            if winnerVector == line: # checking for winning rows
                noWinner = False
        if noWinner is False:
            break

        index = 0
        for column in range(0, 5): # checking for winning columns
            checkColumn = []
            for line in bingoCard:
                checkColumn.append(line[column])
            if checkColumn == winnerVector:
                noWinner = False

    numberIndex += 1

## FINDING THE SUM OF ALL UNCROSSED NUMBERS, MULTIPLYING BY WINNING NUMBER ##
sumNum = 0
for line in bingoCards[winningCard]:
    for number in line:
        if number != 'X':
            sumNum += int(number)

print(f"The answer is: {sumNum * int(bingoNumbers[numberIndex - 1])}")