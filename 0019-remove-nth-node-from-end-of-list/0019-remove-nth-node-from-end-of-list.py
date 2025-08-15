# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return  
        dummy = ListNode(0, head)
        left, right, index = dummy, dummy, 0
        while index < n:
            right = right.next
            index += 1
            
        while right.next:
            left = left.next
            right = right.next

        curr = left 
        curr.next = curr.next.next
        return dummy.next
            
        