s = "abc"
t = "ahbgdc"


i,j = 0, 0

if s == '' : print('is a sub sequence')
if len(s) > len(t) : print('Not a sub sequence')

i = 0


for j in range(len(t)):
	if t[j] == s[i]:
		if i == len(s) - 1:
			print('is a sub sequence')		
		i+=1

print('not a sub sequence')

