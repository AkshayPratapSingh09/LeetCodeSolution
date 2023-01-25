s = "tree"
count = {}
for c in s:
    count[c] = 1 + count.get(c, 0)
print(count)

sorted_char = sorted(count , key=lambda x:count[x], reverse=True)
print(sorted_char)
# res = ''
# for c in sorted_char:
#     res += c * count[c]
    
# # print(res)