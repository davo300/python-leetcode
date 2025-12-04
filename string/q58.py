# 58. Length of Last Word
# Topics: String


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0   # i = 11 - 1 = 10
        
        while s[i] == " ":      # check for trailing whitespaces
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length




if __name__ == "__main__":
    s = Solution()
    str = "Hello World"
    print(s.lengthOfLastWord(str))    # output: 5
