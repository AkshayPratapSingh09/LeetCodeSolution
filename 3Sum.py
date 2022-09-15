num = [1,2,3,4,5]
# ls = [[i,j,k] for i in num for j in num for k in num]
# ans = []
# for element in ls:
#     if sum(element) == 0:
#         ans.append(element)
# print(ls)

numbers = [-1,0,1,2,-1,-4]
target = 0
tar = []
i, j, k = 0, len(numbers)-1, len(numbers)-2
while i > j and k>j:
    if numbers[i] + numbers[j] + numbers[k] == 0:
        case = [numbers[i],numbers[j],numbers[k]]
        tar.append(case)
        if sum > target:
            k-=1
            j-=1
        elif sum <target:
            i += 1
print(tar)