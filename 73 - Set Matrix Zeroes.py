"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_change = set()
        cols_to_change = set()

        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    rows_to_change.add(i)
                    cols_to_change.add(j)

        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if i in rows_to_change or j in cols_to_change:
                    matrix[i][j] = 0

        return matrix
