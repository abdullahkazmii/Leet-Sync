from typing import List


# def reverseString(s: List[str]):
#     """
#     Do not return anything, modify s in-place instead.
#     """
#     rev = s[::-1]
#     return rev


# print(reverseString(s))


# two pointer approach
# def reverseString2(s: List[str]):
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#     return s


# s = "Abdullah"
# print(reverseString2(s))


# reverse using stack
def reverseString3(s: List[str]):
    stack = []
    for char in s:
        stack.append(char)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1
    return s


name = "abdullaH"
print(reverseString3(name))
