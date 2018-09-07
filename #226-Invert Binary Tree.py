# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def helper(self, rootl, rootr,prev):
        
        if rootl and rootr:
            prev.left = rootr
            prev.right = rootl
        
        if rootl == None and rootr:
            prev.left = rootr
            prev.right = None
        
        if rootl and rootr == None:
            prev.right = rootl
            prev.left = None
        
        
        
        if rootl!=None:     
            self.helper(rootl.left, rootl.right, rootl)
        if rootr!=None:
            self.helper(rootr.left, rootr.right, rootr)
        
    
    def invertTree(self, root):
        if root == None or not root:
            return None
        self.helper(root.left,root.right, root)
        return root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
