num = [-1,0,1,2,-1,-4]
ls = [[i,j,k] for i in num for j in num for k in num if i != j and i != k and j != k]
ans = []
for element in ls:
    if element[0] + element[1] + element[2] == 0:
        element.sort()
        if element in ans:
            continue
        ans.append(element)
    

# print(len(ls))
print(ans)