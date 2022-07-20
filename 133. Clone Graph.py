"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hasmap = {}
        def clone(node):
            if node in hasmap:
                return hasmap[node]
            
            newNode = Node(node)
            for i in node.neighbors:
                Neighbor = clone(i)
                newNode.neighbors.append(Neighbor)
            return newNode
        
        return clone(node) if node else None
        
