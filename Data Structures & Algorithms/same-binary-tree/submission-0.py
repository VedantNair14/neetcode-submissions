# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: Both nodes are empty (None)
        # Reaching the end of both branches at the same time means they match!
        if not p and not q:
            return True
            
        # Case 2: One node is empty, but the other is NOT
        # This means the trees have structural differences (mismatched shapes).
        if not p or not q:
            return False
            
        # Case 3: Both nodes exist, but their values are different
        if p.val != q.val:
            return False
            
        # Case 4: The current nodes match! Now check their subtrees recursively.
        # Both the left subtrees AND the right subtrees must match.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)