# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# p0  c1 -> n2 -> 3 ->

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            curr = head
            next_ = curr.next

            curr.next = prev
            prev = curr
            head = next_

        return prev