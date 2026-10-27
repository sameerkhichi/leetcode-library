class Solution(object):
    #First find out range by getting the length of the array
    #use a for loop to go from 0 to n = len(nums) and check if each one is in the list nums, whichever one isnt return it
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        range = len(nums)
        num_set = set(nums)
        counter = 0

        while counter <= range:

            if counter not in num_set:
                return counter
            
            counter += 1
        
