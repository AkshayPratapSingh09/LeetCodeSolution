nums1 = [1,2,2,1]
nums2 = [2,2]
l3 = []
def solution(nums1,num2):
    for i in nums1:
        for j in nums2:
            if i == j:
                l3.append(i)
    return list(set(l3))
