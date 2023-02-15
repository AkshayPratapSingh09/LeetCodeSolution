# def maxNumOfSubstrings(s: str):
        
#         start, end = {}, {}
#         for i, c in enumerate(s):
#             end[c] = i
#             if c not in start:
#                 start[c] = i
#         # r will contain all minimal sub-intervals of the string that satisfy condition 2
#         r = []
#         stack = [] # stack will contain nested sub-intervals currently under consideration
#         for i, c in enumerate(s):

#             while stack and stack[-1][0] > start[c]:
#                 stack.pop() # Sub-interval does not contain first occurence of character c
                
#             if stack and stack[-1][1] < end[c]:
#                 while len(stack) > 1 and stack[-2][1] < end[c]:
#                     stack.pop()
#                 stack[-1][1] = end[c] # Left end of sub-interval must be extended
#             elif i == start[c] and (not stack or end[c] < stack[-1][1]) :
#                 stack.append([i, end[c]]) # i is potential start of minimal sub-interval

#             if stack and stack[-1][1] == i:
#                 r.append(stack[-1])
#                 stack.clear() # Minimal sub-interval found. All other sub-intervals on the stack containing it cannot be minimal
                
#         return [s[fro:to+1] for fro, to in r]

# s = "abaccdbbd"
# k = 3
# print(maxNumOfSubstrings(s))

print([1,2] + [3])