class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        column_sets = [set() for i in range(9)]
        box_sets = [set() for i in range(9)]
        for row in range(0, 8):
            for column in range(0, 8):
                current = board[row][column]
                if current == '.':
                    continue
                
                box = 3 * (row // 3) + (column // 3)

                if current in row_sets[row] or \
                current in column_sets[column] or \
                current in box_sets[box]:
                    return False
                else:
                    row_sets[row].add(current)
                    column_sets[column].add(current)
                    box_sets[box].add(current)
        return True
