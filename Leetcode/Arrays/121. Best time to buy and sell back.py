# [121] Best Time to Buy and Sell Stock

"""Solution 1
I will use a 2  pointer approach with 2 loops, very brute force. one pointer will 
start from the back of the array and the other from the front.
The front pointer will forward 1 each iteration until it reaches the index
before the back pointer at which point the back pointer moves 1 to the front
and the front pointer repeats the same thing. eahc iteration we compute
the profit with fornt pointer as buy and back as sell. The highest
profit is returned.
Edge. in case of just 1 element in array, return 0
Issue: O(n^2) time complexity is not good enough

Solution 2
Need only 1 loop. we keep track of the lowest price so far and each step we go
further we see if selling now after having bought at that lowest price is greater
than the previous selling point. We then return the max profit"""
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # best (lowest) buy so far
            if price < min_price:
                min_price = price
            else:
                # profit if we sell today
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit