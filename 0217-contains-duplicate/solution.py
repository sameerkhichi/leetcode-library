class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Convert the numbers into a set which filters out duplicates 
        numSet = set(nums)

        #if the length of the set is smaller than the length of the array that means a duplicate was filtered out
        if len(numSet) < len(nums):
            return True
        
        return False

