# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        dummy = None

        while list1 and list2:
            if list1.val <= list2.val:
                if not merged:
                    merged = list1
                    dummy = merged
                else:
                    merged.next = list1
                    merged = merged.next

                list1 = list1.next
            else:
                if not merged:
                    merged = list2
                    dummy = merged
                else:
                    merged.next = list2
                    merged = merged.next

                list2 = list2.next
        
        while list1:
            if not merged:
                merged = list1
                dummy = merged
            else:   
                merged.next = list1
                merged = merged.next
                
            list1 = list1.next

        while list2:
            if not merged:
                merged = list2
                dummy = merged
            else:   
                merged.next = list2
                merged = merged.next

            list2 = list2.next
        
        return dummy
           