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
	magnitude.append(int(splitInput[1]))

## FIND DEPTH & HORIZONTAL POSITION, CALCULATE PRODUCT ##
horizontalPosition = 0
depth = 0
aim = 0

for index in range(0, len(commandInputs)):
	if direction[index] == 'forward':
		horizontalPosition = horizontalPosition + magnitude[index]
		depth = depth + magnitude[index] * aim
	elif direction[index] == 'up':
		aim = aim - magnitude[index]
	elif direction[index] == 'down':
		aim = aim + magnitude[index]

product = horizontalPosition * depth
print(f"Your depth product is: {product}!")