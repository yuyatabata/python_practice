# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = []

        while head.next:
            stack.append(head)
            print('stack', stack)
            head = head.next

        while stack:
            cur = stack.pop()
            cur.next.next = cur
            cur.next = None

        return head
