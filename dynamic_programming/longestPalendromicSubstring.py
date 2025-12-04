class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length of middle index i.e. middle 'b' babad
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # r+1 becuase the splice is upper bound EXCLUSIVE
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even length of middle indicies i.e. 'bb' in cbbd
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # r+1 becuase the splice is upper bound EXCLUSIVE
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
    
if __name__ == "__main__":
    s = "cbbd"
    solution = Solution()
    ans = solution.longestPalindrome(s)
    print(ans)
