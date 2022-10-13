nums1 = [1,3]
nums2 = [2]
l = len(nums1)

nums1.extend(nums2)
nums1.sort()
# if len(nums1) ==0:
#     return
if l%2 ==0:
    return nums1[((l+1)/2)+1]

if l%2 !=0:
    return (nums1[((l+1)/2)+1] +nums1[((l+1)/2)+2])/2

