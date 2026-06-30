# Definition for a Node (provided in the problem environment).
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Step 1: Create a hash map to connect old nodes to their deep copies
        # We also map None to None to cleanly handle tail and null random pointers
        oldToCopy = {None: None}

        # First Pass: Clone all individual nodes and store them in the dictionary
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        # Second Pass: Wire the 'next' and 'random' pointers for the cloned nodes
        curr = head
        while curr:
            copy = oldToCopy[curr]
            # Use the hash map to find the corresponding cloned versions
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        # Return the clone of the original head node
        return oldToCopy[head]