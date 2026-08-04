# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize max_sum with the root's value (handles all-negative trees safely)
        max_sum = [root.val]

        def dfs(node):
            if not node:
                return 0

            # Step 1: Recursively compute the max path sum from left and right subtrees.
            # If a subtree returns a negative sum, clamp it to 0 (ignore it).
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            # Step 2: Compute the max path sum WITH a split at the current node (curve peak)
            current_split_sum = node.val + left_max + right_max

            # Step 3: Update global max_sum if the split path here is the largest found so far
            max_sum[0] = max(max_sum[0], current_split_sum)

            # Step 4: Return the max sum WITHOUT a split (straight path) to parent node
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_sum[0]