# Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # Case 1: Both p and q are greater than curr, look in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Case 2: Both p and q are less than curr, look in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Case 3: We found the split point! 
            else:
                return curr  