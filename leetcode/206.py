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

        while head.next:  # 最後から一つ手前のNode(val=4まで)をリストに格納
            stack.append(head)
            print('stack', stack)
            head = head.next  # 　次の番号のNodeを指定。最終的にhead=5となる

        while stack:
            cur = stack.pop()  # stack配列の末尾でから順に4,3,2,1をcur(カレント)から参照
            # cur.next.nextはheadであるval=5のポインタ(next)のこと。Noneを指していたポインタをつなぎ変え
            cur.next.next = cur
            cur.next = None

        return head
