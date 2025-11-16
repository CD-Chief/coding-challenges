# [392] Is Subsequence
"""Solution 1
turn s into a list
We loop once through t and keep an index which starts from 0 for s
each iteration we check if the current chsr in t is == s[index]
if so we iterate the index.
At the end we check if the index is == len(s) -1
if so its true
Edge: if either s or t is len is 0 just return false?
    not sure what to do in this case
"""
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sList = list(s)
        sIndex = 0
        for char in t:
            if sIndex == len(sList):
                return True
            if char == sList[sIndex]:
                sIndex += 1
        if sIndex == len(sList):
            return True
        return False