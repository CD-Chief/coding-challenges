# [190] Reverse Bits
"""Solution 1
get the binary of the input, making sure all 32 bits are included. Reverse
the binary, and then convert that binary back into a number. Return the number
We can use bin() to convert to binary and then fill in the extra 0's if needed.
edge cases: empty n ?
Issue: forgot to remove the 0b after converting to binary
"""
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bin1 = bin(n)[2:]

        # Convert to string to add zeros
        bin1 = str(bin1)

        # Add Zeros
        while len(bin1) <= 31:
            bin1 = "0" + bin1
        
        # Flip bits
        bin2 = (bin1[::-1])

        # Convert to decimal
        num2 = int(bin2, 2)

        return num2
