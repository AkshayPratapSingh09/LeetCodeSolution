low =3
high =7
count = 0
# while low <=high:
#     if low%2 != 0:
#         count += 1
#     # elif low%2==0:
#     #     continue
#     print(low)
#     low+=1
# print( count)
r = high - (low-1)
r = r//2
print(r)
if low%2 != 0:
    r +=1
# if high%2 != 0:
#     r +=1
print(r)