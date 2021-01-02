# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        l_a = self.getLength(headA)
        l_b = self.getLength(headB)
        while l_a > l_b:
            headA = headA.next
            l_a -= 1
        while l_b > l_a:
            headB = headB.next
            l_b -= 1
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
    def getLength(self, head: ListNode) -> int: 
        local_head = head
        length = 0
        while local_head.next:
            length += 1
            local_head = local_head.next
        return length
