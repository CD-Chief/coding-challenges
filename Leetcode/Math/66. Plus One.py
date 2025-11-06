# [66] Plus One
"""Solution 1
loop form the back of the array, check if its a 9. otherwise add 1 to it
if its a 9 turn it into a 0 and do the same until you reach the end of the array. if
that is still a 9, make it 0 and add a 1 to the front of the array"""
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        done = False

        for i in range(len(digits) -1, -1, -1):
            if not done:
                if i == 0 and digits[0] == 9:
                    digits[i] = 0
                    print (digits)
                    digits.insert(0, 1)
                    print (digits)
                    print (f"end {digits}")
                    return digits

                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits