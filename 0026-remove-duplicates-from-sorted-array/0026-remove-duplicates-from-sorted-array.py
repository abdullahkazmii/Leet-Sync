class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_sorted = sorted(set(nums))  
        
        for i in range(len(unique_sorted)):
            nums[i] = unique_sorted[i]
        
        return len(unique_sorted)
    
        
