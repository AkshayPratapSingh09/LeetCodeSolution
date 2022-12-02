a = 9669
b = str(a)
for i in range(len(b)):
    # print(b[i])
    if b[i] !=9:
        # b[i] = 9
        print(b[:i])
        print(b[i+2:len(b)])
        b = b[:i] + "9" + b[i+2:len(b)]
        # print(b)
        break
# print((b))