class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # (Hashmap) stores character and its last index 
        max_len = 0
        start = 0  # start index of the current substring

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_len = max(max_len, i - start + 1)
        
        return max_len

def main():
    s = Solution()
    str = "abcabcbb"
    print(s.lengthOfLongestSubstring(str))
    
    


if __name__ == "__main__":
    main()