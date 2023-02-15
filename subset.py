# nums = [1,2,3]
# subsets = [[]]

# for num in nums:
#     print("Case here",num)
#     print("Subset right  now ->",len(subsets))

#     for i in range(len(subsets)):
#         print("index here ->",i)
#         print("subsets",subsets)
#         currSubset = subsets[i]
#         print("Index ->",currSubset)
#         case = currSubset + [num]
#         subsets.append(case)
#         print("subsets",subsets)
# print( subsets)
# print([1,2,3] + [56])

a = [1,2,3]

ans = [[1],[2],[3],[1,2],[2,3],[1,2,3],[1,3],[]]

res = [[]]

for i in range(len(a)):
    for r in range(len(res)):
        case = res[r] + [a[i]] 
        res.append(case)
        # print("case",case)
print(res)


# print(res)
