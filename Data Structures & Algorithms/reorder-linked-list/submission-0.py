# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        reversed_head = prev

        curr = head
        while curr and reversed_head:
            tmp1 = curr.next
            tmp2 = reversed_head.next

            curr.next = reversed_head
            reversed_head.next = tmp1

            curr = tmp1
            reversed_head = tmp2
        