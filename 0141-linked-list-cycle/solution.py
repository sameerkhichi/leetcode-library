# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Itterate through the list
#store each node in a dictionary
#on each pass check if the node is already in the dictionary
#if it is - you have a cycle.
class Solution(object):
    def hasCycle(self, head):
        #To try and solve this with O(1) space complexity it has to be done without memory
        #We can use Floyd's cycle finding algorithm where there is a slow and a fast pointer
        #if they ever meet it mustve been in a cycle
        #if the fast pointer gets to the end of the list - then there is no cycle.

        fast = head
        slow = head

        if head is None:
            return False
        
        while fast is not None and fast.next is not None:
            
            #fast moves by two while slow moves by one
            fast = fast.next.next
            slow = slow.next

            #check for cycle
            if slow == fast:
                return True
        
        #if fast got to the end of the list that means there is no cycle
        return False

        
        """ Solved at O(n) space and time 
        :type head: ListNode
        :rtype: bool
        """

        """
        if (head is None):
            return False

        if (head.next is None):
            return False

        if(head.val is None):
            return False

        nodeDict = {}

        while (head.next is not None):
            
            currNode = head.next #hey dont be stupid you didnt use this variable in the loop condition

            if currNode in nodeDict:
                return True
            
            nodeDict[currNode] = currNode.val

            head = head.next


        return False
        """
            
