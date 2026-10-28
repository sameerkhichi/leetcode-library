# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        self.counter = 0

        #check a node n places infront
        def checkNode(head, n):
            #base case
                if self.counter == n:
                    return head

                head = head.next
                self.counter += 1
                return checkNode(head, n) #hey dont forget the return at the end idiot this is python
        
        #if there is just one node - remove it
        if not head.next:
            return None

        curr = head
        prev = None

        #if its just removing the node at the end
        if n == 1:

            #just get to the end of the list and remove the last node
            while curr:
                if not curr.next:
                    if not prev:
                        prev = head
                    prev.next = None
                prev = curr
                curr = curr.next
        else: #if its not at the end - find out where the node is to remove it and get rid of it

            while curr:

                #checks the node n times infront of this one - check at each node
                nFromEnd = checkNode(curr, n)
                self.counter = 0 #reset the counter so that the recursive function runs right for the next node

                #if the recursive function finds n steps from now is none - remove the current node
                if not nFromEnd:
                    if not prev: #if this is true that means we are removing the head
                        return curr.next #to remove the head just return everything BUT the head which is everything after the current node
                    else:
                        prev.next = curr.next
                        curr.next = None

                    return head
                
                #store previous and increment current
                prev = curr
                curr = curr.next

        return head
            
