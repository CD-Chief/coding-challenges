# [108] Convert Sorted Array to Binary Search Tree
#
"""Solution 1
Height balanced search tree means both sides must be the height
To do this we need the middle number of the array as this is will allow the array to be
balanced on both sides since its sorted. That nmber becomes the root and then
from there we do the same thing on each side of the middle number recursively
edge: single number, should be covered by the function anyway

Issue: had an issue because I was passing the actual tree into the function
instead of bulding subtrees recusively and tying them together. Should also make
sure to think about recursion systematically, in terms of base case and 
recursive case
"""

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildTree(lower, upper):
            if lower > upper:
                return None
            mid = ((upper - lower) // 2) + lower
            node = TreeNode(nums[mid])
            node.left = buildTree(lower, mid - 1)
            node.right = buildTree(mid + 1, upper)
            return node
        
        return buildTree(0, len(nums) - 1)