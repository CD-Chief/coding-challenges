# [530] Minimum Absolute Difference in BST
"""Solution 1
Use a recursive method to go through the bst and add each node value to an array
after that, sort the array, and loop through it, calculating the difference between
2 values each time and recording the smallest difference
"""
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        valArr = []
        def fillArr(node):
            if not node:
                return
            
            valArr.append(node.val)

            fillArr(node.left)
            fillArr(node.right)
        fillArr(root)
        valArr.sort()

        smallestDiff = 0
        for i in range(len(valArr)):
            if i < len(valArr) -1:
                diff = valArr[i+1] - valArr[i]
                if i == 0:
                    smallestDiff = diff
                
                if diff < smallestDiff:
                    smallestDiff = diff
        
        return smallestDiff