# Definition for singly-linked list (provided in the problem comments).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to act as the grounding start of our new list
        dummy = ListNode()
        # 'tail' will always point to the last node of our newly building list
        tail = dummy

        # Step 2: Loop while BOTH lists still have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                # If list1's node is smaller, connect it to our merged chain
                tail.next = list1
                # Advance list1 to its next node
                list1 = list1.next
            else:
                # If list2's node is smaller or equal, connect it to our merged chain
                tail.next = list2
                # Advance list2 to its next node
                list2 = list2.next
            
            # Move the tail pointer forward to our newly appended node
            tail = tail.next

        # Step 3: If one list runs out of elements first, simply append 
        # the remaining chunk of the other list directly to the end
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Step 4: The actual head of our merged sorted list is right after the dummy node
        return dummy.next