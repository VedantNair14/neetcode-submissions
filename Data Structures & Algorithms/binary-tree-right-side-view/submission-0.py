from collections import deque

# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge Case: If the tree is empty, return an empty list
        if not root:
            return []

        res = []
        # Step 1: Initialize the queue with the root node
        q = deque([root])

        # Step 2: Traverse level by level
        while q:
            rightmost_node = None
            level_size = len(q)

            # Process all nodes in the current level
            for i in range(level_size):
                node = q.popleft()
                
                # Update our rightmost tracking pointer with the current node
                rightmost_node = node

                # Add left and right children to the queue for the NEXT level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # After processing the entire level, the last node seen is added to res
            if rightmost_node:
                res.append(rightmost_node.val)

        return res