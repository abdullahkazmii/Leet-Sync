from typing import List


def reverseString(s: List[str]):
    """
    Do not return anything, modify s in-place instead.
    """
    rev = s[::-1]
    return rev


s = "abdullah"
print(reverseString(s))
