# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that returns the height if balanced, or -1 if unbalanced
        def dfs(node):
            # Base Case: An empty node is balanced and has a height of 0
            if not node:
                return 0
            
            # 1. Check the left subtree
            left_height = dfs(node.left)
            if left_height == -1:
                return -1 # Left side is already unbalanced, bubble up failure
                
            # 2. Check the right subtree
            right_height = dfs(node.right)
            if right_height == -1:
                return -1 # Right side is already unbalanced, bubble up failure
                
            # 3. Check the current node's balance factor
            # If the difference between left and right height is greater than 1, it's unbalanced
            if abs(left_height - right_height) > 1:
                return -1
                
            # If balanced, return the actual height of this node to its parent
            return 1 + max(left_height, right_height)

        # If the root returns anything other than -1, the entire tree is balanced
        return dfs(root) != -1