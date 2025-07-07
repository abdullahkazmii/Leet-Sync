class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # count = 0
        # for i in range(len(jewels)):
        #     for j in range(len(stones)):
        #         if jewels[i] == stones[j]:
        #             count+=1
        #         else:
        #             continue
        # return count

        # jewelsMap, stonesMap = {}, {}
        # for i in range(len(jewels)):
        #     jewelsMap[jewels[i]] = jewelsMap.get(jewels[i], 0) + 1

        # for j in range(len(stones)):
        #     stonesMap[stones[j]] = stonesMap.get(stones[i], 0) + 1
        
        # if 

        jewelSet = set(jewels)
        count = 0
        for i in range(len(stones)):
            if stones[i] in jewelSet:
                count+=1
            else:
                continue
        return count
 