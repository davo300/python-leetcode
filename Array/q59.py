# 59. Spiral Matrix II
# Topics: Array, Matrix, Simulation
# two dimensional matrix is defined as:
# matrix[row][column]
# Want to generate a matrix in spiral order
'''matrix =  [[1,2,3],
              [8,9,4],
              [7,6,5]]'''
# this appends 2D matrix elements in to a result 1D array in spiral order following that pattern
# we use for loops to get the specific elements that follows the pattern for arrays of size n x n
# number of rows = n = number of columns.

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]   # generate n x n matrix of 0's
        # we use the 4 pointer technique
        left_col, right_col = 0, n - 1 
        top_row, bottom_row = 0, n - 1
        val = 1

        while left_col <= right_col:  # once the col pointers cross, we have numbered the spiral matrix correctly.
            # fill in every val in top row -> we normally put the last central elements of the spiral here
            for col in range(left_col, right_col + 1): # two dimensional matrix is defined as:
                matrix[top_row][col] = val             # matrix[row][column]
                val += 1
            top_row += 1
            # fill in every val in right col
            for row in range(top_row, bottom_row + 1):
                matrix[row][right_col] = val
                val += 1
            right_col -= 1
            # fill in every val in bottom row (reverse order)
            for col in range(right_col, left_col - 1, -1):
                matrix[bottom_row][col] = val
                val += 1
            bottom_row -= 1
            # fill in every val in left col (reverse order)
            for row in range(bottom_row, top_row - 1, -1):
                matrix[row][left_col] = val
                val += 1   
            left_col += 1
        
        return matrix
        

if __name__ == "__main__":
    s = Solution()
    n = 12  
    matrix = s.generateMatrix(n)
    for row in matrix:
        print(row)
    
