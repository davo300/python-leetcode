class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length of current string
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # r+1 becuase the splice is upper bound EXCLUSIVE
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even length of current string
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # r+1 becuase the splice is upper bound EXCLUSIVE
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))