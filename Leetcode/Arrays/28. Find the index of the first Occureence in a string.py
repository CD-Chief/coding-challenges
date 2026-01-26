# [28] Find the Index of the First Occurrence in a String
"""Solution 1
We make a variable which has a counter for the needle.
this var starts at 0 and when the first letter, the 0th index
of the needle is found we incrment the var, if the next letter is not 
the next letter of the needle the var is reset to 0. Otherwise
the count continues until the max index of needle, in which case
we return True
Issue: we need to return the index in the haystack, not true or false

Solution 2
The same thing but instead have another varibale that updates to the 
first index of the needle in the haystack. and use a in range loop
Issue: we don't catch cases in which the needle starts within a failing case
I.e. we skip over it in this case  e.g
"mississippi"
"issip"

Solution 3
we switch to a sliding window mechanism. we know the length of the needle
and for each letter in the haystack we compare if the needle starts there
if it does we check the next letter if it matches, if it doesn't we just slide
the window forward and do the same until the full winodw block matches 

Solution 4
Was about to implement 3 when I realised python already has a method that 
does that :p"""


#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)
                