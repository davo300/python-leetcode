class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_count = r_count = max_len = 0
        
        i = 0  # start from the beginning of the string

        while i < len(s):
            if s[i] == "(":
                l_count += 1    # left count means (
            else:
                r_count += 1    # right count mean )

            # if the parenthesis are well formed
            if l_count == r_count:
                max_len = max(max_len, l_count + r_count)
            elif r_count > l_count:     
                l_count = r_count = 0
            
            i += 1
        
        l_count = r_count = 0
        
        i = len(s) - 1  # start from the end of the string
        while i >= 0:
            if s[i] == "(":
                l_count += 1
            else:
                r_count += 1
            
            # if the parenthesis are well formed
            if l_count == r_count:  
                max_len = max(max_len, l_count + r_count)
            elif l_count > r_count:     # opposite from above
                l_count = r_count = 0

            i -= 1

        return max_len


if __name__ == "__main__":
    s = Solution()
    str = "((()" 
    print(s.longestValidParentheses(str))       