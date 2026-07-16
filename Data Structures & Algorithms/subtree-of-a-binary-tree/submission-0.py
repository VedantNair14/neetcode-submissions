# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: If subRoot is empty, an empty tree is technically a subtree of ANY tree
        if not subRoot:
            return True
        # Base Case 2: If the main root is empty but subRoot is not, subRoot cannot exist inside it
        if not root:
            return False

        # Step 1: Check if the trees are identical starting at the current main root node
        if self.isSameTree(root, subRoot):
            return True

        # Step 2: If they don't match here, look for subRoot in the left OR right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # Helper function: The exact same logic used in the "Same Binary Tree" problem
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)          