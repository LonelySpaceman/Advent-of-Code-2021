## RETRIEVE INPUT DEPTHS FROM .txt FILE ##
with open("day1_input.txt") as fileObject:
	depths = fileObject.readlines()

## REMOVE WHITESPACE FROM depths, CONVERT TO INTEGER ##
index = 0
for depth in depths:

	depths[index] = int(depth.rstrip())
	index = index + 1

## COUNT THE NUMBER OF DEPTH INCREASES, DECREASES, AND FLATS ##
increases = 0
decreases = 0
flats = 0

for index in range(1, len(depths)):

	if depths[index] == depths[index - 1]:
		flats = flats + 1
	elif depths[index] > depths[index - 1]:
		increases = increases + 1
	elif depths[index] < depths[index - 1]:
		decreases = decreases + 1

## PRINT OUT NUMBER OF INCREASES, DECREASES, FLATS ##
print(f"The depth was steady {flats} times!")
print(f"The depth increased {increases} times!")
print(f"The depth decreased {decreases} times!")