class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dictionary = {}

        #enumerate gives index and value
        #is is the index
        #num is the value at index i
        for i, num in enumerate(nums):
            
            remainder = target - num

            if remainder in dictionary:
                return [dictionary[remainder], i]

            dictionary[num] = i
            