"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List

class Solution:
    def find_word(self, board: List[List[str]], word: str, row: int, col: int) -> bool:
        if board[row][col] != word[0]:
            return False

        stack = [(row, col, 0, set([(row,col)]))]

        while stack:
            row, col, word_index, visited = stack.pop()

            if word_index == len(word) - 1:
                return True

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                next_row, next_col = row + dx, col + dy
                if 0 <= next_row < len(board) and \
                   0 <= next_col < len(board[0]) and \
                   (next_row, next_col) not in visited and \
                   board[next_row][next_col] == word[word_index+1]:
                   new_visited = visited.copy()
                   new_visited.add((next_row, next_col))
                   stack.append((next_row, next_col, word_index + 1, new_visited))

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.find_word(board=board, word=word, row=row, col=col):
                    return True

        return False

# Tests
solution = Solution()
assert solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
assert solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
assert not solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
 