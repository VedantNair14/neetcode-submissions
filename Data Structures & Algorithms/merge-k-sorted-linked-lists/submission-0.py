# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # Handle edge cases: empty input array or no lists present
        if not lists or len(lists) == 0:
            return None

        # Step 1: Keep pairing up and merging until only ONE final list remains
        while len(lists) > 1:
            mergedLists = []
            
            # Traverse the array jumping by 2 to pair up adjacent lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # If there's an odd number of lists, the last one won't have a pair
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the pair and add the result to our temporary list stage
                mergedLists.append(self.mergeTwoLists(l1, l2))
                
            # Replace the old array of lists with our newly merged, halved array
            lists = mergedLists

        return lists[0]

    # Helper function: Classic iterative merge of two sorted linked lists
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next