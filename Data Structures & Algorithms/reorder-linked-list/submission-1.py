# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return head
        cur=fst=head
        while fst and fst.next:
            cur=cur.next
            fst=fst.next.next
        mid=cur.next
        cur.next=None
        prev=None
        while mid:
            nxt=mid.next
            mid.next=prev
            prev=mid
            mid=nxt
        mid=prev
        cur=head
        while cur and mid:
            nxt=cur.next
            cur.next=mid
            nxt2=mid.next
            mid.next=nxt
            cur=nxt
            mid=nxt2
