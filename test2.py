def findMedianSortedArrays(nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        print(l)
        if l ==0:
            return
        if l%2 ==0:
            print(((l+1)/2)+1)

        if l%2 !=0:
            print(((l+1)/2)) 
            print((int((l+1)/2)+1)/2)

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))