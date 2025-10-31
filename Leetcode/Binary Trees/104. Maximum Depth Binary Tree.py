# [104] Maximum Depth of Binary Tree
#
"""
Solution 1
Recursive function which takes a node and a number and checks if the node exists, if it does the function
runs the same function on both left and right of the node and returns the larger number of the two
if the function detects a node is not valid, it returns the greater of the two branches, if both are not valid,
it returns the given number 
edge: node does not exist?

Explanation isn't very good but I figured it out while coding and it worked first try! 

Your runtime beats 100 % of python3 submissions
Your memory usage beats 7.36 % of python3 submissions (19.3 MB)
"""

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node, depth):
            left = 0
            right = 0
            if node.left:
                left = getDepth(node.left, depth + 1)
            if node.right:
                right = getDepth(node.right, depth + 1)

            if not node.left and not node.right:
                return depth
            
            if left > right:
                return left
            return right
        
        return getDepth(root, 1)