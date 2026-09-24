"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base Case: Empty graph input
        if not node:
            return None

        # Maps each original node to its brand-new cloned node
        old_to_new = {}

        def dfs(curr: 'Node') -> 'Node':
            # If the node was already cloned, return the existing clone
            if curr in old_to_new:
                return old_to_new[curr]

            # Step 1: Create a clone of the current node
            copy = Node(curr.val)
            # Step 2: Register it in the hash map BEFORE exploring neighbors (prevents cycles)
            old_to_new[curr] = copy

            # Step 3: Recursively clone and link all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)