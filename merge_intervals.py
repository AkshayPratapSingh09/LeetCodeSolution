nums = [-1,0,1,2,-1,-4]
ans = []
for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j, len(nums)):
                    print(i,j,k)
                    if i!=j and i!=k and j!=k and (nums[i] + nums[j] + nums[k] == 0):
                        case = [nums[i], nums[j], nums[k]]
                        case.sort()
                        if case not in ans:
                            ans.append(case)
print(ans)
