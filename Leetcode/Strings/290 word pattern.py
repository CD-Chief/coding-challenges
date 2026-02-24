# [290] Word Pattern
"""Solution 1
we can make use of a dictionary and dynamically update and check it
we loop through the pattern and for each letter. When there is a new
letter we add it to the dictionary and add its corresponding word.
If its not new we check that thw word at that position corresponds
to the saved letters value in the dictionary
to iterate through the string s, we can turn it into an array
with each word taking an index. Pythons Split() can be used for this.
Enumarate can be used to loop over pattern
Edge: s and pattern are contrained to have at least 1 word. So no need

Issue: a word can be assigned to multiple characters in pattern
    : Used an array to hold already used words and check if new
    characters have an already uswd word
Issue: there can be more or less characters than words.
    : added a check to make sure chars == words
    This should have been an edge case"""
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        patternDict = {}

        stringArr = s.split()
        usedWords = []

        if len(pattern) != len(stringArr):
            return False

        for i, char in enumerate(pattern):
            if char in patternDict:
                if patternDict[char] != stringArr[i]:
                    return False
            else:

                # Check if word has already appeared for another char
                if stringArr[i] in usedWords:
                    return False

                # Add to dictionary
                patternDict[char] = stringArr[i]
                # Add new word
                usedWords.append(stringArr[i])
        
        return True