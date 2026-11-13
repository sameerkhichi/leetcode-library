class Solution(object):
    def maxProduct(self, nums):
        #The best way to solve this question is using dynamic programming. 
        #The subquestion in this question is just asking what is the absolute maximum (and minimum) product of a subarray that must end at exactly index i. 
        #If we can find the answer to that question at each step, the maximum of those answers would be the answer to the bigger qestion.

        #the reason that we need to keep track of the minimum as well is because storing the lowest number if it is negative, and we have another really low negative number later, multiplying them together creates a really big positive number which could be the new global maximum.

        #empty case
        if not nums: return 0

        global_max = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]

        for i in range(1,len(nums)):

            num = nums[i]
            
            #if the number is negative flipping the current maximum and current minimum should take care of the flip thanks to the -
            if num < 0:
                temp = curr_min
                curr_min = curr_max
                curr_max = temp

            #find the max and min between the current number alone and the current number multiplied with the rest of the #'s before it
            curr_min = min(num, curr_min*num)
            curr_max = max(num, curr_max*num)

            #find out what the largest product is - the one we had or the new maximum at this step
            global_max = max(curr_max, global_max)

        
        return global_max







        """ This one ALSO didnt work it misses things like [-2,3,-4]
        #Use a dynamic sliding window approach
        #Move a window along, calculating the product at each step. 
        #If moving right caused the product of the window to go down, check what number it is
        #if the number was 0 move left and right to rigth after that number and set a checker to true
        #if the number was not 0 move both left and right TO that number and continue. 

        if len(nums) <= 1:
            return nums[0]

        left = 0
        right = left+1
        bestProduct = nums[0]
        finalProduct = 0
        zeroPresent = False

        for num in nums:

            if right <= len(nums)-1:
                print(nums[left])
                print(nums[right])
                #finding the product of the window after moving right
                windowProduct = bestProduct*nums[right]
            else:
                finalProduct = bestProduct
                break

            if windowProduct < bestProduct:
                if nums[right] == 0:
                    zeroPresent = True
                    right += 1
                    left = right
                    if bestProduct > finalProduct:
                        finalProduct = bestProduct
                        print("FINAL PRODUCT UPDATED")
                        print(finalProduct)
                    bestProduct = nums[right]

                else:
                    left = right
                    if bestProduct > finalProduct:
                        finalProduct = bestProduct
                        print("FINAL PRODUCT UPDATED")
                        print(finalProduct)
                    bestProduct = nums[right]

            if windowProduct > bestProduct:
                bestProduct = windowProduct

            if right < len(nums)-1:
                right += 1
            
        if finalProduct<0 and zeroPresent:
            return 0
        else:
            return finalProduct
        """   

        
        """
        #this wont work either as it misses cases that require you to look to the left or right of negatives.
        #Start in the middle and work your way out
        #each time just add the number to the right and or the left only if it increases the product
        left = len(nums)//2
        right = left
        bestProduct = nums[left]

        while left >= 0 or right <= len(nums)-1:

            #careful for the case where it would be better to check all to the left or right of a 0
            if left > 0:
                addLeft = bestProduct*nums[left-1]
            if right < len(nums)-1:
                addRight = bestProduct*nums[right+1]
            
            if addLeft > bestProduct and left>0:
                left -= 1
                bestProduct = addLeft
            if addRight > bestProduct and right<len(nums)-1:
                right +=1
                bestProduct = addRight
            
            left -= 1
            right += 1
        
        return bestProduct
        """







        """ This didnt work because it misses 0 cases and uses floor division 
        :type nums: List[int]
        :rtype: int
        """
        """
        left = 0
        right = len(nums)-1
        bestProduct = 0

        #find the product of all values in the array 
        for num in nums:
            if bestProduct == 0:
                bestProduct = bestProduct + num
            else:
                bestProduct = bestProduct*num

        while left < right:
            
            #evaluate what the window product would be shringking from the left and the right
            dropLeftProduct = bestProduct//nums[left]
            dropRightProduct = bestProduct//nums[right]

            #determine if shrinking window makes a difference, then shrink and store the current best product.
            if dropLeftProduct > dropRightProduct:
                if dropLeftProduct > bestProduct:
                    left += 1
                    bestProduct = dropLeftProduct
            if dropRightProduct > dropLeftProduct:
                if dropRightProduct > bestProduct:
                    right -= 1
                    bestProduct = dropRightProduct
            if dropLeftProduct == dropRightProduct:
                if dropRightProduct > bestProduct:
                    right -= 1
                    bestProduct = dropRightProduct
                if dropRightProduct == bestProduct:
                    return bestProduct
            
            left += 1
            right -= 1
        
        return bestProduct
        """    

            
        
