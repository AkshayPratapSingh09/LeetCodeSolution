class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if i in stack:
                stack.remove(i)
            else:
                stack.append(i)
        return stack[0]
    
            
            