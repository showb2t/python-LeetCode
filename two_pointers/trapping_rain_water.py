height = [0,1,0,2,1,0,1,3,2,1,2,1]


l_max = 0
r_max = 0


l_max_array = [0]
r_max_array = [0]


for i in range(1,len(height)):
	l_max = max(height[i-1], l_max)
	l_max_array.append(l_max)

for j in range(len(height)-2, -1 , -1):
	r_max = max(height[j+1], r_max)
	r_max_array.append(r_max)

r_max_array.reverse()


print(l_max_array)
print(r_max_array)


water_stored = 0

for k in range(len(height)):
	potential = min(l_max_array[k], r_max_array[k]) - height[k]
	if potential > 0:
		water_stored = water_stored + potential
	else:
		continue

print(water_stored)


