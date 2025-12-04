# 74. Search a 2D Matrix
# Topics: Array, Binary Search, Matrix
# Difficulty: Medium
# Time: O(log(n*m))

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(nums, target):
            low = 0             # index postions not elements
            hi = len(nums) - 1  # index postions not elements
            while low <= hi:
                mid = (low + hi) // 2       # index postions not elements
                if nums[mid] == target:
                    return nums[mid]      # use element value not index this time.
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    hi = mid - 1 
    
            return -1       # if target not found
        
        # main logic
        for r in matrix:    # r1 = [1, 3, 5, 7], r2 = [10,11,16,20], r3 = [23,30,34,60]
            ans = binarySearch(r, target)
            if ans == target:       # ans == 3
                return True
        
        return False        # if target is not found in any row

        
if __name__ == "__main__":
    sol = Solution()
    matrix = [[ 1, 3, 5, 7],
              [10,11,16,20],
              [23,30,34,60]]
    target = 3
    print(sol.searchMatrix(matrix, target))