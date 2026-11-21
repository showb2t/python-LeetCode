hashmap = {'I': 1, 
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000 }


s = "III"

sum = 0 
for itr in range(len(s)):
    if itr == 0:
        sum = hashmap[s[itr]]
    if itr != 0:
        if s[itr] == 'X' and s[itr-1] == 'I':
            sum = sum + 8
        elif s[itr] == 'V' and s[itr-1] == 'I':
            sum = sum + 3
        elif s[itr] == 'L' and s[itr-1] == 'X':
            sum = sum + 30
        elif s[itr] == 'C' and s[itr-1] == 'X':
            sum = sum + 80
        elif s[itr] == 'D' and s[itr-1] == 'C':
            sum = sum + 300
        elif s[itr] == 'M' and s[itr-1] == 'C':
            sum = sum + 800
        else:
            sum = sum + hashmap[s[itr]]
    print(itr, s[itr], sum)

print(sum)
        
        
            
            
#print(sum)