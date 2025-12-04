# 121. Best Time to Buy and Sell Stock
# Topics: Array, Dynamic Programming, Sliding Window?
# Difficulty: Easy
# Time: You should aim for a solution with O(n) time
# Space: O(1) space, where n is the size of the input array.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


if __name__ == "__main__":
    sol = Solution()
    # prices = [10,1,5,6,7,1]   # output = 6
    # prices = [10,8,7,5,2]       # output = 0
    prices = [2,1,2,1,0,1,2]
    print(sol.maxProfit(prices))