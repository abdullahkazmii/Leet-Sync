class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums) -1:
            if nums[i] != nums[i+1]:
                i+=1
            elif nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
                i+=1
        
        pos = 0 
    
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0
        
        return nums
        