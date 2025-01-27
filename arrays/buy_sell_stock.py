from typing import List


def maxProfit(prices: List[int]):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        print(f"While Loop L : {l} & R: {r}")
        if prices[l] < prices[r]:
            print(f"Price Loop L : {prices[l]} & R: {prices[r]}")
            profit = prices[r] - prices[l]
            print(f"While Loop Profit: {profit}")
            maxP = max(maxP, profit)
            print(f"MaxP: {maxP}")
        else:
            print(f"Else L : {l} & R: {r}")
            l = r
        print(f"Before R: {r}")
        r += 1
        print(f"After R: {r}")
    print("=========Max: ", maxP)
    return maxP


prices = [1, 2, 5, 4]
print(maxProfit(prices))
