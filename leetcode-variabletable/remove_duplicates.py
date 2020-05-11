def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    index = 0 
    for num in nums[1:]:
        ex_num = nums[index]
        index += 1 
        if num == ex_num:
            del nums[index]
            index -= 1
    return nums
print(removeDuplicates([1,1,2,3]))

"""
var: value
nums = [1,1,2,3]
index = 0
ex_num = 1 
index = 1
nums = [1,2,3]
index = 0
ex_num = 1 
index = 1
ex_num = 2
index = 2 
ex_num = 3 
index = 3
return: [1,2,3]
            
"""




    