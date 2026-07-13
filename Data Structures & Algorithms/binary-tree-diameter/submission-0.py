# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Step 1: Initialize a variable to track the maximum diameter found.
        # We use a list with a single element so we can modify it inside our helper function.
        max_diameter = [0]

        # Step 2: Define the bottom-up DFS helper function
        def dfs(node):
            # Base Case: An empty node has a height of 0
            if not node:
                return 0

            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Calculate the diameter passing through the CURRENT node
            current_diameter = left_height + right_height

            # Update our global maximum if the current diameter is larger
            max_diameter[0] = max(max_diameter[0], current_diameter)

            # Return the height of this subtree back up to the parent node
            return 1 + max(left_height, right_height)

        # Step 3: Run the DFS starting from the root
        dfs(root)
        
        # Step 4: Return the maximum diameter recorded
        return max_diameter[0]