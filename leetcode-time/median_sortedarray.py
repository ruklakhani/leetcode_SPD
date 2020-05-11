def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums = nums1 + nums2
    nums.sort()
    length = len(nums)
    if length % 2 == 0:
        left = nums[(length//2)-1]
        right = nums[length//2]
        return (left+right) / float(2)
    else: 
        return nums[length//2]

'''
O(n) because we are using sort()
'''