nums = [0,0,0]
ans = []

for i in range(0,len(nums)):
    for j in range(len(nums)-1):
        for k in range(len(nums)-2):
            if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                case = [nums[i],nums[j],nums[k]]
                case.sort()
                if case in ans:
                    continue
                ans.append(case)
print(ans)
