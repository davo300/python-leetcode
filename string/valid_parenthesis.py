class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Python program to
        # demonstrate stack implementation
        # using list
        if not s:
            return True
        
        if len(s) > 10**4:
            return False
        
        stack = []
        for i in range(len(s)):
            input = s[i]
            # append() function to push
            # element in the stack

            if input == '(' or input == '[' or input == '{':
                stack.append(input)
            elif input == ')' or input == ']' or input == '}':
                if not stack:
                    return False
                top = stack.pop()
                if input == ')' and top != '(' or input == ']' and top != '[' or input == '}' and top != '{':
                    return False
                
    
        if not stack:
            return True
        else:
            return False 

if __name__ == "__main__":
    s = Solution()
    str = "()"
    print(s.isValid(str))       