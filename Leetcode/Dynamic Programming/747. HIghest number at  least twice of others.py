# [747] Largest Number At Least Twice of Others
"""Solution 1
hold 2 variables, highest secondHighest. We loop through the array
and continously replace these 2, when we find a num higher than highest
it becomes the new highest and the num at highest moves to secondHIghest.
At the end we check if highest is at least double of secondhighest. we return
its index
in python we can find the largest value, get its index and then remove it
afterwards we get largest value again and compare it to the previous"""
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        highest = []
        #First val is index
        highest.append(nums.index(max(nums)))
        #Second val is number
        highest.append(nums[highest[0]])

        nums.remove(highest[1])

        if highest[1] >= max(nums) * 2:
            return highest[0]
        return -1