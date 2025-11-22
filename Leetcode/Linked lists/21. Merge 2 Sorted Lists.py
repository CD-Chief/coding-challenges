# [21] Merge Two Sorted Lists
"""Solution 1
start with a temporary root node. Now from here we create the merged list
we start at the first node of each list, compare them, if they are the same 
we link them both to the node, if different we link the smaller one, if only one
node is there we link that one.
Next, for the list/s where the node was chosen from, we move to next node and comapre
across lists again... To end the loop, both next nodes must be null
Issue: Way too complicated implementation and keeping track of too many var with
no need

Solution 2
Same as first but different implementation. And when one list is done, just add the other on
"""
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        currentNode = ListNode()
        tempNode = currentNode

        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next
        
        if list1:
            currentNode.next = list1
        elif list2:
            currentNode.next = list2
        
        
        return tempNode.next