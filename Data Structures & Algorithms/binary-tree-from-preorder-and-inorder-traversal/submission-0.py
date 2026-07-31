# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Map each value in 'inorder' to its index for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Step 2: Track the current root index in 'preorder' using a list pointer
        pre_idx = [0]

        # Step 3: Define the helper recursive function using boundaries in 'inorder'
        def helper(in_left, in_right):
            # Base Case: If the left boundary exceeds the right boundary, no subtree exists
            if in_left > in_right:
                return None

            # Pick the current root value from 'preorder' and advance the index pointer
            root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1

            # Create the actual tree node
            root = TreeNode(root_val)

            # Find where this root sits in 'inorder'
            idx = inorder_map[root_val]

            # Recursively construct the left and right subtrees
            # Note: We MUST construct the left subtree first because 'preorder' processes left before right!
            root.left = helper(in_left, idx - 1)
            root.right = helper(idx + 1, in_right)

            return root

        # Start recursion covering the full span of 'inorder'
        return helper(0, len(inorder) - 1)   