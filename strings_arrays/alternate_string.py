word1 = 'abc'
word2 = 'pqrst'

len_W1= len(word1)
len_W2 = len(word2)

i, j = 0, 0
curr_word = 1
s = []

while i < len_W1 and j < len_W2:

    if curr_word == 1:
        s.append(word1[i])
        i+=1
        curr_word = 2
    else:
        s.append(word2[j])
        j+=1
        curr_word = 1
    
while i < len_W1 :
    s.append(word1[i])
    i+=1

while j < len_W2 :
    s.append(word2[j])
    j+=1

print(''.join(s))

