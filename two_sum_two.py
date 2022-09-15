numbers = [2,7,11,15]
target = 9

# tar = [numbers[i]+ numbers[j] for i in range(len(numbers)) for j in range(len(numbers)-1)]
# tar = [[i,j] for i in numbers for j in numbers[1:] if i!=j]
# print(tar)
tar = []
for i in range(0,len(numbers)):
    for j in range(len(numbers)-1):
        if i == j:
            continue
        print("i is",i,"j is",j)
        if numbers[i] + numbers[j] == target:
            # tar.append([numbers[i],numbers[j]])
            case = [i+1,j+1]
            case.sort()
            if case in tar:
                continue
            else:
                tar.append([i+1,j+1])

print(tar)


