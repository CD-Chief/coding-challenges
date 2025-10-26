# [125] Valid Palindrome
#
# Approach 1
# Remove all non alphabet charecters and spaces
# Turn it into a list if reverse is == original its a palindrome
# Edge = Empty, single letter?

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1 : return True

        removed = ''.join(ch.lower() for ch in s if ch.isalnum())

        if "".join(reversed(removed)) == removed : return True
        return False
        
        
# @lc code=end