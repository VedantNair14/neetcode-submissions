# Definition for singly-linked list (provided in problem space).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Step 1: Initialize both pointers to start at the head of the list
        slow = head
        fast = head

        # Step 2: Loop as long as the fast pointer and its next node exist
        # If either is None, it means we hit a dead end (no cycle)
        while fast and fast.next:
            slow = slow.next          # Slow moves 1 step
            fast = fast.next.next     # Fast moves 2 steps

            # Step 3: Check if the fast pointer caught up to the slow pointer
            if slow == fast:
                return True           # Cycle detected!
                
        return False                  # Broke out of loop, hit a dead end