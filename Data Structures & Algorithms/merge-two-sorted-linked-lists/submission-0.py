# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        dummy = ListNode(0)
        prev = dummy

        while curr1 and curr2: 
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next
            else: 
                prev.next = curr2
                curr2 = curr2.next
            
            prev = prev.next
    
        if curr1: 
            prev.next = curr1
        if curr2: 
            prev.next = curr2
        
        return dummy.next