# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1=l1
        val2=l2
        carry=0
        prev=dummy=ListNode(None)
        while val1 or val2 or carry:
            v1=val1.val if val1 else 0
            v2=val2.val if val2 else 0
            sm=v1+v2+carry
            digit=sm%10
            sm//=10
            carry=sm
            prev.next=ListNode(digit)
            prev=prev.next
            if val1:
                val1=val1.next
            if val2:
                val2=val2.next
        return dummy.next