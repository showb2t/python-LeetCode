x= 10

int_str = str(x)

print(int_str[::-1])


str_len = len(int_str)
print("str_len: ", str_len)
for p in range(round(str_len/2)):
    if int_str[p] != int_str[str_len-p-1]:
        print(False)

print(True)