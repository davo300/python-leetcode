# 90. Subsets II
# Difficulty: Medium

'''
DFS:	
A general graph/tree traversal algorithm. 
Think of it as exploring as far as possible down one path before backing up.
Backtracking:
A form of DFS where you build a solution incrementally, 
and undo (backtrack) when you hit an invalid or complete path. 
Its DFS + undoing choices.
'''

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2]
    print(s.subsetsWithDup(nums))
