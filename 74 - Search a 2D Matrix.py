"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # If outside the bounds of the matrix the return True/False
        if target < matrix[0][0]:
            return False
        if target > matrix[n-1][m-1]:
            return False

        # Column search
        cl, cr = 0, n - 1
        while cl <= cr:
            cm = (cl + cr) // 2
            if matrix[cm][-1] == target:
                return True
            elif matrix[cm][-1] < target:
                cl = cm + 1
            elif matrix[cm][-1] > target:
                cr = cm - 1
        
        # Row search
        rl, rr = 0, m - 1
        while rl <= rr:
            rm = (rl + rr) // 2
            if matrix[cl][rm] == target:
                return True
            elif matrix[cl][rm] < target:
                rl = rm + 1
            elif matrix[cl][rm] > target:
                rr = rm - 1

        return False
