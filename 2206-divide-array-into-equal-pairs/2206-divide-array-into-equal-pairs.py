class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
        
        for key in freq:
            if freq[key] % 2 != 0:
                return False
        return True
        