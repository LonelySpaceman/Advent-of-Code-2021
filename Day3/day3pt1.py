## RETRIEVE INPUTS FROM .txt FILE ##
with open("day3_input.txt") as fileObject:
	inputs = fileObject.readlines()

## REMOVE WHITESPACE FROM INPUTS ##
index = 0
for inputCheck in inputs:
	inputs[index] = inputCheck.rstrip()
	index = index + 1

## CONSTRUCT GAMMA RATES AND EPSILON RATES ##
gamma = []
epsilon = []

# make gamma list of zeroes as long as the inputs
for index in inputs[0]:
	gamma.append(0)

# calculate gamma rate and epsilon rate
for inputCheck in inputs: # for each input, if the number is 1 in a certain position, add one to the gamma list in that same index. If the number is 0, subtract 1.
	index = 0
	for check in inputCheck:
		if check == '1':
			gamma[index] = gamma[index] + 1
		elif check == '0':
			gamma[index] = gamma[index] - 1
		index = index + 1

for index in gamma: # epsilon will be the opposite of gamma
	epsilon.append(index * -1)

index = 0
for epsilonCheck in epsilon: # construct binary epsilon rate
	if epsilonCheck < 0:
		epsilon[index] = 0
	elif epsilonCheck > 0:
		epsilon[index] = 1
	index = index + 1

index = 0
for gammaCheck in gamma: # construct binary gamma rate
	if gammaCheck < 0:
		gamma[index] = 0
	elif gammaCheck > 0:
		gamma[index] = 1
	index = index + 1

## CONVERT GAMMA AND EPSILON RATES IN TO DECIMAL, FIND PRODUCT ##
epsilonRate = '' # convert epsilon into single string
for epsilonCheck in epsilon:
	epsilonRate += str(epsilonCheck)

gammaRate = ''
for gammaCheck in gamma: # convert gamma into single string
	gammaRate += str(gammaCheck)

gammaRate = int(gammaRate, 2) # convert binary to decimal
epsilonRate = int(epsilonRate, 2)

product = gammaRate * epsilonRate
print(f"The power consumption of the Submarine is: {product} generic power units")