# [169] Majority Element
"""Solution 1
I will use the counnt() method for lists in python and make a 
seperate list. Loop though nums and for each not the count()
of that value in the new array, appending each time
at the end the new arrays indexes should be mapped to nums
we find the largest number in that new array, map its index to
nums and get its value"""

"""Solution 2
We can use count a lot smarter. instead, we loop through the
list and check if each values count() is greater than half
the array, if so return it

Issue: Both of these soltions went over the time limit as they were both On^2"""

"""Solution 3
This time, instead of checking how much each num appears for each num
we loop through the array and use a hasmap to map the values
and how often they appear.
"""
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums)
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > n // 2:
                return num