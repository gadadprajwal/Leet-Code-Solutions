# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        
        slow = head
        fast = head
        
        while(fast and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
