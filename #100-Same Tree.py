# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        
        
        # Base case check if the nodes are null, if both the nodes are then they are still same.
        if p == None and q == None:
            return True
        
        # If any one of the two nodes are null, then they are not same
        if p == None or q == None:
            return False
        
        # Once you know both the nodes are not Null, now check their value if they are same or not.
        # Once the values of both the nodes are same now we will have to check for the remaing sub trees.
        # Call the function for the left sub tree of both the trees and repeat that for the right sub tree.
        if p.val == q.val:
            if self.isSameTree(p.left, q.left) == True:
                if self.isSameTree(p.right, q.right) == True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
        
        
        
        
        
        # if p == q:
        #     return True
        # else:
        #     if p is not None and q is not None:
        #         if p.val == q.val:
        #             if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
        #                 return True
        # return False
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
