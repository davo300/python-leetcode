# 40. Combination Sum II
# Difficulty: Medium
# Time and Space Complexity:
# You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the size of the input array.

'''
Question: How is dfs similar to backtracking algorithm?
Yes, backtracking is often described as a refined application of
Depth-First Search (DFS). Both algorithms explore a tree-like structure
of possibilities, but backtracking adds a crucial element: pruning.

However thid dfs DOES include pruning!!!!
So it is a backtracking algorithm

the goal of this problem is the same as combinationSum part 1 but, we
cannot use the same index more than once.
'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:   # base case
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()
            
        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(s.combinationSum2(candidates, target))