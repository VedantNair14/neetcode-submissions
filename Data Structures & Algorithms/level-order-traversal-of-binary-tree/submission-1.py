from collections import deque

# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge Case: If the tree is empty, return an empty list
        if not root:
            return []

        res = []
        # Step 1: Initialize the queue with the root node
        q = deque([root])

        # Step 2: Process the tree level by level until the queue is empty
        while q:
            level = []
            # Freeze the size of the current level
            level_size = len(q)

            # Process every node belonging to the CURRENT level
            for _ in range(level_size):
                # Pop the leftmost node from the queue
                node = q.popleft()
                level.append(node.val)

                # Add its left and right children to the queue for the NEXT level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Append the completed level values to our final result list
            res.append(level)

        return res