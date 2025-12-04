# Q39. Combination Sum
# Difficulty: Medium
# this is the optimal solution version,
# Time: O(2^{t/m})
# Space: O(t/m)
# Where t is the target value and m is the minimum value in nums.

'''
Question: How is dfs similar to backtracking algorithm?
Yes, backtracking is often described as a refined application of
Depth-First Search (DFS). Both algorithms explore a tree-like structure
of possibilities, but backtracking adds a crucial element: pruning.

However this dfs DOES include pruning!!!!
So it is a backtracking algorithm
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                cur.append(candidates[j])
                dfs(j, cur, total + candidates[j])
                cur.pop()
                
        dfs(0, [], 0)
        return res





if __name__ == "__main__":
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(s.combinationSum(candidates, target))