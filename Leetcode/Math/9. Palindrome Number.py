# [9] Palindrome Number
"""Basically I just have to reverse the int and compare it to 
original int. Hvae to figure out how ot reverse the int
Will try convert it into a string and then reverse it"""
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)

        if strX == strX[::-1] : return True
        return False