# 51. N-Queens
# Difficulty: Hard
# Time: O(n!)
# Space: O(n^2)
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set() 
        posDiag = set()
        negDiag = set()
        
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:  # base case
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    n = 4

    print(sol.solveNQueens(n))
    # [[
    # ".Q..",
    # "...Q",
    # "Q...",
    # "..Q."
    # ],
    # 
    # [
    # "..Q.",
    # "Q...",
    # "...Q",
    # ".Q.."
    #]]
    