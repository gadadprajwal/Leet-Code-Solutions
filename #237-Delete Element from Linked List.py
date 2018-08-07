class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
