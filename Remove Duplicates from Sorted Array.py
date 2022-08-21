# def rem(g):
#     nums = [1,1,2]
#     ln = len(nums)
#     # print(ln)
#     b = list(set(nums))
#     ln2 = len(b)
#     # print(ln2)
#     # print()
#     x = ln-ln2
#     for i in range (x):
#         b.append("_")
#     # print(b)
#     return f"{ln2},",f"{b}"
# print(rem(10))

def removeDuplicates(nums):
        ln = len(nums)
        # print(ln)
        b = list(set(nums))
        ln2 = len(b)
        # print(ln2)
        # print()
        x = ln-ln2
        for i in range (x):
            b.append("_")
        # print(b)
        nums = b
        return b
nums = [1,1,2]
print(removeDuplicates(nums))