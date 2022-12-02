s = "bookers"
first = s[:len(s)//2]
second = s[len(s)//2:]
# print(first)
# print(second)
firstv = 0
secondv = 0
for i in range(len(s)):
    if i<len(s)//2:
        if s[i] in ["a", "e", "i","o","u",'A', 'E', 'I', 'O', 'U']:
            firstv +=1
    else:
        if s[i] in ["a", "e", "i","o","u",'A', 'E', 'I', 'O', 'U']:
            secondv +=1
        # print("Second Half")
        # print(s[i])
print(firstv)
print(secondv)
