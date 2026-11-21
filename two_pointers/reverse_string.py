s = ["h", "e", "l", "l", "o", "h"]


lPointer= 0 
rPointer = len(s) - 1

while lPointer <= rPointer:

	print(lPointer, rPointer)
	s[lPointer], s[rPointer] = s[rPointer], s[lPointer]
	lPointer = lPointer + 1
	rPointer = rPointer - 1

print(s)