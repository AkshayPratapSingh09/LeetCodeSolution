nums = [-1,0,3,5,9,12]
target = 0

def search(nums,target):
    l = 0
    u = len(nums)-1

    while l<=u:
        mid = (l + u) // 2
        # print("Mid here is",mid)

        if nums[mid] == target:
            pos = mid
            return pos
        else:
            if nums[mid] < target:
                l = mid+1
                # print("L now changed to", l)
                
            else:
                u = mid-1
                # print("U now changed to", u)
    return False

# print(search(nums,target))

if search(nums,target):
    res = search(nums,target)
    print("Found at",res)
else:
    print("Not Found")
