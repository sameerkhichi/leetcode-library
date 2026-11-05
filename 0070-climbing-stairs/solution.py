class Solution(object):
    #n is the number of steps it takes to get to the top of a staircase
    #You can either choose to step up one step or two.
    #To find the amount of distinct amount of ways to get to the top
    #we need permutations of n between 1 and 2.

    #We can see from pattern recognition that #of distinct ways to get n:
    ## distct ways to get n-1 + # fistct ways to get n-2

    #start with the knowns of n = 2 and n = 3 and work your way up to n
    #at each step size store it in a dictionary to use for the next step size up to n.
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3

        counter = 4
        dictionary = {}
        dictionary[2] = 2
        dictionary[3] = 3 

        while counter <= n:
            
            #formula to get current number of distinct ways for the current step size
            ways = dictionary[counter-1] + dictionary[counter-2]

            dictionary[counter] = ways
            
            #next staircase size
            counter += 1

        return dictionary[n]
        
