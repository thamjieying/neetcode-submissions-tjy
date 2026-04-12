# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateTree(node, max=float('inf'), min=float('-inf')):
            if not node: 
                return True
            
            if min < node.val < max: 
                return validateTree(node.left, node.val, min) and validateTree(node.right, max, node.val)
            
            else: 
                return False

        return validateTree(root)
    
