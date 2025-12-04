# 37. Sudoku Solver
# Difficulty: Hard
# Topics: Array, Hash Table, Backtracking, Matrix

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        # Initialize sets with existing board numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    # square_id used to check each of the 9 sub grids and its used to check the squares set for duplicates
                    # By multiplying the row block by 3 and adding the column block, you get a unique square_id from 0 to 8.
                    # square_id:[0][1][2]
                               #[3][4][5]
                               #[6][7][8] 
                    square_id = (i // 3) * 3 + j // 3
                    squares[square_id].add(num)  # add square_id's to the squares set

        solved = False

        def backTrack(i, j):
            nonlocal solved
            if i == 9:  # base case
                solved = True
                return
            # logic used to iterate through each row and column
            new_i = i + (j + 1) // 9  # only equals 1 when 9 // 9 = 1
            new_j = (j + 1) % 9     # new_j + 1 for every column until 9 % 9 == 0 -> means new row

            if board[i][j] != '.':
                backTrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    square_id = (i // 3) * 3 + j // 3   # find the current square_id aka sub square
                    if num not in rows[i] and num not in cols[j] and num not in squares[square_id]:  # check if current number is not in the sets
                        board[i][j] = str(num)
                        rows[i].add(num)
                        cols[j].add(num)
                        squares[square_id].add(num)

                        backTrack(new_i, new_j)

                        if not solved:
                            board[i][j] = '.'
                            rows[i].remove(num)
                            cols[j].remove(num)
                            squares[square_id].remove(num)

        backTrack(0, 0)


if __name__ == "__main__":
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]


    '''
    board =[["8","3",".",".","7",".",".",".","."]
           ,["6",".",".","1","9","5",".",".","."]
           ,[".","9","8",".",".",".",".","6","."]
           ,["8",".",".",".","6",".",".",".","3"]
           ,["4",".",".","8",".","3",".",".","1"]
           ,["7",".",".",".","2",".",".",".","6"]
           ,[".","6",".",".",".",".","2","8","."]
           ,[".",".",".","4","1","9",".",".","5"]
           ,[".",".",".",".","8",".",".","7","9"]]
    ''' 
    s.solveSudoku(board)

    # print the board after it's been solved
    for row in board:
        print(" ".join(row))
