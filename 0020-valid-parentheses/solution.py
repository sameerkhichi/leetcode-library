class Solution(object):
    #to solve this question we can use a stack
    #for each letter in the string check it 
    #if it is any of the open bracket types - add it to the stack
    #if it is a closed bracket - pop from the stack - check if it is the same bracket type
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #edge case where its only one character - always false
        if len(s) == 1: return False

        #initialize the stack
        stack = []

        for char in s:
            
            #if it is an opening character put it in the stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            
            #if the character is a closing braket - pop the stack and check if its the same bracket type
            if char == ')':
                if len(stack) == 0: return False #if the stack is empty when it gets to a closed bracket, that means a bracket was never opened
                start = stack.pop()
                if start == '(':
                    continue
                else:
                    return False 

            elif char == '}':
                if len(stack) == 0: return False
                start = stack.pop()
                if start == '{':
                    continue
                else:
                    return False

            elif char == ']':
                if len(stack) == 0: return False
                start = stack.pop()
                if start == '[':
                    continue
                else:
                    return False
        
        #if there is still something in the stack there are brackets were never closed
        if len(stack) > 0: 
            return False
        else:
            return True
