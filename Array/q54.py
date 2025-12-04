# 54. Spiral Matrix
# Topics: Array, Matrix, Simulation
# two dimensional matrix is defined as:
# matrix[row][column]
# for 
'''matrix =  [[1,2,3],
              [4,5,6],
              [7,8,9]]'''
# this appends 2D matrix elements in to a result 1D array in spiral order following that pattern
# we use for loops to get the specific elements that follows the pattern for arrays of size m x n
# m = number of rows, n = number of columns.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # we use the 4 pointer technique
        left_col, right_col = 0, len(matrix[0])  # len([1,2,3]) == 3 == right_col
        top_row, bottom_row = 0, len(matrix)     # bottom_row == 3
        
        while left_col < right_col and top_row < bottom_row:
            # get every i in the top_row row -> we normally get the last central elements of the spiral here
            for i in range(left_col, right_col): # two dimensional matrix is defined as:
                res.append(matrix[top_row][i])   # matrix[row][column]
            top_row += 1
            # get every i in the right_col col
            for i in range(top_row, bottom_row):
                res.append(matrix[i][right_col - 1])
            right_col -= 1
            if not (left_col < right_col and top_row < bottom_row):
                break
            # get every i in the bottom_row row
            for i in range(right_col - 1, left_col - 1, -1):
                res.append(matrix[bottom_row - 1][i])
            bottom_row -= 1
            # get every i in the bottom_row left_col col
            for i in range(bottom_row - 1, top_row - 1, -1):
                res.append(matrix[i][left_col])
            left_col += 1
        
        return res



if __name__ == "__main__":
    s = Solution()
    matrix1 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    print("Matrix1")
    print(s.spiralOrder(matrix1))

    matrix2 = [[1, 2,  3,  4],
               [5, 6,  7,  8],
               [9, 10, 11,12]]
    print("Matrix2")
    print(s.spiralOrder(matrix2))