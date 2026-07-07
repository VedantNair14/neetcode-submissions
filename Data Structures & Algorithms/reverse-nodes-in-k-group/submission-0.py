# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Use a dummy node to seamlessly handle head updates
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the k-th node from our current position
            kth = self.getKth(groupPrev, k)
            if not kth:
                # If there aren't enough nodes left to form a group of k, stop!
                break
            
            # Save the starting node of the next group
            groupNext = kth.next

            # Step 2: Reverse the current group of k nodes
            # 'prev' starts at groupNext because the new tail of this group
            # must link directly to the beginning of the next group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Step 3: Connect the previous group's tail to this group's new head
            # groupPrev.next currently points to the old head (which is now the tail)
            tmp = groupPrev.next
            groupPrev.next = kth
            
            # Slide groupPrev forward to become the tail of our newly reversed group
            groupPrev = tmp

        return dummy.next

    # Helper function: Move forward k steps and return that node
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr