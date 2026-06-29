# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node to gracefully handle edge cases 
        # (like deleting the actual head node)
        dummy = ListNode(0, head)
        
        # Initialize our two pointers at the dummy node
        left = dummy
        right = dummy

        # Step 2: Advance the right pointer 'n' steps ahead
        # This creates a fixed gap of size 'n' between left and right pointers
        for _ in range(n):
            right = right.next

        # Step 3: Shift both pointers forward together until right reaches the very end
        while right.next:
            left = left.next
            right = right.next

        # Step 4: The Magic Step - Skip the Nth node from the end
        # left is currently standing exactly BEFORE the node we want to delete
        left.next = left.next.next

        # Step 5: Return the true beginning of the updated list
        return dummy.next