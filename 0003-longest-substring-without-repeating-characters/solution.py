class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Dynamic sliding window 2 pointers
        
        char_map = {} #dictionary with index:char mappings. (so left pointer can jump to the duplicate found)
        left = 0 #left pointer
        max_length = 0

        #right is the right pointer itterating through the string
        for right, char in enumerate(s):

            #found a duplicate that is within the window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1 #left pointer moves directly one after where the first duplicate of the pair was kicking it out of the window.
            
            char_map[char] = right #newest position for the current character {we move one to the right storing the current character position pair}

            #the max length only increases if the current window length is bigger than what was already stored.
            max_length = max(max_length, ((right - left) + 1))

        return max_length


    
    """
    This one wont work either because the pointers wont catch a duplicate anywhere that isnt the start and end of the string. I need a combination of the two.
        #sliding window 2 pointers
        i = 0 #left pointer
        j = 1 #right pointer
        longest_streak = 0
        current_streak = 0

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        for char in s:
            if s[i] == s[j]:
                longest_streak = max(longest_streak, current_streak)
                i += 1
                j += 1
                current_streak = 0

            if j == (len(s)-1):
                break

            current_streak += 1
            j += 1
            print(i,j)


        return max(longest_streak, current_streak)
        """

    """
        This solution wouldnt work because it couldnt track where the duplicate started when one was found eg 1R1T7 kept returning 3 intead of 4
        This solution needs sliding window
        if len(s) == 0:
            return 0

        longest_streak = 1
        index = 0
        characters = {}
        counter = 0

        for char in s:
            if char in characters:
                longest_streak = max(longest_streak, len(characters))
                characters = {}
                counter += 1
        
            characters[char] = index
            index +=1
        
        if counter == 0:
            return len(s)
        

        print(longest_streak, len(characters))
        print(characters)
        return max(longest_streak, len(characters))
    """


