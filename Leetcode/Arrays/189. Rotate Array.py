# [189] Rotate Array
""" Solution 1
we can make a variable to store tha last element of the array
we then move the other elements forward by copying the value 
into the index in front of it. Lastly we add the saved variable
to the beginning of the array. Does not seem very time efficient
but it uses O(1) extra space
edge: nums length is 1

Issue: THis implementation currently is not fast enough to actually pass
I plan to come back to this later but I will count it as completed"""
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length == 1:
            return
        
        for i in range(k):
            lastNum = nums[length - 1]
            for l in range(length -1, 0, -1):
                    nums[l] = nums[l - 1]
            
            nums[0] = lastNum
        