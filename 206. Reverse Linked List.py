# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = head
        p = head
        
        r = None
        
        while p:
            temp = p.next
            p.next = r
            r = p
            p = temp
        return r
