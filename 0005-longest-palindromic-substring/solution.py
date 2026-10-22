class Solution(object):
    
    def longestPalindrome(self, s):

        #Apply sliding window
        #right moves through the string one by one
        #each step check if the new character will make a palindrome
        #if it does NOT create one, left shift forward by ONE
        #if it DOES create one, left stays put and we check next character to the right for a longer one

        if not s:
            return ""

        left = 0
        longest = 1 #the baseline is for the longest palindrome is 1
        start_index = 0 #tracking the start index for the curernt best palindrome (starts with the first letter)

        for right in range(len(s)):
            
            #check if a new ODD palindrome formed
            # an odd palindrome range would be from right - (longest - 1) to right (did it beat the curernt longest palindrome)
            odd_start = right - longest - 1
            if odd_start >= 0 and s[odd_start : right + 1] == s[odd_start : right + 1][::-1]:
                start_index = odd_start
                longest +=2 #next odd number would be 3 (1 +2)
                continue #next itteration

            #check if a new EVEN palindrome formed
            # an even palindrome range would be from right - longest to right(so checking length 2, 4 .....)
            even_start = right - longest
            if even_start >= 0 and s[even_start : right + 1] == s[even_start : right + 1][::-1]:
                start_index = even_start
                longest += 1 #next even number = 2 (1+1)
                continue

            #if neither happened move left pointer right by one
            left += 1

        return s[start_index : start_index + longest]


    
    
    """ this didnt work because it didnt check for palindromes larger than 2 length
    def _reverseString(self, s):
        
        reverse = ""
        length = len(s)
        right = length - 1
        for char in s:
            if right <= 0:
                reverse = reverse + s[right]
                break
            else:
                reverse = reverse + s[right]
                right -= 1

        return reverse
            
    
    
    def longestPalindrome(self, s):
        """
    """
        :type s: str
        :rtype: str
        """
    """
        #apply dynamic sliding window
        #Right pointer should itterate through the string
        #Left should move to right when the window is no longer considered a pallindrome
        #Just before Left moves - it should store the window into a dictionary ith its length to then compare later for the longest substring.


        strlength = len(s)

        if strlength == 1:
            return s

        pallindromes = {}
        left = 0

        #itterate through the entire string
        for right, char in enumerate(s):

            #Build the string in the window
            windowString = ""
            for i in range(left, right):
                windowString = windowString + s[i]

            #if the reverse of the string is the same as the window string then add it to the dictionary
            if windowString == self._reverseString(windowString):
                pallindromes[windowString] = len(windowString)
            else:
                left = right #if it wasnt then slide left to right.

        
        return max(pallindromes, key=pallindromes.get)
            


    """
