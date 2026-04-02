"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node, visited={}):
            if not node:
                return None
            
            if node in visited: 
                return visited[node]

            new_node = Node(node.val)
            visited[node] = new_node
            for neig in node.neighbors:
                new_node.neighbors.append(dfs(neig, visited))
            
            return new_node

        return dfs(node)