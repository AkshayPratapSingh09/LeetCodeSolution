dict1 = ["loves","coding","pep","pepcoding","ice","cream","icecream","man","go","mango"]
string1 = "pepcodinglovesmangoicecream"
l = len(string1)
print(l)
count = 0
for i in range(l+1):
    st = string1[i:l]
    print(st)
    for j in range(len(st)+1):
        st2 = st[0:j]
        print(st2)
        if st2 in dict1:
            count += 1
print("Word Used are",count)