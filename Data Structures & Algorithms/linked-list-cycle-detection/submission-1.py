# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        sl=head
        fst=head.next
        while fst and fst.next:
            if sl==fst:
                return True
            sl=sl.next
            fst=fst.next.next
        return False