# pointer one goes down the list one and then starts going down the list 2.
# || ly  for pointer 2.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        flag = 0
        while p1 and p2 and flag <4:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if not p1:
                p1 = headB
                flag = flag + 1
            if not p2:
                p2 = headA
                flag =flag + 1
