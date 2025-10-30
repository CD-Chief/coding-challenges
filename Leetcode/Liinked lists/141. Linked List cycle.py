# [141] Linked List Cycle
#
"""
Solution 1
keep array x. Go through linked list with a looP? the loop
makes sure the next node actually exists before querying it.
it adds the value of each node to x and before doing so checks
if the value is already in the array, if so it has a cycle
Edge: No nodes at all?, Single node.
Issue: Using values to check for cycles does not work, I made
the wrong assumption of thikning that there would be no duplicate
vales, I have to compare the actual node if possible

Solution 2
Same thing but instead of storing vlues I store the nodes

To improve"""

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        currentNode = head

        nodeArr = []
        
        while currentNode:
            if currentNode in nodeArr:
                print (currentNode.val)
                return True
            nodeArr.append(currentNode)
            currentNode = currentNode.next

        return False
