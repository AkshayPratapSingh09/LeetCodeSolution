s = "___4193 with words"
# ans = "4193"
# print(s[s.find(ans)-1])
ans = ""
for i in s:
    if ord(i)<58 and ord(i)>47:
        ans += i
# ans[]
if s[s.find(ans)-1] == "-":
    ans = "-"+ans
# print(ans)
print(int(ans))