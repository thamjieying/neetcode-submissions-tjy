# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        queue = deque()
        queue.append(root)
        res = []
        
        while queue:
            current_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node: 
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current_level: 
                res.append(current_level)
        return res