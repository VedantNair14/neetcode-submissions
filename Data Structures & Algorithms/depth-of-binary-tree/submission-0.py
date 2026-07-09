# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Step 1: Base Case
        # If the current node is empty (None), its depth is 0.
        if not root:
            return 0

        # Step 2: Recursive Step
        # Calculate the max depth of the left and right subtrees,
        # pick the larger one, and add 1 for the current node.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))