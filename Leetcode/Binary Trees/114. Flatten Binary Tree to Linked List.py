# [114] Flatten Binary Tree to Linked List
"""Solution 1
Although definitely not optimal, we can recursively get the 
values of the binary tree in an array using pre order traversal
then write over the existing binary tree adding the values from the array
We also have to make sure to make each nodes left pointer == Null
Edge: no values in root, in this case return root
Issue: the overwriting loop assigns Null to the left and right of the last node

Solution 2
same as last but
we can make a dummy node connect to the root so it starts from root
Issue: this also overwrites the root node making a new tree

Solution 3
First solution but use range() instead for the loop"""
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root
        
        nodeArr = []

        def fillArr(node):
            if not node:
                return
            
            # Pre order
            nodeArr.append(node.val)
            fillArr(node.left)
            fillArr(node.right)
        
        fillArr(root)

        # Write over binary tree

        currentNode = root
        for i in range(len(nodeArr)):
            currentNode.val = nodeArr[i]

            # Check its not the last node
            if i + 1 != len(nodeArr):
                currentNode.left = None

                # Make new right node
                newNode = TreeNode(None)
                currentNode.right = newNode
                currentNode = currentNode.right