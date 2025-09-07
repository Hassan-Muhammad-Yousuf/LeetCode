# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        s = head
        f = head
        d = None

        while f and f.next:
            d = s
            s = s.next
            f = f.next.next
            
        
          
        d.next = s.next
        
        return head

        

