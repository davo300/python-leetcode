# 131. Palindrome Partitioning
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
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])     # or part.copy()
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


if __name__ == "__main__":
    sol = Solution()

    s = "aaab"

    print(sol.partition(s))
