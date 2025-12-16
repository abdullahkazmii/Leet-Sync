class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        total = 0

        for i in nums:
            total = total + i
            sums.append(total)
        return sums
