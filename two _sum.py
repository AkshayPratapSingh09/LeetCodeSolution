a = [1,2,3,5,7]
b = []
def fuc(a,target):
    sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == target:
                return [i,j]

print(fuc(a,6))



# print(b)
        # sum += a[i]
        # b.append(i)
        # # if sum==target:
        # print(i)