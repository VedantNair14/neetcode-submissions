# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that validates if nodes stay within allowed boundaries
        def validate(node, left_bound, right_bound):
            # Base Case: An empty node is always a valid BST
            if not node:
                return True
            
            # The current node's value MUST strictly lie between left_bound and right_bound
            if not (left_bound < node.val < right_bound):
                return False
            
            # Recursively check subtrees:
            # - Going Left: upper limit shrinks to node.val
            # - Going Right: lower limit raises to node.val
            return (validate(node.left, left_bound, node.val) and 
                    validate(node.right, node.val, right_bound))

        # Start validation with infinite bounds for the root
        return validate(root, float('-inf'), float('inf'))