nums = [0,1,2,2,3,0,4,2]

val = 2

i = 0
n = len(nums)


while i < n :

	if nums[i] == val:
		nums[i] = nums[n-1]
		n -= 1
	else:
		i += 1

print(n)
print(nums)
