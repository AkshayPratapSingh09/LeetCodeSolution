s = "au"
if len(s)==1:
     print(1)
else:
    ans = 0
    stack = []
    count = 0
    for i in s:
        if i in stack:
            ans = max(ans, len(stack))
            stack = []
        count += 1
        stack.append(i)
        ans = max(ans, len(stack))
        print(stack)
    print(ans)
