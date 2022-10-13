nums = [5,7,7,8,8,8,8,8,10]
target = 8
stack = []
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        stack = []
        if l == 0:
            return [-1,-1]
        if l == 1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
            
        if l>1:
            
            for i in range(0,len(nums)):
                if nums[i] == target:
                    if len(stack)==2:
                        stack.pop()
                        stack.append(i)
                    else:
                        stack.append(i)
            if len(stack)==1:
                stack.append(stack[0])
                return stack
            elif len(stack)==0: return [-1,-1]
            else:
                return stack
            