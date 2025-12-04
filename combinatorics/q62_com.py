# 62. Using Combinatorics is fast!!
# Can also use dynamic programming this is cooler though
# each square of the board can be computed with the combination formula.
# Basically, its a modified combination formula for this specific problem, modified from n choose k
# "How many unique ways can I choose m - 1 movements down and n - 1 movements right 
# (in any order) from m + n - 2 total steps?"


import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)
    
if __name__ == "__main__":
    s = Solution()
    m = 5
    n = 5
    print(s.uniquePaths(m,n))