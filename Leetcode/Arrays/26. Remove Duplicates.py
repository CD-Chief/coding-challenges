# [26] Remove Duplicates from Sorted Array
"""Solution 1
Loop though array and for each value use count() to count how
many of that value is within the array, if its >1 remove the value
and continue
Issue: with index when removing a value

Solution 2
instead make a new array and add each new value not already in that array
to the array with a loop 
Issue: The problem wants me to change the array itself not return the answer

Solution 3
I'll add a loop to append the new values to the nums array"""


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newArr = []

        for num in nums:
            if num not in newArr:
                newArr.append(num)
            print (newArr)

        nums.clear()

        for num in newArr[::-1]:
            nums.insert(0, num)

            
        return len(nums)