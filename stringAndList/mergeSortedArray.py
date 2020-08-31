def merge(nums1, m, nums2, n):
    """
    append elements of nums2 to nums1 then sort nums1 => take O(aloga) a = m+n
    m : number of elements in nums1, n: number of element in nums2
    """
    for i in range(n):
        if m+i < len(nums1):
            nums1[m+i] = nums2[i]
        else:
            nums1.append(nums2[i])
    nums1.sort()
    
nums1 = [1,2,3,0,0,0]
nums2 = [2, 5, 6]

merge(nums1, 3, nums2, 3)
print(nums1)
        

nums1 = [1,2, 0]
nums2 = [2, 5, 6]

merge(nums1, 2, nums2, 3)
print(nums1)
        
