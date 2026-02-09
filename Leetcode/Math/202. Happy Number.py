# [202] Happy Number
"""Solution 1 
2 loops, a while loop that checks a value to see if it is 1 yet.
And a loop that goes though all numbers in the integer and adds up the squares
to make the value for the for loop to check for.
To prevent the loop being endless, we can set a value that is added up each
loop iteration and once it reaches a certain value we stop the loop
Edge ?"""
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        sqSum = 0
        num = n
        iterations = 0

        while sqSum != 1 and iterations < 10:
            sqSum = 0

            strNum = str(num)
            for i in strNum:
                singleInt = ord(i) - ord('0')
                sqSum += singleInt ** 2

            num = sqSum
            iterations = iterations + 1
        
        if sqSum == 1:
            return True
        
        return False