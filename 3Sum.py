num = [1,2,3,4,5]
ls = [[i,j,k] for i in num for j in num for k in num]
ans = []
for element in ls:
    if sum(element) == 0:
        ans.append(element)
# print(ls)