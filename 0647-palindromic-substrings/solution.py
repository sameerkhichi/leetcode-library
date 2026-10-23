class Solution(object):
    #start from the middle and expand outwards
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0


        def expandWindowOutwards(left, right):
            
            #if the window is a pallindrome expand
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left-=1
                right+=1

        for i in range(len(s)):

            expandWindowOutwards(i, i + 1) #even length pallindromes
            expandWindowOutwards(i, i) #odd length pallindromes


        return self.count        







        """ This didnt work as it would miss multiple pallindromes on the way in from the outsides
        #Each letter in a string counts as a substring and palindrome - this will have to be added to the count (count + s.length + 1)

        length = len(s)
        pallindromeCount = 0
        count = 0 #to track what itterating we are on in the loop
        left = 0 #left pointer starts at the beggining of the string
        right = length - 1 #rigth pointer starts at the end of the string

        #As long as this is true - left and right pointers havent met in the middle of the string yet.
        while count < length - 1:
            print("TOWARDS MIDDLE")
            #if window is greater than one character 
            if ((abs(right - left)) >= 1) and right != left:
                #check if the window is a pallindrome
                if (s[left:right+1] == s[left:right+1][::-1]) and ((left >=0) and (right<=(length-1))):
                    print(left,right)
                    print(s[left:right+1],s[left:right+1][::-1])
                    pallindromeCount+=1 #increase the count
            
            #itterate the count
            count += 1

            print(s[left:right+1])

            #right moves first 
            if((count%2 != 0)):
                right -= 1
            #left moves on the next itterartion
            if((count%2 == 0)):
                left += 1

        print(count)

        #pointers met in the middle - now they go back the other way
        while (count < ((2*length) - 1)):
            print("BACK TO ENDS")
            #if window is greater than one character 
            if ((abs(right - left)) >= 1) and right != left :
                #check if the window is a pallindrome
                if (s[left:right+1] == s[left:right+1][::-1]) and ((left >=0) and (right<=(length-1))):
                    print(left,right)
                    print(s[left:right+1],s[left:right+1][::-1])
                    pallindromeCount+=1 #increase the count
            
            #itterate the count
            count += 1

            #right moves first back the direction it came from (end of string) 
            if((count%2 != 0)):
                right += 1
            #left moves on the next itterartion towards the beggining of the string
            if((count%2 == 0)):
                left -= 1
            
            #in the evnt the entire string is a pallindrome avoid adding it for a second time
            if((right == length-1) and (left == 0)):
                 if s[left:right+1] == s[left:right+1][::-1]:
                    pallindromeCount-=1
            
            print(s[left:right+1])

        #add the length of the string to the counter as each character is a pallindrome
        pallindromeCount = pallindromeCount + length

        print(count)
        return pallindromeCount
    """
