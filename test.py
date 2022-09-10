nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums1.sort()
nums1 = list(set(nums1))
nums2.sort()
nums2 = list(set(nums2))
nums1.extend(nums2)
if nums1[0] == 0:
    nums1.remove(0)
print(nums1)