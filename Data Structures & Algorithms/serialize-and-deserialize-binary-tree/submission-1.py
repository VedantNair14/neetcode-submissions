# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            # Root -> Left -> Right
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        vals = data.split(",")
        self.i = 0  # Global index pointer to track current value in 'vals'

        def dfs():
            # If current value is 'N', it's a null/None node
            if vals[self.i] == "N":
                self.i += 1
                return None

            # Create the node with current integer value
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # Recursively construct Left and Right subtrees
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()