## RETRIEVE INPUT COMMANDS FROM .txt FILE ##
with open("day2_input.txt") as fileObject:
	commandInputs = fileObject.readlines()

## USE THE .split() METHOD TO SEPARATE DIRECTION AND MAGNITUDE ##
# create empty lists with direction and magnitude
direction = []
magnitude = []

# split direction and magnitude from commandInputs and append to empty lists
for commandInput in commandInputs:
	splitInput = commandInput.split()

	direction.append(splitInput[0])
	magnitude.append(splitInput[1])

## FIND DEPTH & HORIZONTAL POSITION, CALCULATE PRODUCT ##
horizontalPosition = 0
depth = 0

for index in range(0, len(commandInputs)):
	if direction[index] == 'forward':
		horizontalPosition = horizontalPosition + int(magnitude[index])
	elif direction[index] == 'up':
		depth = depth - int(magnitude[index])
	elif direction[index] == 'down':
		depth = depth + int(magnitude[index])

product = horizontalPosition * depth
print(f"Your depth product is: {product}!")