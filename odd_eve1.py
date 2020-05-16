# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        con_point = even
        while True:
            if odd is None or even is None or even.next is None:
                odd.next = con_point
                break
            odd.next = even.next
            odd = even.next
            if odd.next is None:
                even.next = None
                odd.next = con_point
                break
            even.next = odd.next
            even = odd.next
        return head

