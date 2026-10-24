class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        def calculateArea(left,right):
            #area is calculated by the shortest end by the distance they values are to eachother
                wallHeight = min(height[left],height[right])
                wallLength = right-left
                return (wallHeight*wallLength)


        #in the event the array is just two values
        if len(height) == 2:
            ht = min(height[0],height[1])
            return (ht*ht)
        
        maxArea = 0
        left = 0
        right = len(height)-1

        while left < right:
            currentArea = calculateArea(left,right)
            maxArea = max(maxArea,currentArea)

            #only move the pointer that points to a shorter wall inward
            #Although inward reduces width = rudcing area
            #only way to increase area is find a taller limiting wall.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea




    """ This worked but runs 0(n^2) and exceeds time limit - right thinking but need something more efficient
    #to form a container with the most water, you need to optimize and find the MAXIMUM. You want the tallest possible bar that are far enough apart.
    #itterate through the array starting in the middle and working your way out.
    #you need to do this for each item in the array as you have to check EVERY combination
    #Starting in the middle has two cases a array of even and odd length
    #store each area in a dictionary, the key being an array of the left and right pointers, the value being the area
    def maxArea(self, height):
        """
    """
        :type height: List[int]
        :rtype: int
    """
    """

        #in the event the array is just two values
        if len(height) == 2:
            ht = min(height[0],height[1])
            return (ht*ht)
        
        #dictionary to store areas that we have found to compare for the largest
        areas = list()

        def calculateArea(left,right):
            #area is calculated by the shortest end by the distance they values are to eachother
                wallHeight = min(height[left],height[right])
                wallLength = right-left
                return (wallHeight*wallLength)

        def expandOutward(left, right):
            #while the pointers are within the bounds of the array
            #need to check three cases, add one to the right, add one to the left, then add both sides.
            while (left >= 0 and right < len(height)):
                
                #check area before moving
                areas.append(calculateArea(left,right)) #store the area in the list
                #itterate the pointers
                left-=1
                right+=1

        for i, val in enumerate(height):
            
            expandOutward(i,i+1)
            expandOutward(i,i)

        print(areas)
        
        return max(areas)
    """ 
