from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res


nums = [2, 5, 1, 3, 4, 7, 8, 9]


print(shuffle(nums, 4))
