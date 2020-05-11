def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)): 
        for n in range(len(nums)):
            if nums[i] + nums[n] == target:
                if i != n:
                    return [i, n]

"""
for each number in nums, we compare that number 
to the other numbers in nums using 2 for loops
in the for loops we check that two numbers add up 
to the target number
if they are not the same number, and they add up to the target, 
return the indices
"""