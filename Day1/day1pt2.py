## RETRIEVE INPUT DEPTHS FROM .txt FILE ##
with open("day1_input.txt") as fileObject:
	depths = fileObject.readlines()

## REMOVE WHITESPACE FROM depths, CONVERT TO INTEGER ##
index = 0
for depth in depths:
	depths[index] = int(depth.rstrip())
	index = index + 1

## GROUP AND SUM DEPTHS INTO DEPTH WINDOWS ##
depthWindows = []
for index in range(0, len(depths)):
	try:
		depthWindows.append(depths[index] + depths[index + 1] + depths[index + 2])
	except:
		break

## COUNT THE NUMBER OF DEPTH INCREASES, DECREASES, AND FLATS ##
increases = 0
decreases = 0
flats = 0

for index in range(1, len(depthWindows)):
	if depthWindows[index] == depthWindows[index - 1]:
		flats = flats + 1
	elif depthWindows[index] > depthWindows[index - 1]:
		increases = increases + 1
	elif depthWindows[index] < depthWindows[index - 1]:
		decreases = decreases + 1

## PRINT OUT NUMBER OF INCREASES, DECREASES, FLATS ##
print(f"The depth was steady {flats} times!")
print(f"The depth increased {increases} times!")
print(f"The depth decreased {decreases} times!")