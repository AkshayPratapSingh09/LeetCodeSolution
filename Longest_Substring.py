s = "abcabcbb"
ans = 0
count = 0
pre = 0 
for i in s:
    if i != pre:
        print("Checking If",i," =",pre)
        count += 1
        print("Count here is:",count)
        ans = max(ans,count)
        print("Ans here is:",count)
        pre = i
    else:
        count = 0
print(ans)