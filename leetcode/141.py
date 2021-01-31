# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        while head:
            print('val', head.val)
            print('head', head)
            if head in dic:
                return True
            else:
                dic[head] = True
            head = head.next
            print('next', head.val)
            print('dict', dic)
        return False
