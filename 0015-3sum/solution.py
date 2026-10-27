class Solution(object):
    # Sort the list
    # get a fixed number (each item will have to be a fixed number at some point to get all the possibilities)
    # Then use two pointers - one right after i, and the second at the end. 
    # Find the two numbers that when summed with the fixed number = 0, when it is found add it to the list
    # if one isnt found, inner loop breaks when left crosses right.
    # This then goes to the next fixed number
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        solList = list()
        sortedNums = sorted(nums) #sort nums array

        for i, num in enumerate(sortedNums):
            #resetting left and right pointers
            
            right = len(sortedNums) - 1
            left = i+1
            fixedNum = sortedNums[i] #relaized late that i returns the value not the index so this is redundant. and could just be num

            if i == right: #in the event the fixed number is the last number we dont want i to equal the right
                right = i-1

            while left < right: #so long as the left and right pointers dont cross
                tripleSum = sortedNums[left] + sortedNums[right] + fixedNum

                #check to see if there is a match
                if (tripleSum == 0) and (left != right != i):
                    triplet = [fixedNum, sortedNums[left], sortedNums[right]]
                    if triplet not in solList:
                        print(triplet)
                        print(i, left, right)
                        solList.append(triplet)
                
                #itterate pointers
                if tripleSum < 0: #if the sum is too small move right to make it bigger
                    left += 1
                else: #if it is too big move right to the left to make it smaller
                    right -= 1 #move right even if it is 0 since we need to check other combos with this fixed #
                    #could move left too it doesnt really matter 
        
 
        return solList
