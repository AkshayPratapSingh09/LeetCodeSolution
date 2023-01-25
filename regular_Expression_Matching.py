def maxPalindromes(s: str, k: int) -> int:
        count = 0
        stack = []
        def isPalindrome(s):
            return s == s[::-1]
        
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                r = s[i:j]
                print(r)
                if isPalindrome(r):
                    print(r)
                    if len(r)>=k:
                        count = 0
                        for t in range(len(stack)):
                            if r in stack[t]:

                                print("case here:",r)
                                print("Stack here:",stack[t])
                                count += 1
                        if count == 0:
                            stack.append(r)
                        else:
                            continue
        return stack

s = "fttfjofpnpfydwdwdnns"
# print("fpnpf" in s)
k = 2
print(maxPalindromes(s,k))