height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

lp = 0
rp = len(height) - 1

max_width = rp - lp
max_height = height[lp] if height[lp] < height[rp] else height[rp]


max_water = max_height * max_width

while lp < rp:

	max_width = rp - lp
	max_height = height[lp] if height[lp] < height[rp] else height[rp]

	if max_water < max_height * max_width:
		max_water = max_height * max_width 

	if height[lp] < height[rp]:
		lp+=1
	else:
		rp-=1

print(max_water)

