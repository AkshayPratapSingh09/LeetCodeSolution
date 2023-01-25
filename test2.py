s = "leetcode"
words = ["leet", "code"]
dp = [False] * (len(s)+1)
dp[len(s)] = True
print(dp)

for i in range(len(s) -1, -1,-1):
    print(i)
    for w in words:
        print("Word here:",w,"  len here:",len(w))
        print(s[i:i+len(w)])
