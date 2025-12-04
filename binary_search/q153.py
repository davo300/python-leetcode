# 153. Find Minimum in Rotated Sorted Array
# Topics: Array, Binary Search
# Difficulty: Medium
# Time: You should aim for a solution with O(logn) time and 
# Space: O(1) space, where n is the size of the input array.



from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]       # first element 
        l, r = 0, len(nums) - 1         # first and last indexes

        while l <= r:
            if nums[l] < nums[r]:           # inflection point found
                res = min(res, nums[l])     # if left number is less than right number, find current min, and break out
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1               # find inflection point
            else:
                r = m - 1
        
        return res



if __name__ == "__main__":
    sol = Solution()
    nums = [3,0,1,2]      # problem is, its not sorted, its been rotated 3 times
    print(sol.findMin(nums))