# [120] Triangle
"""Solution 1
We can use a recursive function to basically compute all the paths and then
return the smallest one. The function for each node branches into
2 nodes below it which should return, in any instance of the function
the function takes smallest valuee returned from the 2 calls and returns
that
Edge : 1 level : return the single number?
Issue : Timed out

Solution 2
We start from the bottom of the array with a loop.
Each row for each numbjer we check the numbers below it and add the smaller one
to it and then move up until we reach the top which gives us the answer. 
This should work faster as previously every path was computed but now there would
be no need, we build the path form the bottom up
Same edge case
"""
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if len(triangle) == 1 :
            return triangle[0][0]
        
        # Reversed loop
        for i in reversed(range(len(triangle))):
            # Check if this is not the bottom row
            if i + 1 != len(triangle):
                # Loop through row
                for j in range(len(triangle[i])):
                    # Change values in place
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]