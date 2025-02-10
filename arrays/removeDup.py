from typing import List


def removeDuplicates(nums: List[int]):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l,  nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))  # Output: [0, 1, 2, 3, 4]
