class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Topics: Two Pointers, String, String Matching
        # The main idea here is to check all the substrings
        # of the haystack string until we find the needle string.
        if needle == "":
            return 0
        # In Python, range(stop) goes up to but excludes stop,
        # so +1 ensures the last possible substring starting point is included.
        for i in range(len(haystack) + 1 - len(needle)):
            # sequence[start:stop:step]
            # in test case 1, haystack[i: i + len(needle)] = 'sad' = haystack[0:3] 
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(s.strStr(haystack, needle))