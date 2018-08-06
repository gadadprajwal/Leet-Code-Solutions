# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Define your stack.
class Stack:
    def __init__(self):
        self.__storage = []

    def isEmpty(self):
        return len(self.__storage) == 0

    def push(self,p):
        self.__storage.append(p)

    def pop(self):
        return self.__storage.pop()



class Solution:
    
    # Helper function which takes root and the lis array which will return the list of inorder elements
    # Recursive function call it from the main function if you want to see it running
    def inorderTraversalHelper(self,root,lis):
        if root == None:
            return lis
        else:
            lis=self.inorderTraversalHelper(root.left,lis)
            lis.append(root.val)
            lis=self.inorderTraversalHelper(root.right,lis)
            return lis
    
    # Iterative function
    def inorderTraversal(self, root):
        stack = Stack()
        arr = []
        while(root != None or not stack.isEmpty() ):
            if root:
                stack.push(root)
                root = root.left
            else:
                root = stack.pop()
                arr.append(root.val)
                root = root.right
        return arr    
            
