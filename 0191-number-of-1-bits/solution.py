class Solution(object):
    
    #To find out how many set bits there are in a positive integer n
    #First convert the number into its binary form
    #each time you get a remainder while converting incrememnt a counter
    #no need to continue, you can just return the counter
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        counter = 0
        
        while n > 0:
            remainder = n%2

            if remainder == 1:
                counter += 1

            n = n//2

        return counter
