s = "barfoothefoobarman"
words = ["foo","bar"]


# from itertools import permutations
# final = []
# res = []
# count = 0
# for i in range(len(list(permutations(words)))):
#    final.append("".join(list(permutations(words))[i]))

# for i in range(0,len(s)-len(final[0])+1):
#     case = s[i:len(final[0])+ count]
#     print(case)
#     if case in final:
#         res.append(i)
#     count +=1
# print(res)

out = []
words.sort()
len_w = len(words[0])
combined_len =  len_w * len(words)
for i in range(len(s)-combined_len+1):
    sample = s[i:i+combined_len]
    print(sample)

    valid = True
#print('sample:', sample)

temp_word = []
for j in range(len(words)):
    #  print(sample[j*len_w:j*len_w+len_w])
    temp_word.append(sample[j*len_w:j*len_w+len_w])

print(temp_word)