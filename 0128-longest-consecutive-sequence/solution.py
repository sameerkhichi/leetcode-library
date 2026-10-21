class Solution(object):

    def longestConsecutive(self,nums):

        if len(nums) == 0:
            return 0

        num_set = set(nums) #converting array to a set - sets are implemented using a hash table - auto removes duplicates
        longest_streak = 1 #track the longest streak

        for num in num_set:

            if num - 1 not in num_set:

                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
    
    
    
    
    
    
    
    
    
    """
    #This solution is O(nlogn) - accepted but too slow.
    #list needs to be sorted from smallest to largest.
    #itterate through sorted array untill you find a break where the next number isnt exactly one more
    def longestConsecutive(self, nums):

        counter = 0
        current_streak=1
        longest_streak=1
        sorted_nums = sorted(nums) #sorts array in O(nlogn) time - may not be allowed in interviews or some questions.

        for i in range(1, len(sorted_nums)):

            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            #If consecutive, increase the current streak
            elif sorted_nums[i] == sorted_nums[i-1] + 1:
                current_streak += 1
            #If sequence breaks, reset the current streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
    
        return max(current_streak, longest_streak)
"""


