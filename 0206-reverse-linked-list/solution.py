# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#To reverse a singly linked list just go through each node tracking prev and next
#Have each pointer point backwards
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        curr = head

        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        
        return prev
        
