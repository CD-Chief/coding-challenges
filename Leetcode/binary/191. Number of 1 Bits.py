# [191] Number of 1 Bits
"""Solution 1
convert the int to binary and then to str and loop through
the string to count the 1's and return it"""
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(bin(n)[2::])

        setBits = 0
        for num in binary:
            if num == "1":
                setBits += 1
        
        return setBits
