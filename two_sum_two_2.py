#Compeleted


numbers = [2,7,11,15]
target = 9
s, l = 0, len(numbers)-1
while l > s:
    sum = numbers[s] + numbers[l]
    if sum > target:
        l-=1
    elif sum <target:
        s += 1
    else:
        case = [s+1,l+1]
print(case)