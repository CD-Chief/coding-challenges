# [35] Search Insert Position
#
""" Solution 1
So since it has to be written in log n time complexity this
makes me think of binary search. therefore you would check
the size of the array and start in the middle, if the target
is lower you would go to the middle of that part and so on until
you find the value or you don't and return where the value would be

edge: if value is in array
Issue: this didnt really work, I feel like I did'nt really have this
visualized in my head, WHat helped was writing down the different steps

Solution 2
this time I thought I'd incorporate the "edge" into the solution,
it wasnt really anedge case anyway. this time, you have 2 pointers
left and right. when the midpoint value is lower than target
left becomes midpoint +1 and vice versa for when its higher.
Such that when the left pointer crosses the right or the right
pointer crosses the left we know that is where the value must be inserted
"""

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  # Not found: left is the correct insert position
