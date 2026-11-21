numbers = [-5,-3,0,2,4,6,8]
target = 5

lPointer = 0
rPointer = len(numbers) - 1


while lPointer <= rPointer:

    print(lPointer, rPointer)

    if numbers[lPointer] + numbers[rPointer] == target:
        print("Answer: ", [lPointer+1, rPointer+1])
        break
    if numbers[lPointer] + numbers[rPointer] > target:
        rPointer -= 1
    elif numbers[lPointer] + numbers[rPointer] < target:
        lPointer += 1     
    elif numbers[rPointer] > target:
        rPointer -= 1   
