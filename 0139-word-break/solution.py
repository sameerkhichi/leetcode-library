class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict) # Sets give fast O(1) lookups
        length = len(s)
        
        # dp[i] will store True if a valid word combination ends at index i
        dp = [False] * (length + 1) #this is a boolean array
        dp[0] = True # Base case: empty string prefix is always 'matched'
        
        for i in range(1, length + 1):
            for j in range(i):
                # instead of building a string - check the slice s[j:i]
                # BUT we only care if the prefix before it (dp[j]) was also a valid match!
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # We found a valid way to reach index i, move to next character
                    
        return dp[length]

