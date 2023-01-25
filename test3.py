sentence = "eetcode"
words = sentence.split()
ptr = 0
ptr2 = 0
count = 0
for i in range(len(words)):
    ptr = i
    ptr2 = i+1
    if ptr ==len(words)-1:
        ptr2 =0
    if words[ptr][-1] == words[ptr2][-1]:
        count +=1
print( count == len(words))