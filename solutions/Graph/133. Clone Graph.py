"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        # Hash map to store the mapping from original node to cloned node
        # key: original node, value: cloned node
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # If the node has already been visited, return its clone from the map
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the current node (do not copy neighbors yet)
        clone_node = Node(node.val, [])

        # Mapping the original node to its clone in the hash map
        # This MUST be done before recursive calls to handle cycles
        self.visited[node] = clone_node

        for neighbor in node.neighbors:
            # Recursively clone the neighbors and add to the cloned node's neighbors list
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node
