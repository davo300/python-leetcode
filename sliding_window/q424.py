
# 424. Longest Repeating Character Replacement
# Topics: Hash Table, String, Sliding Window
# Difficulty: Medium
# Time: You should aim for a solution with O(n) time and O(m) space, 
# where n is the length of the string and m is the number of unique characters in the string.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)    # Create count freq. map: get() function returns s[r] if it exists in count freq.map, 0 otherwise
            maxf = max(maxf, count[s[r]])               

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

if __name__ == "__main__":
    sol = Solution()
    s = "ABAB"
    k = 2
    print(sol.characterReplacement(s, k))