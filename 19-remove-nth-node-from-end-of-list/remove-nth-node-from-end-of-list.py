# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        temp=head
        if n == l:
            return head.next
        for _ in range(l-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head

