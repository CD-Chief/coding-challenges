# [58] Length of Last Word
"""Solution 1
Loop through string, keep a counter that counts up for each non space
but resets to 0 when there is a space
Issue: did not consider last character being empty
    
Solution 2
To fix this I would hold 2 variables
one lastWord which holds the length of the last word
and currentLetters to replace letters
lastWord is reset to hold currentLetters every time there is a new letter
but when there is a 0, lastWord stays the same"""
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        lastWord = 0
        currentLetters = 0

        for char in s:
            if char.isalpha():
                currentLetters += 1
                lastWord = currentLetters
            else:
                currentLetters = 0
        
        return lastWord