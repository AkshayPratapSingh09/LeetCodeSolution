a = [78,65,43,23,1]

def reversal(a):
    n = len(a)
    rev = [0] * n
    # print(rev)
    for i in range(n):
        rev[n-i-1] = a[i]
    print(rev)

reversal(a)
