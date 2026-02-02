"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        arr = range(0, x)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2

            if arr[m] * arr[m] == x:
                return arr[m]

            elif arr[m] * arr[m] < x:
                l = m + 1

            else:
                r = m - 1

        return r
