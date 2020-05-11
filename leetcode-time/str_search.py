def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if haystack == needle:
        return 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i 
    return -1
                
"""
time complexity: O(n)
depends on the length of haystack 
"""