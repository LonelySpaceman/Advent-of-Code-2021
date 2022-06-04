## RETRIEVE INPUTS FROM .txt FILE ##
with open("day3_input.txt") as fileObject:
	inputs = fileObject.readlines()

## REMOVE WHITESPACE FROM INPUTS ##
index = 0
for inputCheck in inputs:
	inputs[index] = inputCheck.rstrip()
	index = index + 1

## FIND OXYGEN GENERATOR RATING ##
oxGen = inputs[:] # begin with a list of all inputs
bitPositions = range(0, len(oxGen[0]) - 1)

for bitPosition in bitPositions:
	counter = 0
	for oxCheck in oxGen: # find out if there are more zeroes or ones in bit position
		if oxCheck is None:
			continue
		elif oxCheck[bitPosition] == '1':
			counter = counter + 1
		elif oxCheck[bitPosition] =='0':
			counter = counter - 1

	index = 0
	for inputCheck in inputs: # delete elements from bit position
		if inputCheck[bitPosition] == '1' and counter < 0: # delete ones if there are more zeroes
			oxGen[index] = None
		elif inputCheck[bitPosition] == '0' and counter >= 0: # delete zeroes if there are more ones or if number of zeroes and ones are the same
			oxGen[index] = None
		index = index + 1

for oxCheck in oxGen:
	if oxCheck is not None:
		oxRating = int(oxCheck, 2)

## FIND CO2 SCRUBBER RATING ##
co2Scrub = inputs[:] # begin with copy of input list

for bitPosition in bitPositions:
	counter = 0
	for co2Check in co2Scrub: # find out if there are more zeroes or ones in bit position
		if co2Check is None:
			continue
		elif co2Check[bitPosition] == '1':
			counter = counter + 1
		elif co2Check[bitPosition] =='0':
			counter = counter - 1

	index = 0
	for inputCheck in inputs: # delete elements using current bit position
		if inputCheck[bitPosition] == '0' and counter < 0: # delete zeroes if there are more zeroes
			co2Scrub[index] = None
		elif inputCheck[bitPosition] == '1' and counter >= 0: # delete ones if there are more ones or if number of zeroes and ones are the same
			co2Scrub[index] = None
		index = index + 1

	if co2Scrub.count(None) == len(inputs) - 1:
		break

for co2Check in co2Scrub:
	if co2Check is not None:
		scrubRating = int(co2Check, 2)

## FIND AND DISPLAY LIFE SUPPORT RATING ##
print(f"The Oxygen Generator Rating is: {oxRating}")
print(f"The CO2 Scrubber Rating is: {scrubRating}")
print('------------')
print(f"This means the total Life Support Rating is: {scrubRating * oxRating}")