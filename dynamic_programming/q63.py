# 63. Unique Paths II
# Topics: Array, Dynamic Programming, Matrix
# m = rows, n = columns
# Time: O(n * m), Space: O(n)

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)       # length of the outer array, number of rows
        n = len(obstacleGrid[0])    # length of the first array element (row) = number of columns
        dp = [0] * n                # create dp[] array containing the current row
        dp[n - 1] = 1               # dp[] row is all we need to store in memory
  
        for row in reversed(range(m)):         
            for col in reversed(range(n)):      
                if obstacleGrid[row][col]:  # if we find an obstacle, set it dp[col] = 0
                    dp[col] = 0
                elif col + 1 < n:           # if we are not at edge, we can add the paths together
                    dp[col] = dp[col] + dp[col + 1]

        return dp[0]    # return the total at dp[0]



if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0,0,0],
                    [0,1,0],    # obstacle = 1
                    [0,0,0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))