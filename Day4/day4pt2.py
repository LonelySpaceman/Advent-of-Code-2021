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

## DEFINE FUNCTIONS FOR REPLACING THE NUMBERS IN BINGO CARDS, CHECKING IF A BINGO CARD HAS WON ##
def cardmarker(inputNum, inputCard): # takes a bingo number and card, marks number on card with 'X'
    outputCard = inputCard[:]
    for line in outputCard:
        index = 0
        for number in line:
            if number == inputNum:
                line[index] = 'X'
            index += 1
    return outputCard

def horizontalwin(inputCard): # takes an input bingo card, checks if the card has won by matching five in a row
    winnerVector = ['X','X','X','X','X']
    for line in inputCard:
        if winnerVector == line:
            winningCard = True
            break
        else:
            winningCard = False
    return winningCard

def verticalwin(inputCard): # takes an input bingo card, checks if the card has won by matching five in a column
    winnerVector = ['X','X','X','X','X']
    for column in range(0, 5):
        checkColumn = []
        for line in inputCard:
            checkColumn.append(line[column])
        if checkColumn == winnerVector:
            winningCard = True
            break
        else:
            winningCard = False
    return winningCard

## REMOVE NUMBERS FROM BOARDS, REMOVE WINNING BOARDS UNTIL ALL BOARDS HAVE WON ##
wonCards = []
numIndex = 0

while len(wonCards) != 100:

    cardIndex = 0
    for bingoCard in bingoCards: # marks all the bingo cards based off the number bingoNumbers[numIndex]
        bingoCards[cardIndex] = cardmarker(bingoNumbers[numIndex], bingoCard)
        cardIndex += 1
    numIndex += 1

    winnerFound = True
    while winnerFound is True:
        cardIndex = 0
        for bingoCard in bingoCards:
            if horizontalwin(bingoCard) or verticalwin(bingoCard): # if any cards have won, put them in the wonCards list and ckeck bingoCards again for any more winners
                wonCards.append(bingoCards.pop(cardIndex))
                winnerFound = True
                break
            else:
                winnerFound = False
                cardIndex += 1
        
        if len(wonCards) == 100: # if all cards have won, don't search bingoCards for winning cards again
            winnerFound = False

## CALCULATE LAST WINNING CARD PRODUCT, DISPLAY PRODUCT ##
sumNum = 0
for line in wonCards[-1]:
    for num in line:
        if num != 'X':
            sumNum += int(num)

winningNumber = int(bingoNumbers[numIndex - 1])

print(f"The final product of  the last winning card and all unmarked numbers is: {sumNum * winningNumber}")