# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = []
        def dfs(node):
            if len(val) == k:
                return
            
            if not node: 
                return
            
            dfs(node.left)     
            val.append(node.val)
            dfs(node.right)

        dfs(root)
        return val[k-1]
