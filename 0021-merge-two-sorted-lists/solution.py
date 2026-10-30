# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        #create a dummy node to create a new list.
        #itterate through the two original lists comparing each nodes value
        #whichever one is smaller - add it to the new list - it then naturally increments
        #When one list empties you can just append the rest of the remaining list as they are sorted already

        dummy = ListNode(-1)
        tail = dummy
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:

            if curr1.val > curr2.val:
                curr2next = curr2.next
                tail.next = curr2
                curr2 = curr2next
                tail = tail.next
            else:
                curr1next = curr1.next
                tail.next = curr1
                curr1 = curr1next
                tail = tail.next
            
        #if one list is empty and the other isnt just append the remaining values to the end of the new list 
        if not curr1 and curr2:
            tail.next = curr2
        if not curr2 and curr1:
            tail.next = curr1
        
        #the new head starts one after the dummy
        return dummy.next




        """ This solution had a lot of edge case bugs 
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        if not list1: return list2
        if not list2: return list1
        if not list1 and not list2: return None

        if not list1.next and not list2.next:
            if list1.val > list2.val:
                list2.next = list1
                return list2
            else:
                list1.next = list2
                return list1

        curr1 = list1
        curr2 = list2
        prev1 = None
        prev2 = None

        while curr1 and curr2:

            print(curr1, curr2)

            #Based on which node is bigger is what decides if a node moves before or after a current node
            if curr1.val < curr2.val: #if the node from list 1 is smaller than the node in list2 move it before curr2
                #keep track of the next nodes for each list current pointer
                curr2next = curr2.next 
                curr1next = curr1.next
                curr1.next = curr2 #set the next node for the one we are moving in to the current node in main list (moving node left of the other)
                if prev2: #there wont be one when were still at the head in the original list
                    prev2.next = curr1 #ensure the left side of original list connects to the new node we are putting in
                prev2 = curr1 #move previous up one
                curr1 = curr1next #increment the merge in list to the next one over

            elif (curr1.val >= curr2.val and (curr1.val < curr2.next)): #node val must be smaller than curr2 next and larger than curr2
                curr1next = curr1.next
                curr2next = curr2.next
                curr2.next = curr1
                curr1.next = curr2next
                prev2 = curr2
                curr2 = curr1
                curr1 = curr1next

            #increment the list 2 pointers - dont intterate list1 pointers as we remove nodes from it into list 2
            prev2 = curr2
            curr2 = curr2.next
        
        return list2
        """


