# [139] Word Break
"""Solution 1
loop through the string letter by letter and add each letter
to a variable, building a word as you go. Each time check whether the current
built word comes up in the dictionary, if it does, clear the current word
and keep going. If you reach the end of the string and the built word is
not empty, false. Otherwise True

Issue: Not sure how to explain it, but the case of 
"catsanddog"
["cat", "cats","dog","and"]
Is not possible with this approach
We can try doing this approach both backwards and forwards?

Issue: that does not work either, proven by case
"aaaaaaa"
["aaaa","aaa"]

Solution 2
We can use a recursive approach. We will start at the beginning of the string
and use a loop to try each of the possibilites in wordDict. Staring a
new branch for each. We can only try a word if at the current position
the word matches a part of the string, we therefore iterate to the end
of that word in that string an repeat until the end of the string.
If no word fits anymore, the function returns false.
If the whole function only returns false, the output is false

To make this a bit easier each run of the recusrive method holds
a copy of the string wihtout the chosen word

Issue: This fails as time limit exceeds : To fix this, we can use
@cache in python to cache results and thereofre stop the function
from computing things it already has and instead just return the 
cached result

"""
#

# @lc code=start

from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # O(1) lookup
        
        @cache
        def recursive(currentString: str):
            if not currentString:  # Base case: empty string = fully segmented
                return True
            
            for word in word_set:
                if currentString.startswith(word):
                    # Recurse on the remainder after this word
                    if recursive(currentString[len(word):]):
                        return True
            return False
        
        return recursive(s)