s = "MCMXCIV"

hashmap = {'I': 1, 
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000 }

sum = 0 
for itr in range(len(s)):
    if itr == 0:
        sum = hashmap[s[itr]]
    if itr != 0:
        if hashmap[s[itr]] > hashmap[s[itr-1]]:
            sum = sum + hashmap[s[itr]] - (hashmap[s[itr-1]]*2) 
        else:
            sum = sum + hashmap[s[itr]]

return sum