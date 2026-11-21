#s = "race a car"

s="A man, a plan, a canal: Panama"

lp = 0
hp = len(s) - 1

isPalindrome = True

while lp < hp:

	if not s[lp].isalnum():
		lp+=1
		continue 
	if not s[hp].isalnum():
		hp-=1	
		continue

	#print(s[lp].lower(), s[hp].lower())

	if s[lp].lower() != s[hp].lower():
		isPalindrome = False
		break
	
	lp, hp = lp+1, hp-1



print(isPalindrome)