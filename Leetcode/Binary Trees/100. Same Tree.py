# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""Solution 1
write a method for converting a binary tree into a list. Use this method on both 
binary trees and compare the output
Edge: both roots don't exist

Issue: forgot some return statements and had to add a none marker to compare structure as well
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def toListWrap(root):
            valList = []
            def toList(root):
                if not root:
                    valList.append("None")
                    return
                
                toList(root.left)
                toList(root.right)

                valList.append(root.val)

            toList(root)
            return valList
        
        pArr = toListWrap(p)
        qArr = toListWrap(q)

        if pArr == qArr:
            print(pArr)
            return True
        print(f"{qArr} and {pArr}")
        return False