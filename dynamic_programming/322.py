# 322. Coin Change
# Toics: Array, DP, BFS

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    sol = Solution()
    coins = [1,3,4,5]
    amount = 7
    print(sol.coinChange(coins, amount))