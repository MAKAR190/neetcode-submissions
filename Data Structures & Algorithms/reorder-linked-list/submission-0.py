# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next

        # Splitting halves
        slow.next = None

        # Reversing l2
        prev = None
        curr = l2

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        l2 = prev
        
        # Merging lists
        while l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next if l1_next else None
            l2 = l2_next
        
