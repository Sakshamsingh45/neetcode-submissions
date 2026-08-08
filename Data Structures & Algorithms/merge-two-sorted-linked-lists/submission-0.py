# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur=dummy=ListNode(None)
        fst,snd=list1,list2
        while fst and snd:
            if fst.val<snd.val:
                cur.next=fst
                cur=cur.next
                fst=fst.next
            elif fst.val>snd.val:
                cur.next=snd
                cur=cur.next
                snd=snd.next
            else:
                cur.next=fst
                fst=fst.next
                cur=cur.next
                cur.next=snd
                snd=snd.next
                cur=cur.next
        if fst:
            cur.next=fst
        if snd:
            cur.next=snd
        return dummy.next
