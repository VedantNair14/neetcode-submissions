# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Base Case
        # If we reach an empty node (Null/None), there's nothing to invert.
        if not root:
            return None

        # Step 2: Swap the left and right children of the current node
        # Python allows us to do an elegant in-place swap on a single line
        root.left, root.right = root.right, root.left

        # Step 3: Recursively call the function on both subtrees
        # This repeats the swapping process all the way down to the leaf nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Step 4: Return the modified tree root
        return root