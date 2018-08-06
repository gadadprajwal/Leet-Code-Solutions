# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def listofleaf(self,root, lis):
        # Base Case - Whenever you find a leaf node append it to the list
        if root.left == None and root.right == None:
            lis.append(root.val)
        
        # Check if your root has left child or not to recurse it further
        if root.left != None:
            self.listofleaf(root.left, lis)
        # Check if your root has right child or not to recurse it further
        if root.right != None:
            self.listofleaf(root.right, lis)
    
    
    def leafSimilar(self, root1, root2):
        # Check for few null cases
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        # To store list of leaf for tree 1
        lis = []
        self.listofleaf(root1,lis)
        # For tree 2
        lis2 = []
        self.listofleaf(root2,lis2)
        return lis == lis2
        
        
        
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
