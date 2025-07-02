from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]
        return [item[0] for item in sorted_items]
        