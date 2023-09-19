"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        if not node:
            return None
        def cloning(node):
            if node and node not in visited:
                #deep clone
                newNode = Node(node.val)
                visited[node.val] = newNode
                newNode.neighbors = [visited.get(n.val) or cloning(n) for n in node.neighbors]
            return newNode
        return cloning(node)
            
            