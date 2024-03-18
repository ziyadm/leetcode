"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == '.':
                    continue

                if value in rows[row] or value in cols[col] or value in squares[3 * (row // 3) + (col // 3)]:
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                squares[3 * (row // 3) + (col // 3)].add(value)

        return True

# Tests
solution = Solution()
assert solution.isValidSudoku(board=[["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]])
assert not solution.isValidSudoku(board= [["8","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]])