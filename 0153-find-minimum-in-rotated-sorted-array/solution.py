class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Some base cases as the algorithm I made works best for arrays of length 3 and larger
        if not nums: return None

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return min(nums[0], nums[1])

        curr = len(nums)//2 #Start at the middle of the array
        #establish pointers
        left = curr - 1
        right = curr + 1
        smallest = None #Just to get the loop running

        while not smallest: #should return before this condition gets evaluated as false
            
            #loop to the other end if we are on the edge of the array
            if curr == 0:
                left = len(nums) - 1
            if curr == len(nums) - 1:
                right = 0
            
            #if the current number is smaller than the one to the right and left, then we are at the smallest number
            if nums[right] > nums[curr] and nums[left] > nums[curr]:
                smallest = nums[curr]
                return smallest
            
            #if either one is less that the current number - we should move to it
            if nums[right] < nums[curr] or nums[left] < nums[curr]:
                #move to the smaller one between left and right and update the pointers
                if nums[right] < nums[left]:
                    curr = right
                    right = curr + 1
                    left = curr - 1
                else: #they cant be equal since items are unique and if they both were smaller this wouldve finished already.
                    curr = left
                    left = curr - 1
                    right = curr + 1
            
        
