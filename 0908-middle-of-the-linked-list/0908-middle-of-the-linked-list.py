# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        def length(head):
            count = 0 
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count
        if length(head) == 1:
            return head

        middle = length(head) // 2 
        index  = 1
        curr = head
        while index < middle:
            index += 1
            curr  = curr.next
        head = curr.next
        return head
            
            




        
        