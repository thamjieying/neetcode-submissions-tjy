from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        level_q = deque([root])
        res = []

        while level_q:
            level_count = len(level_q)
            level_nodes = []
            for _ in range(level_count):
                node = level_q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    level_q.append(node.left)
                if node.right: 
                    level_q.append(node.right)
            res.append(level_nodes)
        
        return res