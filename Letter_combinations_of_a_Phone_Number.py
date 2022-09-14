
digit = "23"
dig = [int(x) for x in digit]


num = [x for x in range(2,10)]


ls = [
    ["a","b","c"], ["d","e","f"],
["g","h","i"],["j","k","l"],
["m","n","o"],["p","q","r","s"],
["t","u","v"],["w","x","y","z"]
]
letters = dict(zip(num,ls))
# print(letters[2][1]+letters[3][1])
st = ""
# g = len(dig)
# def combination():
result = []
st = ""
for r in dig:
    for j in range(len(letters[r])):
        for h in  range(len(letters[r])):
            st += letters[r][j]+ letters[r+1][h]
            print(st)
            if len(st)==len(dig)-1:
                print("This is the case",st)
                result.append(st)
                st =""
                # break
print(result)