
# 3. Longest Substring Without Repeating Characters
# Topics: Hash Table, String, Sliding Window
# Difficulty: Medium
# Time: You should aim for a solution with O(n) time and O(m) space, 
# where n is the length of the string and m is the number of unique characters in the string.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):     # len(s) == 7 -> range(7)
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

if __name__ == "__main__":
    sol = Solution()
    str = "zxyzxyz"
    print(sol.lengthOfLongestSubstring(str))