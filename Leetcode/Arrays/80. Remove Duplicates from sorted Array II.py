# [80] Remove Duplicates from Sorted Array II
"""Soltion 1
make a function that takes in a value and an index and checks how many times the number
comes up, up to that index

Then, make loop iterating over the nums, every iteration, use the function to make
sure the num has not been added to the start of the array twice, otherwise skip to the next
Issue: too complicated and failed most cases

Solution 2
We keep not of the fact that the array is sorted
With this in mind we can instead iterate over the array and 
keep not of the current value, each iteration we count how mayn times
the current value has come up and if its the third time, the pointer stays there
for the iterating pointer to continue to find a new value to replace it with...
Issue: could not get it working

Solution 3
We know that the first 2 values will always pass, if we check for a case other than that
and check that numbers after that are greater than the number 2 values ago then they pass too
otherwie we replace number at write index with this number"""
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0 # Index to write at

        for num in nums:

            
            if k < 2:
                k += 1
            elif num > nums[k - 2]:
                nums[k] = num
                k += 1

        return k