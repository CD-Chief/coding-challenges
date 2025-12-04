# [101] Symmetric Tree
"""Solution 1
We can make a recursive function to put all values from a root down
into an array, we then use this method on both the left and right side of
the root given and compare the arrays we get back
Issue: I realised the sides have to be mirrored, therefore this won't work
as seen in example 2.
Solutioon 2
to handle that issue we could have the function make a 2d array
and for each row in the tree we make a row in the array for it
lastly, we can compare both arrays row by row by comapraing 
on row with the other row but reversed"""
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        
        def treeArr(node, arr, level):
            
            if len(arr) - 1 < level:
                arr.append([])
            
            if not node:
                arr[level].append(None)
                return
            
            
            arr[level].append(node.val)
            treeArr(node.left, arr, level+1)
            treeArr(node.right, arr, level+1)

        
        arrLeft = []
        treeArr(root.left, arrLeft, 0)

        arrRight = []
        treeArr(root.right, arrRight, 0)

        if len(arrLeft) != len(arrRight):
            return False

        for i in range(len(arrLeft)):
            if arrLeft[i] != arrRight[i][::-1]:
                return False
        
        return True