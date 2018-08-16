# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


        # Two pointer approach
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        l1 = headA # Point towards the starting of first list
        l2 = headB # Point towards the starting of second list
        
        # Base Case
        if headA == None or headB == None:
            return None
        
        # Traverse both the lists simulataneously until one out of the reach the last element
        while(l1 != None and l2!= None):
            l1 = l1.next
            l2 = l2.next
        
        # If the first pointer has reached the end point remaining pointer to the start of remaining list
        # Now initialise the new pointers again at the starting of both the list as follows with names long and short
        # Long will be the one with remaining list 
        # Short will be the one which reached null 
        if l1 == None:
            remaining = l2
            long_ = headB
            short_ = headA
        else:
            remaining = l1
            long_ = headA
            short_ = headB
        
       # Now till the remaining pointer becomes null increment long pointer so that it becomes equivalent to short list
        while(remaining != None):
            long_ = long_.next
            remaining = remaining.next

       # Now both long and short pointer are at the same level now unless and untill both the pointer will contain same value we are supposed to move them ahead so that we can reach the intersection of both the list
        while(short_ != None):
            if short_ == long_:
                return short_
            short_ = short_.next
            long_ = long_.next
            
        return None
                
            
        
        
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
