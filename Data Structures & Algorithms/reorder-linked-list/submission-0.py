class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list using Tortoise and Hare
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'second' is the head of the second half of the list
        second = slow.next
        # Cut off the first half from the second half
        slow.next = None

        # Step 2: Reverse the second half of the list
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 'second' now points to the head of the reversed second half
        second = prev 
        first = head

        # Step 3: Interleave/Merge the two halves (first and second)
        while second:
            # Save the next nodes for both halves before breaking pointers
            tmp1, tmp2 = first.next, second.next
            
            # Connect first half node to second half node
            first.next = second
            # Connect second half node back to the next first half node
            second.next = tmp1
            
            # Slide pointers forward
            first = tmp1
            second = tmp2