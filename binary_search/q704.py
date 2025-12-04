# 704. Binary Search
# Topics: Array, Binary Search
# Difficulty: Easy
# Time: O(log(n))

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        low = 0             # index postions not elements
        hi = len(nums) - 1  # index postions not elements
        while low <= hi:
            mid = (low + hi) // 2       # index postions not elements
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                hi = mid - 1 
 
        return -1       # if target not found
        
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(sol.search(nums, target))