# 875. Koko Eating Bananas 
# Topics: Array, Binary Search, Weekly Contest 94
# Difficulty: Medium
# Time: You should aim for a solution with O(nlogm) time 
# Space: O(1) space, where n is the size of the input array, and m is the maximum value in the array.


from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles):     # for edge case 
            return max(piles)

        def hours_needed(speed: int) -> int:
            return sum(math.ceil(pile / speed) for pile in piles)
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left  # smallest k that works

        
if __name__ == "__main__":
    sol = Solution()
    piles = [30,11,23,4,20]
    h = 5
    print(sol.minEatingSpeed(piles, h))