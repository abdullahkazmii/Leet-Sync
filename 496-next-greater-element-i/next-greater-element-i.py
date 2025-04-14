class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for num in nums1:
            index = nums2.index(num)  
            next_greater = -1         
            for i in range(index + 1, len(nums2)): 
                if nums2[i] > num:
                    next_greater = nums2[i]
                    break
            result.append(next_greater)
        return result