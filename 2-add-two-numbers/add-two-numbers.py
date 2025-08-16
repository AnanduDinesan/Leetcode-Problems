# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1,t2=l1,l2
        i=0
        carry=0
        head=ListNode(0)
        temp=head
        while t1!=None or t2!=None or carry:
            n1=t1.val if t1 else 0
            n2=t2.val if t2 else 0
            temp.next= ListNode((n1+n2+carry)%10)
            carry=(n1+n2+carry)//10
            temp=temp.next
            if t1: t1=t1.next
            if t2: t2=t2.next
        return head.next