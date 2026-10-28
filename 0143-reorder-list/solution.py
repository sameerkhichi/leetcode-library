# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#split the list down the middle
#reverse only the second half of the list
#add nodes to the original head alternating between the first and second half going forward.
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        #find and split the list down the middle
        #apply slow/fast pointer approach
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        #slow.next is now at the middle of the list so we can label it as the head in the middle.
        middleHead = slow.next
        #seperate the two lists
        slow.next = None

        #reverse the list from the middleHead onward
        #to reverse a single linked list is just going through with two pointers prev and curr
        prev = None
        curr = middleHead

        while curr:
            #temporarily store the next connection before getting rid of it
            tempNext = curr.next
            #point backwards
            curr.next = prev
            #move the pointers along in the right order.
            prev = curr
            curr = tempNext
        #as the loop finishes - prev becomes the new head with prev.next being none
        middleHead = prev

        #so now we have middleHead a reverse half slice of the orignal list - we can sew the two halves together again alternating
        first = head
        second = middleHead
        while second:
            #store the connect before you sever it
            firstTempNext = first.next 
            secondTempNext = second.next
            
            #perform the reorder
            first.next = second
            second.next = firstTempNext

            #update the pointers
            first = firstTempNext
            second = secondTempNext





        
