# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        
        # Three Pointer Approach
        prev = None
        cur = head
        ahead = head.next
        
        while(ahead!=None):
            
            cur.next = prev
            prev = cur
            cur = ahead
            ahead = ahead.next
        # For the last remaining element to be attached
        cur.next = prev
        return cur
        
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
