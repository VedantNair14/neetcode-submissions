# Definition for singly-linked list (provided in the problem comments).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize pointers
        # 'prev' tracks the node behind us (starts as None because the new tail points to None)
        prev = None
        # 'curr' tracks the node we are currently standing on
        curr = head

        # Step 2: Traverse through the list until we run out of nodes
        while curr:
            # Save a reference to the next node before we break the link
            nxt = curr.next
            
            # The Magic Step: Reverse the pointer to face backward
            curr.next = prev
            
            # Move our sliding window pointers forward one step
            prev = curr
            curr = nxt

        # Step 3: 'prev' will be standing on the new head of the reversed list
        return prev