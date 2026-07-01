# Definition for singly-linked list (provided in file {F337F950-AA47-446C-85EB-01CA9A678013}.png).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node to construct the new list easily
        dummy = ListNode()
        curr = dummy
        
        # 'carry' stores any value >= 10 that spills over to the next place value
        carry = 0
        
        # Step 2: Loop while there are still digits to process OR a leftover carry
        while l1 or l2 or carry:
            # Extract values from nodes if they exist, otherwise default to 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Step 3: Calculate the total sum for this place value
            total_sum = v1 + v2 + carry
            
            # Compute the new carry (e.g., 14 // 10 = 1)
            carry = total_sum // 10
            
            # Compute the digit to store in the new node (e.g., 14 % 10 = 4)
            digit = total_sum % 10
            
            # Create the new node and link it
            curr.next = ListNode(digit)
            
            # Move our output pointer forward
            curr = curr.next
            
            # Move l1 and l2 forward to their next digits if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # The true head of our sum list is right after the dummy node
        return dummy.next