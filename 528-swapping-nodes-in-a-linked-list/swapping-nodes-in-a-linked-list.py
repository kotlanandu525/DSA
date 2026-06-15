# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        arr=[]
        dummy,curr=head,head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        n=len(arr)
        arr[k-1],arr[n-k]=arr[n-k],arr[k-1]
        i=0
        while head:
            head.val=arr[i]
            head=head.next
            i+=1
        return dummy