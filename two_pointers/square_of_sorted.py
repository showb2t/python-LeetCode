nums = [-4, -1, 0, 3, 10]

sq_nums = [n*n for n in nums] 

lPointer = 0
rPointer = len(sq_nums) - 1

final_array = []

while lPointer <= rPointer:
	if sq_nums[rPointer] > sq_nums[lPointer]:
		final_array.append(sq_nums[rPointer])
		rPointer = rPointer - 1
	else:
		final_array.append(sq_nums[lPointer])
		lPointer = lPointer + 1	

	print(final_array)

print(final_array[::-1])


