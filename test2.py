from cmath import inf


def maxSubArray(nums):
    case = -inf
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            print("i is",i,"j is ",j)
            sum += nums[j]
        case = max(case, sum)
    return case

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))