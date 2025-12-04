# 215. Kth Largest Element in an Array


from typing import List
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":

    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.findKthLargest(nums, k))  