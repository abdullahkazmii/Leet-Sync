from typing import List


def runningSum(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if i > 0:
            nums[i] += nums[i - 1]
        else:
            nums[i] = nums[i]
    return nums


nums = [1, 2, 3, 4]
print(runningSum(nums))
