from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = 0
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
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

# Call the method correctly
if __name__ == "__main__":
    n = 9
    solution = Solution()
    ans = solution.solveNQueens(n)
    print(ans)
