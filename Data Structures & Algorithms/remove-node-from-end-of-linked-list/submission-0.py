# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=dummy=ListNode(None,head)
        fst=cur=head
        for i in range(n):
            fst=fst.next
        while fst!=None:
            cur=cur.next
            fst=fst.next
            prev=prev.next
        prev.next=cur.next
        cur.next=None
        return dummy.next