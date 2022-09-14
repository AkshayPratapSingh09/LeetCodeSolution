conv = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ans = 0
last = 0
inp = "LVIII"
# XIV
for i in inp:
    # if conv[i] > last:
        # ans = ans - 2*last + conv[i]
        # print("Ans op:",ans)
    ans = ans + conv[i]
    print(ans)
    print("last:",last)
    print("Value", conv[i])
    if conv[i] > last:
        ans = ans - 2*last
    last = conv[i]
print(ans)