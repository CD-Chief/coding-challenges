# [20] Valid Parentheses
"""Solution 1
make a variable for each bracket
whenever an open bracket for the specific bracket is found that var is incremented
when the closing bracket for that var is found that var is decremented
if a closing bracket is found before an open bracket, return false
if the variables are not all == to 0, return false
edge cases: string is empty
Issue: order is important ([)] should fail too
Solution 2
instead have a list, where you append whenever a new open bracket comes in,  when a closing bracket comes
you pop off the last value from the list, assuming its the corresponsding bracket
Return true only when the list is empty. 
"""
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s): return True

        brackets = []
        
        for bracket in s:
            match bracket:
                case "(":
                    brackets.append("(")
                case "[":
                    brackets.append("[")
                case "{":
                    brackets.append("{")

                case ")":
                    if not brackets: return False
                    if brackets[-1] == "(":
                        brackets.pop()
                    else: return False
                case "]":
                    if not brackets: return False
                    if brackets[-1] == "[":
                        brackets.pop()
                    else: return False
                case "}":
                    if not brackets: return False
                    if brackets[-1] == "{":
                        brackets.pop()
                    else: return False
        
        if not brackets:
            return True
        return False