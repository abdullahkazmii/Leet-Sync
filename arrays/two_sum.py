from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in nums:
        for j in i + 1:
            if nums[i] + nums[j] == target:
                return i, j
