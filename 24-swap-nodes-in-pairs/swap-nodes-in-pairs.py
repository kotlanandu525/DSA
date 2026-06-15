# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0,head)
        dummy.next=head
        prev=dummy
        while prev.next and prev.next.next:
            a=prev.next
            b=prev.next.next

            prev.next=b
            a.next=b.next
            b.next=a

            prev=a
        return dummy.next


