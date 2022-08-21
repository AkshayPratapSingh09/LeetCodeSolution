# #trailing zeroes
# count = 0
# a = 123040060000
# i = 0
# b = a
# while i==0:
#     b = b/10
#     # print(b)
#     i = b%10
#     # print(i)
#     b = b
#     # print(b)
#     count += 1
# print(count)

# factorial
fact = 1

for i in range(1,n+1):
    fact = fact * i
print(fact)

def recr(n):
    if n == 0 or n==1:
        return 1

    else:
       return recr(n-1) *recr(n)

