def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x = str(x)
    reversed_num = x[::-1]
    str_to_int = int(reversed_num)
    return str_to_int

print(reverse(123))

"""
turn x into a string so we can reverse it 
reverse the string 
turn the reversed string into an integer 
return the reversed integer 
"""
