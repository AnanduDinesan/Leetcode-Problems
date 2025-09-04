# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count_dict={}
        while temp:
            count_dict[temp.val]=count_dict.get(temp.val,0)+1
            temp=temp.next
        temp=head
        result=rtemp=ListNode(0)
        while temp:
            if count_dict[temp.val]==1:
                rtemp.next=ListNode(temp.val)
                rtemp=rtemp.next
            temp=temp.next
        return result.next
