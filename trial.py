
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
st = ""
# for r in dig:
for r in dig:
    for j in letters[r][range(10)]:
# def func(r,j):
        st += letters[r][j]
        print(st)
    if len(st)!=len(dig):
        r = r + 1
       
# func(2,0)
        # func()

