# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder (print by level)
        # inorder (print by want you see on screen)
        if not preorder or not inorder: 
            return None
        
        root = TreeNode(preorder[0])
        
        root_index = inorder.index(root.val) # middle index
        
        root.left = self.buildTree(preorder[1: root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        
        return root

