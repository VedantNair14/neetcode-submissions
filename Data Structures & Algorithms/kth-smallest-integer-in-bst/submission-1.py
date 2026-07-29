  # Definition for a binary tree node (provided in your editor comments).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        # Continue while there are nodes to visit or nodes left on the stack
        while curr or stack:
            # Step 1: Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # Step 2: Pop the top element (the smallest unprocessed node)
            curr = stack.pop()

            # Step 3: Count this node as processed
            k -= 1
            if k == 0:
                return curr.val

            # Step 4: We've visited the left and current node, now check the right subtree
            curr = curr.right