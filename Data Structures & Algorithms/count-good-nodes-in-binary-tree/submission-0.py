# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function to perform DFS while tracking path maximum
        def dfs(node, max_val):
            # Base Case: An empty node contributes 0 good nodes
            if not node:
                return 0

            # Step 1: Check if the current node is "good"
            is_good = 1 if node.val >= max_val else 0

            # Step 2: Update the maximum value seen so far on this path
            new_max = max(max_val, node.val)

            # Step 3: Count good nodes in both subtrees with the updated max value
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)

            # Return total good nodes found at this node and below it
            return is_good + left_count + right_count

        # Start DFS with the root node, setting the initial max value to root's value
        return dfs(root, root.val)