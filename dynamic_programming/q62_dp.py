# 62. Unique Paths
# Topics: Math, Dynamic Programming, Combinatorics
# m = rows, n = columns
# Time: O(m * n)
# Memory: O(n) -> length of a row

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n   # set bottom row to all 1's
        
        for i in range(m - 1):  # don't include bottom row
            newRow = [1] * n    
            for j in range(n - 2, -1, -1):  # start at col - 2, to -1, in reverse order
                newRow[j] = newRow[j + 1] + row[j]      # add bottom and right rows together
            row = newRow
        return row[0]


if __name__ == "__main__":
    s = Solution()
    m = 20
    n = 20
    print(s.uniquePaths(m,n))
