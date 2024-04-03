""" 74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m \* n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
from typing import List
import unittest

class Solution:
    def target_found_in_col(self, matrix: List[List[int]], target: int, row: int) -> bool:
        num_cols = len(matrix[0])
        min_col, max_col = 0, num_cols - 1

        while min_col <= max_col:
            mid_col = (max_col + min_col) // 2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] > target:
                max_col = mid_col - 1
            else:
                min_col = mid_col + 1

        return False

    def find_row(self, matrix: List[List[int]], target: int) -> bool:
        last_col_index = len(matrix[0]) - 1
        min_row, max_row = 0, len(matrix) - 1

        while min_row <= max_row:
            mid_row = (max_row + min_row) // 2
            if matrix[mid_row][0] <= target and target <= matrix[mid_row][last_col_index]:
                return mid_row
            elif target < matrix[mid_row][0]:
                max_row = mid_row - 1
            else:
                min_row = mid_row + 1
            
        return None

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.find_row(matrix=matrix, target=target)
        if row is not None:
            return self.target_found_in_col(matrix=matrix, target=target, row=row)
        return False


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_found(self):
        self.assertEqual(self.solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3), True)

    def test_target_not_found(self):
        self.assertEqual(self.solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13), False)

if __name__ == '__main__':
    unittest.main()