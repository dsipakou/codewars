# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head  
        counter = 0
        while tmp:
            counter += 1
            tmp = tmp.next
        counter = counter // 2
        while counter > 0:
            head = head.next
            counter -= 1
        return head