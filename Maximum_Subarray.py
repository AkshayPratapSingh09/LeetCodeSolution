nums = [-2,1,-3,4,-1,2,1,-5,4]
# lists = []
# max = 0
# # for i in range(len(nums)):
# #     print(i)
# for i in range(len(nums) + 1):
#         for j in range(i):
#             if sum(nums[j: i]) > max:
#                 max = sum(nums[j: i])
#                 # case = nums[j: i]
#             # lists.append(nums[j: i])
# # print(lists)
# print(max)
# # print(case)

def maxSubArray(nums):
        maxs = nums[0]
        sum = 0
        
        for i in nums:
            if sum < 0:
                sum = 0
            sum += i
            maxs = max(maxs,sum)
        return maxs
print(maxSubArray(nums))