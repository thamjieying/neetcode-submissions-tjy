# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        if root:
            q.append(root)

        while q:
            current_q_len = len(q)
            depth += 1
            for _ in range(current_q_len):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            
        return depth
