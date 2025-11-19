# [637] Average of Levels in Binary Tree
"""Solution 1
We can make a recursive method which takes in both a node and the current level
we can use a 2 dimensional array to store the values, each level of it represents a level in the bin tree
after filling it we calculate the averages and fill another array with it which is returned"""
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        nodeArr = []
        def fillArr(node, level):
            if not node:
                return
            if len(nodeArr) <= level:
                nodeArr.append([node.val])
            else:
                nodeArr[level].append(node.val)
            
            fillArr(node.left, level +1)
            fillArr(node.right, level +1)
        
        fillArr(root, 0)

        # Next build new array
        avgArr = []
        for i in range(len(nodeArr)):
            levelSum = 0
            for num in nodeArr[i]:
                levelSum += num

            avgArr.append(levelSum / float(len(nodeArr[i])))
        
        return avgArr