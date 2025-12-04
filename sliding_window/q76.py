# 76. Minimum Window Substring

# Topics: Hash Table, String, Sliding Window

# Difficulty: Hard

# Recommended Time & Space Complexity:
# You should aim for a solution with O(n) time and O(m) space, 
# where n is the length of the string s and m is the number of unique characters in s and t.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res      # unpack res = [9, 12]
        return s[l: r + 1] if resLen != float("infinity") else ""

if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))