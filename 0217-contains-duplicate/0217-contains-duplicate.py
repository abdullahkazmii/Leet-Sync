class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num]=1
        return False

        
        

        