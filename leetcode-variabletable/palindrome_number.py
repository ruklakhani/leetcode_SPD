def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    num = str(x)
    result = num[::-1]
    if num == result:
        return True
    return False

# print(isPalindrome(32123))

"""

___________|___________
    num    | '32123'
    result | '32123'
           |
            
"""