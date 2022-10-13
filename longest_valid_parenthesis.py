# a,b = "(", ")"
# s= "()()"
# stack = []
# count = 0
# for c in s:
#     stack.append(c)
#     if stack[0] ==a and stack[-1]==b:
#         stack.pop(0)
#         stack.pop(-1)
#         count+=1

# print(stack)
# print(count)


s = ")()())"
a,b = "(", ")"
stack = []
count = 0
for c in s:
    stack.append(c)
    if stack[0]==b:
        stack.pop(0)
        print(stack)
    if len(stack)>0:    
        if stack[0] ==a and stack[-1]==b:
            stack.pop(0)
            stack.pop(-1)
            count+=2
print(count)

