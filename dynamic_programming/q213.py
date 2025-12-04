# 213. House Robber II

from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1])) # So nums[1:] = the list without its first element.

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,2]
    print(sol.rob(nums))