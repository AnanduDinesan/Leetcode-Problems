# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        mid=head
        if not head:
            return head
        if not head.next:
            head=head.next
            return head
        while fast and fast.next:
            mid=slow
            slow=slow.next
            fast=fast.next.next
        mid.next=slow.next
        return head