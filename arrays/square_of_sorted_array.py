from math import sqrt
from typing import List


def square_sort_array(num: List[int]):
    # approach - 1
    square = []
    for i in num:
        square.append(i**2)
        square.sort()
    return square

    # approach - 2
    # squared = [x**2 for x in num]
    # return sorted(squared)

    # square = []
    # for i in range(num):


nums = [-3, 1, 4, 0, 1, 5, 9, 2, 6, 5]
sorted_nums = square_sort_array(nums)
print(sorted_nums)  # Output: [0, 1, 1, 2, 4, 5, 5, 9, 36, 81]

