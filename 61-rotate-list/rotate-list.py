# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        n=0
        temp=head

        while temp:
            n+=1
            temp=temp.next

        rot=k%n
        i=n-rot-1

        temp1=head
        while i:
            temp1=temp1.next
            i-=1
        
        temp2=temp1
        while temp2.next:
            temp2=temp2.next
        
        temp2.next=head
        head=temp1.next
        temp1.next=None

        return head