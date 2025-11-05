#
# [67] Add Binary
#
"""
Solution 1
start by counting the decimal value of each bianry number. do this by
getting the length of the string, then based on that we know how much
the highest value is worth, from there that value is / 2 each iteration 
and if its a 1 that value is added to a sum
after getting both sums, add them and then create the output binary
we can make the output binary by first making a loop which adds 0's
to a string while variable which started from 1 doubles each iteration
until its value becomes more than the sum we are trying to reach
we then stop there and add a 1, then loop back through the string
and whenever you are at a position where its bin value is lower than 
the current residual sum add a 1
Issue, I got stuck with building up the binary again from the sum,
instead I switched to using a built in method to convert"""

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def getBinVal(string):
            bin = 1
            sum = 0
            for num in reversed(string):
                if num == "1":
                    sum +=bin
                bin = bin * 2
            return sum
        
        aSum = getBinVal(a)
        bSum = getBinVal(b)
        Sum = aSum + bSum

        #Now making final binary
        binary = bin(Sum)[2:]
            
        return binary
        