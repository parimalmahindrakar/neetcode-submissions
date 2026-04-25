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
        old_mapings = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            old_mapings[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = old_mapings[curr]
            copy.next = old_mapings[curr.next]
            copy.random = old_mapings[curr.random]
            curr = curr.next
        
        return old_mapings[head]


