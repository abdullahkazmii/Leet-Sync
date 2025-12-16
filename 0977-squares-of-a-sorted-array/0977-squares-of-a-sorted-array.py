class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_array = []
        for i in range(len(nums)):
            sq = nums[i] * nums[i]
            squared_array.append(sq)
        
        return sorted(squared_array)



