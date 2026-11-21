
nums = [2,3, 4]
target = 6
hashmap = {}
for x in range(len(nums)):
    print(hashmap)
    num2 = target - nums[x]
    if num2 in hashmap:
        print("answer: ",[x,hashmap[num2]])
        break
    hashmap[nums[x]] = x

