# [74] Search a 2D Matrix
"""Solution 1
we know the 2d array is sorted increasingly and we have to solve in log(m*n)
so we can't brute force search the whole thing
We can loop through each row in the array, check if the last value is greater than
or equal to the target value, if it is, check through that row. Otherwise
check through next rows"""
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if target in row:
                return True
        return False