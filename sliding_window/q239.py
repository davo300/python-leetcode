# 239. Sliding Window Maximum

# Topics: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

# Difficulty: Hard

# Recommended Time & Space Complexity:
# You should aim for a solution as good or better than O(nlogn) time 
# and O(n) space, where n is the size of the input array.

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()     # index
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
                
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
                
            r += 1

        return output


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))