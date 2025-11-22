# [148] Sort List
"""Solution 1
i don't see a way other than going through the linked list and adding the values to a 
list to then sort it there and then create a new linked list from that?
Edge: Empty list
Issue: building new linkedlist is more difficult than i thought"""
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nums = []
        # move into list
        currentNode = head
        while currentNode:
            nums.append(currentNode.val)
            currentNode = currentNode.next

        # sort list
        nums.sort()

        # turn into linked list
        newHead = ListNode(0)
        currentNode = newHead
        for i in range(len(nums)):
            currentNode.next = ListNode(0)
            currentNode = currentNode.next
            currentNode.val = nums[i]
        
        return newHead.next