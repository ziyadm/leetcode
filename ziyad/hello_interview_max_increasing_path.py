"""
Problem Statement:
    
Given an m x n integers matrix, return the length of the longest increasing path in matrix. From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input:
- A 2D list matrix of integers where 1 <= matrix.length, matrix[i].length <= 200 and -10^9 <= matrix[i][j] <= 10^9

Output:
- An integer representing the length of the longest increasing path.

Example:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
"""
from typing import List

cache = dict()
class Solution:
    def path_length_from(self, starting_row: int, starting_col: int, matrix: List[List[int]]) -> int:
        cache_key = (starting_row, starting_col)
        if cache_key in cache:
            return cache[cache_key]
        stack = [(starting_row, starting_col, 1)]
        visited = set()
        max_path_length = 0

        while stack:
            row, col, length = stack.pop()

            if length > max_path_length:
                max_path_length = length

            for dx, dy in [(0,-1), (1,0), (0, 1), (-1,0)]:
                if 0 <= row + dx < len(matrix) and \
                   0 <= col + dy < len(matrix[0]) and \
                   matrix[row+dx][col+dy] > matrix[row][col] and \
                   (row+dx, col+dy) not in visited:
                    visited.add((row+dx, col+dy))
                    stack.append((row+dx, col+dy, length+1))
            
        cache[cache_key] = max_path_length
        return max_path_length

    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        longest_increasing_path_length = 0

        for row in range(len(matrix)):
            for col in range(len(matrix)):
                longest_increasing_path_length = max(
                    longest_increasing_path_length,
                    self.path_length_from(starting_row=row, starting_col=col, matrix=matrix))
        return longest_increasing_path_length

solution = Solution()
#assert solution.longest_increasing_path(matrix=[[9,9,4],[6,6,8],[2,1,1]]) == 4
#assert solution.longest_increasing_path(matrix=[[3,4,5],[3,2,6],[2,2,1]]) == 4
assert solution.longest_increasing_path(matrix=[[1,1,1],[1,1,1],[1,1,1]]) == 1