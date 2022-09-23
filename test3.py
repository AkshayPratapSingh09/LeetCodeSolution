s = "abcabcbb"

def lengthOfLongestSubstring(s):
      
        if len(s) == 0: return 0
        stack = {}
        l, r = 0, 0
        ans = 1
        while r < len(s):
            if s[r] in stack:
                l = max(l,stack[s[r]]+1)
            ans = max(ans, r - l + 1)
            stack[s[r]] = r
            r += 1
            print(l, r, ans)
        return ans
print(lengthOfLongestSubstring(s))
    