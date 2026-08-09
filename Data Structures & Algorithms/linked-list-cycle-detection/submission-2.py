# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        sl=fst=head
        while fst and fst.next:
            sl=sl.next
            fst=fst.next.next
            if sl==fst:
                return True
        return False