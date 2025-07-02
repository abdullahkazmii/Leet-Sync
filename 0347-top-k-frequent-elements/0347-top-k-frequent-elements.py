from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for i in nums:
        #     count[i] = count.get(i,0)+1
        # sorted_dict = sorted(count)
        top_k = Counter(nums).most_common(k)
        result = []
        for item, _ in top_k:
            result.append(item)
        return result