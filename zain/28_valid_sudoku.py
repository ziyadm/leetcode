class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_sets = [set() for i in range(9)]
        column_sets = [set() for i in range(9)]
        row_sets = [set() for i in range(9)]

        for row in range(9):
            for column in range (9):
                if board[row][column] == '.':
                    continue  

                if board[row][column] in column_sets[column]\
                or board[row][column] in row_sets[row]\
                or board[row][column] in box_sets[3 * (column // 3) + row // 3]:
                    return False
                
                column_sets[column].add(board[row][column])
                row_sets[row].add(board[row][column])
                box_sets[3 * (column // 3) + row // 3].add(board[row][column])
                
        return True                
