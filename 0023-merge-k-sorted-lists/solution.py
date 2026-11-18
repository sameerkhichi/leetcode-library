# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Itterate through the array of lists with two pointers one after the other, keep track of the 3rd one (after the two pointers)
#Merge the two that are pointed to by the pointers
#Then merge that with the one after and continue
#To merge use the same approach used in leetcode 21
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        #From leetcode 21
        def mergeTwo(list1, list2):
            #leveraging a dummy node to make a new list
            dummy = ListNode(-1)
            tail = dummy

            while list1 and list2:
                
                #depending on what value is smaller - merge it in
                if list1.val > list2.val:
                    list2Next = list2.next
                    tail.next = list2
                    list2 = list2Next
                    tail = tail.next
                else:
                    list1Next = list1.next
                    tail.next = list1
                    list1 = list1Next
                    tail = tail.next

            #When theres only one list left just append it to the end of the current list builder
            if list1 and not list2:
                tail.next = list1
            if list2 and not list1:
                tail.next = list2
            
            return dummy.next

        #if theres empty lists or no list just return nothing
        if not lists: return None

        #Now we need to go through the array with two pointers - merging the one at pointer1 with pointer2 and continue until we get to the end of the array
        currList = lists[0] #The current list is the first one
        nextListIndex = 1 #The next one is one index after
        while nextListIndex < len(lists):
            #Just keep merging the current one with the next and continue changing the current merged to the newly created list
            currList = mergeTwo(currList, lists[nextListIndex])
            nextListIndex += 1 #make sure to update the next pointer
        
        return currList


