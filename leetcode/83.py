# # Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next  # 要素への代入のためコピー元のheadの値も更新される
            cur = cur.next  # 全体への代入のため、headは変わらない
        return head


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         while head and :
#             print('head',head)
#             print('val', head.val)
#             # print('next', head.next.val)
#             if (head.next != None) and (head.val == head.next.val):
#                 head = head.next
#         return head

# 配列verで参照渡しの動作確認
# head = [1, 1, 2]
# current = head
# while current and current[1:]:
#     if current[1] == current[0]:
#         current[1:] = current[2:]
#     else:
#         current = current[1:]
#     print('current:{}'.format(current), 'head:{}'.format(head))
