def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    for i in range(len(jewels)):
        for j in range(len(stones)):
            if jewels[i] == stones[j]:
                count += 1
            else:
                continue
    return count


jewels = "zx"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
