# print(height[1][1])
# pairs = []
# def sub_lists(l):
#     for i in range(len(l)):
#         for j in range(len(l)):
#             e = [l[i], l[j]]
#             # if len(e) == 2:
#             pairs.append(e)
#     print(pairs)

# sub_lists(height)

#         e = [l[i], l[j]]
#         # if len(e) == 2:
#         pairs.append(e)
# print(pairs)

# for i in range(len(height)):
#     for j in range(len(height)):
#         dif = j-i
#         breadth = height[j][0] - dif
#         if height[i][1]>height[j][1]:
#             length = height[j][1]
#         else:
#             length = height[i][1]
#         area = length * breadth
#         areas.append(area)
        # heights.append([height[i][1],height[j][1]])

# heights = []
# areas = []
# height = list(enumerate(height, 0))
# print(height)
# print(areas)
# print(heights)












height = [1,8,6,2,5,4,8,3,7]

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
res = 0
for l in range(len(height)):
    for r in range(l+1, len(height)):
        length = r-l
        if (height[l]>height[r]):
            breadth = height[r]
        else:
            breadth = height[l]
        area = length * breadth
        res = max(res, area)

print(res)

            










