"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        prev=dummy=Node(0)
        cur=head
        freq={}
        while cur!=None:
            new=Node(cur.val)
            prev.next=new
            prev=prev.next
            freq[cur]=new
            cur=cur.next
        cur=head
        curl=dummy.next
        while cur!=None:
            node=cur.random
            if node:
                curl.random=freq[node]
            cur=cur.next
            curl=curl.next
        return dummy.next