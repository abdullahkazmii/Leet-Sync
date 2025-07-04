class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_list = []
        for x in nums:
            squared_list.append(x**2)
        return sorted(squared_list)