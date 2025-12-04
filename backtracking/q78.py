# 78. Subsets
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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))
