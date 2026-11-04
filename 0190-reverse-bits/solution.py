class Solution(object):
    #convert integer to binary
    #reverse the binary digits
    #conver the binary back to an integer

    #converting a 32 bit signed integer means using the 2's compliment strategey of diving the number by 2 constantly tracking the remainders 
    #Then write the remainders in reverse and add leading 0's untill it is 32 bits.
    #To solve this since we need to reverse the bits we can just divide the number by 2 and track the remainders, then just add 0's to the end instead of the beggining to 'reverse' it
    #we then have to convert that number back into an integer.
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #converting a 32 bit signed int to binary
        def toReverseBinary(n):

            binaryStr = ""

            #looping exactly 32 times to get all 32 bits.
            for i in range(32):
                remainder = n%2 #modulus gives us the remainder
                binaryStr += str(remainder) #build it out as a string to return later as a int
                n = n//2
            return binaryStr

        def toInt(n):
            return int(n, 2) #converting the binary from base 2 back to base 10 integer

        #convert to binary - reverse it - return the integer of the bianry
        return toInt(toReverseBinary(n))
