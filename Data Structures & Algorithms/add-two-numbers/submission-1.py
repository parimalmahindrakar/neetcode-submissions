# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(-1)
        curr = res_head
        carry = 0

        while head1 or head2 or carry:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0
            summation = val1 + val2 + carry
            reminder = summation % 10
            carry = summation // 10
            new_node = ListNode(val=reminder)
            curr.next = new_node

            if head1: head1 = head1.next
            if head2: head2 = head2.next
            curr = curr.next

        if carry:
            new_node = ListNode(val=carry)
            curr.next = new_node

        return res_head.next


             
        