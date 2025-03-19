class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i - 1]
        else:
            nums[i] = nums[i]
        return nums