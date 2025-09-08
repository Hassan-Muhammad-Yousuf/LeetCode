# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        point = head
        even = head.next
        dummy = even

        while even and even.next:
            point.next = even.next
            point = point.next

            even.next = point.next
            even = even.next

        point.next = dummy

        return head