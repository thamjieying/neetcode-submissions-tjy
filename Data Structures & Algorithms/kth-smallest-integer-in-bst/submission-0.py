# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node, visited=[]):
            nonlocal res
            if not node: 
                return 
            
            if node.val in visited: 
                return 

            if len(res) > k:
                return 

            dfs(node.left)

            res.append(node.val)
            visited.append(node.val)

            dfs(node.right)
        
        dfs(root)
        print(res)
        return res[k-1]

            

            